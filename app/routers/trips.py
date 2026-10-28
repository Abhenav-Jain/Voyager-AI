"""
Trips Router: API endpoints for generating, reading, updating, regenerating,
sharing, and exporting travel itineraries.
"""

import uuid
from fastapi import APIRouter, HTTPException, Query, Response
from typing import List, Optional

from app.models.schemas import (
    TripRequest, Itinerary, RegenerateDayRequest,
    ReplaceActivityRequest, ShareTripRequest
)
from app.services.ai_generator import ai_generator
from app.database.db import db

router = APIRouter(prefix="/api/trips", tags=["Trips"])

@router.post("/generate", response_model=Itinerary)
async def generate_trip(request: TripRequest, user_id: str = Query("guest")):
    """Generates an AI-powered personalized itinerary based on preferences."""
    try:
        itinerary = await ai_generator.generate_itinerary(request, user_id=user_id)
        # Save to database
        db.save_trip(itinerary)
        return itinerary
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to generate itinerary: {str(e)}")

@router.get("", response_model=List[dict])
def list_trips(user_id: Optional[str] = Query("guest")):
    """Lists saved trips for the user or guest."""
    return db.list_trips(user_id=user_id)

@router.get("/{trip_id}", response_model=Itinerary)
def get_trip(trip_id: str):
    """Retrieves a full itinerary by its ID."""
    itinerary = db.get_trip(trip_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Trip itinerary not found")
    return itinerary

@router.delete("/{trip_id}")
def delete_trip(trip_id: str):
    """Deletes an itinerary."""
    deleted = db.delete_trip(trip_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Trip not found")
    return {"message": "Trip successfully deleted", "trip_id": trip_id}

@router.post("/{trip_id}/regenerate-day", response_model=Itinerary)
def regenerate_day(trip_id: str, request: RegenerateDayRequest):
    """Regenerates a single day with customized alternative activities and themes."""
    itinerary = db.get_trip(trip_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    updated = ai_generator.regenerate_single_day(itinerary, request)
    db.save_trip(updated)
    return updated

@router.post("/{trip_id}/replace-activity", response_model=Itinerary)
def replace_activity(trip_id: str, request: ReplaceActivityRequest):
    """Replaces a specific activity with a tailored alternative."""
    itinerary = db.get_trip(trip_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    updated = ai_generator.replace_activity(itinerary, request)
    db.save_trip(updated)
    return updated

@router.post("/{trip_id}/share")
def share_trip(trip_id: str, request: ShareTripRequest):
    """Creates a public sharing link/code for collaborative viewing."""
    itinerary = db.get_trip(trip_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Trip not found")
    
    if not itinerary.share_code:
        itinerary.share_code = f"trip-{uuid.uuid4().hex[:8]}"
    itinerary.is_shared = request.is_public
    db.save_trip(itinerary)
    
    return {
        "share_code": itinerary.share_code,
        "share_url": f"/shared/{itinerary.share_code}",
        "is_shared": itinerary.is_shared
    }

@router.get("/shared/{share_code}", response_model=Itinerary)
def get_shared_trip(share_code: str):
    """Public read-only itinerary view for collaborators."""
    itinerary = db.get_shared_trip(share_code)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Shared trip not found or expired")
    return itinerary

@router.get("/{trip_id}/export")
def export_trip(trip_id: str, format: str = Query("markdown", pattern="^(markdown|ics|json)$")):
    """Exports itinerary in Markdown, JSON, or iCalendar format."""
    itinerary = db.get_trip(trip_id)
    if not itinerary:
        raise HTTPException(status_code=404, detail="Trip not found")

    if format == "json":
        return Response(
            content=itinerary.model_dump_json(indent=2),
            media_type="application/json",
            headers={"Content-Disposition": f"attachment; filename={itinerary.destination.lower()}-itinerary.json"}
        )

    if format == "markdown":
        md = [f"# {itinerary.title}", f"**Destination:** {itinerary.destination}", f"**Dates:** {itinerary.start_date} to {itinerary.end_date}", ""]
        md.append(f"**Traveler Style:** {itinerary.traveler_type.capitalize()} (Group Size: {itinerary.group_size}) | **Pacing:** {itinerary.pacing}")
        md.append(f"**Estimated Total Cost:** ${itinerary.estimated_total_cost:.2f} (${itinerary.cost_per_person:.2f} per person)")
        md.append("")
        md.append(f"> {itinerary.summary}")
        md.append("")
        for day in itinerary.days:
            md.append(f"## Day {day.day_number}: {day.theme} ({day.date})")
            if day.accommodation:
                md.append(f"*Stay:* **{day.accommodation.name}** ({day.accommodation.neighborhood}) - ~${day.accommodation.estimated_nightly_cost}/night")
            if day.logistics_notes:
                md.append(f"*Transit Tip:* {day.logistics_notes}")
            md.append("")
            for act in day.activities:
                md.append(f"- **[{act.time_slot.capitalize()} {act.start_time or ''}] {act.title}** (~${act.estimated_cost})")
                md.append(f"  {act.description}")
                if act.booking_tip:
                    md.append(f"  *Tip:* {act.booking_tip}")
            md.append("")
        return Response(
            content="\n".join(md),
            media_type="text/markdown",
            headers={"Content-Disposition": f"attachment; filename={itinerary.destination.lower()}-itinerary.md"}
        )

    # iCalendar (.ics) basic format
    ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//Personalized Travel Planner//EN"]
    for day in itinerary.days:
        for act in day.activities:
            ics.extend([
                "BEGIN:VEVENT",
                f"SUMMARY:{act.title}",
                f"DESCRIPTION:{act.description} (Tip: {act.booking_tip or 'None'})",
                f"LOCATION:{act.location}",
                f"DTSTART:{day.date.replace('-', '')}T100000Z",
                f"DTEND:{day.date.replace('-', '')}T120000Z",
                "END:VEVENT"
            ])
    ics.append("END:VCALENDAR")
    return Response(
        content="\r\n".join(ics),
        media_type="text/calendar",
        headers={"Content-Disposition": f"attachment; filename={itinerary.destination.lower()}-calendar.ics"}
    )
