"""
Scenarios Router: Direct scenario endpoints matching the user's project requirements:
1. Scenario 1: Solo Traveler Weekend Getaway
2. Scenario 2: Couple Personalized Vacation
3. Scenario 3: Small Group Coordinating a Multi-Day Trip
"""

from fastapi import APIRouter
from app.models.schemas import TripRequest, TravelerType, BudgetLevel, PacingStyle, Itinerary
from app.services.ai_generator import ai_generator
from app.database.db import db

router = APIRouter(prefix="/api/scenarios", tags=["Scenarios"])

@router.get("/scenario-1", response_model=Itinerary)
async def get_scenario_1_solo_weekend():
    """
    Scenario 1: Solo Traveler Planning a Weekend Getaway
    A solo traveler wants a short 2-day weekend trip to Tokyo with limited time.
    Interests: Food, Sightseeing, Budget-friendly, Optimized transit clusters.
    """
    req = TripRequest(
        destination="Tokyo, Japan",
        start_date="2026-11-07",
        end_date="2026-11-08",
        traveler_type=TravelerType.SOLO,
        group_size=1,
        budget_level=BudgetLevel.BUDGET,
        target_budget_usd=250.0,
        interests=["food", "sightseeing", "culture"],
        pacing=PacingStyle.FAST,
        dietary_restrictions=[],
        special_requests="Maximize food markets, efficient subway routes, and vibrant street life."
    )
    itinerary = await ai_generator.generate_itinerary(req, user_id="solo_traveler_demo")
    itinerary.title = "Scenario 1: Solo Weekend Getaway in Tokyo"
    itinerary.highlight_quote = "A fast-paced, high-efficiency solo exploration of Tokyo's historic temples and street food alleys."
    db.save_trip(itinerary)
    return itinerary

@router.get("/scenario-2", response_model=Itinerary)
async def get_scenario_2_couple_vacation():
    """
    Scenario 2: Couple Planning a Personalized Vacation
    A couple planning a romantic 4-day escape to Florence.
    Preferences: Relaxed pacing, scenic viewpoints, premium stays, intimate dining, day regeneration.
    """
    req = TripRequest(
        destination="Florence, Italy",
        start_date="2026-11-14",
        end_date="2026-11-17",
        traveler_type=TravelerType.COUPLE,
        group_size=2,
        budget_level=BudgetLevel.LUXURY,
        target_budget_usd=1600.0,
        interests=["culture", "food", "relaxation"],
        pacing=PacingStyle.RELAXED,
        dietary_restrictions=["authentic local wine & pasta"],
        special_requests="Romantic sunset spots, leisurely mornings, historic boutique stay, and candlelit Tuscan trattorias."
    )
    itinerary = await ai_generator.generate_itinerary(req, user_id="couple_demo")
    itinerary.title = "Scenario 2: Couple's Romantic Escape to Florence"
    itinerary.highlight_quote = "A serene Tuscan journey featuring sunset Chianti aperitivos, Renaissance art, and candlelit osterias."
    db.save_trip(itinerary)
    return itinerary

@router.get("/scenario-3", response_model=Itinerary)
async def get_scenario_3_group_trip():
    """
    Scenario 3: Small Group Coordinating a Multi-Day Trip
    A group of 4 friends organizing a 4-day adventure holiday in Barcelona.
    Blended preferences: Adventure, Culture, Nightlife, and shared group logistics.
    """
    req = TripRequest(
        destination="Barcelona, Spain",
        start_date="2026-11-20",
        end_date="2026-11-23",
        traveler_type=TravelerType.GROUP,
        group_size=4,
        budget_level=BudgetLevel.MODERATE,
        target_budget_usd=2200.0,
        interests=["adventure", "food", "nightlife", "culture"],
        pacing=PacingStyle.BALANCED,
        dietary_restrictions=["tapas friendly", "vegetarian options"],
        special_requests="Group-friendly tapas crawls, beach activities, Gaudí landmarks, and clear split-cost tracking."
    )
    itinerary = await ai_generator.generate_itinerary(req, user_id="group_friends_demo")
    itinerary.title = "Scenario 3: Small Group Multi-Day Adventure in Barcelona"
    itinerary.highlight_quote = "A synchronized 4-friend adventure balancing architectural marvels, beach relaxation, and spirited tapas crawls."
    db.save_trip(itinerary)
    return itinerary
