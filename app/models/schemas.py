from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from enum import Enum
from datetime import datetime

class TravelerType(str, Enum):
    SOLO = "solo"
    COUPLE = "couple"
    GROUP = "group"
    FAMILY = "family"

class BudgetLevel(str, Enum):
    BUDGET = "budget"
    MODERATE = "moderate"
    LUXURY = "luxury"

class PacingStyle(str, Enum):
    RELAXED = "relaxed"
    BALANCED = "balanced"
    FAST = "fast-paced"

class ActivityCategory(str, Enum):
    ATTRACTION = "attraction"
    DINING = "dining"
    ACCOMMODATION = "accommodation"
    TRANSPORT = "transport"
    CULTURE = "culture"
    NIGHTLIFE = "nightlife"
    OUTDOORS = "outdoors"
    RELAXATION = "relaxation"

class Activity(BaseModel):
    id: str = Field(..., description="Unique identifier for the activity")
    title: str = Field(..., description="Activity title or venue name")
    category: str = Field(default="attraction", description="Category of activity")
    time_slot: str = Field(..., description="morning, afternoon, evening, night")
    start_time: Optional[str] = Field(None, description="e.g. 09:30 AM")
    duration_minutes: int = Field(default=90, description="Duration in minutes")
    description: str = Field(..., description="Detailed description and why it fits user's style")
    location: str = Field(..., description="Area, address, or landmark")
    estimated_cost: float = Field(default=0.0, description="Estimated cost in USD")
    tags: List[str] = Field(default_factory=list, description="Descriptive tags")
    booking_tip: Optional[str] = Field(None, description="Reservation or queue tip")

class DayAccommodation(BaseModel):
    name: str = Field(..., description="Recommended hotel, boutique stay, or hostel")
    type: str = Field(default="Hotel", description="Hostel, Boutique Hotel, Luxury Resort, Airbnb")
    neighborhood: str = Field(..., description="Recommended area to stay")
    estimated_nightly_cost: float = Field(default=100.0, description="Cost per night in USD")
    rating: Optional[float] = Field(default=4.5)

class DayPlan(BaseModel):
    day_number: int = Field(..., description="1-indexed day number")
    date: str = Field(..., description="YYYY-MM-DD or formatted date")
    theme: str = Field(..., description="Day theme (e.g., Historic Heart & Rooftop Sunset)")
    accommodation: Optional[DayAccommodation] = None
    activities: List[Activity] = Field(default_factory=list)
    day_budget_estimate: float = Field(default=0.0, description="Total budget for this day")
    logistics_notes: Optional[str] = Field(None, description="Transport advice, transit pass, or route cluster tip")

class TripRequest(BaseModel):
    destination: str = Field(..., example="Tokyo, Japan")
    start_date: str = Field(..., example="2026-11-10")
    end_date: str = Field(..., example="2026-11-12")
    traveler_type: TravelerType = Field(default=TravelerType.SOLO)
    group_size: int = Field(default=1, ge=1, le=50)
    budget_level: BudgetLevel = Field(default=BudgetLevel.MODERATE)
    target_budget_usd: Optional[float] = Field(None, description="Total target budget limit")
    interests: List[str] = Field(default_factory=lambda: ["sightseeing", "food"], example=["food", "sightseeing", "culture"])
    pacing: PacingStyle = Field(default=PacingStyle.BALANCED)
    dietary_restrictions: List[str] = Field(default_factory=list, example=["vegetarian", "gluten-free"])
    special_requests: Optional[str] = Field(None, example="Want scenic sunset spots and local markets")

class Itinerary(BaseModel):
    id: str
    user_id: Optional[str] = "guest"
    title: str
    destination: str
    country: Optional[str] = None
    start_date: str
    end_date: str
    total_days: int
    traveler_type: str
    group_size: int = 1
    budget_level: str
    pacing: str
    estimated_total_cost: float
    cost_per_person: float
    summary: str
    highlight_quote: str
    packing_suggestions: List[str] = Field(default_factory=list)
    local_tips: List[str] = Field(default_factory=list)
    days: List[DayPlan] = Field(default_factory=list)
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    updated_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
    is_shared: bool = False
    share_code: Optional[str] = None

class RegenerateDayRequest(BaseModel):
    day_number: int
    feedback: Optional[str] = "Provide alternative attractions and dining"
    pacing_change: Optional[str] = None

class ReplaceActivityRequest(BaseModel):
    day_number: int
    activity_id: str
    preference: Optional[str] = "Suggest a relaxed outdoor or cultural alternative"

class ShareTripRequest(BaseModel):
    collaborators: List[str] = Field(default_factory=list)
    is_public: bool = True

class UserProfile(BaseModel):
    id: str
    email: str
    full_name: Optional[str] = "Traveler"
    preferred_currency: str = "USD"
    default_traveler_type: TravelerType = TravelerType.SOLO
    interests: List[str] = Field(default_factory=lambda: ["sightseeing", "food"])
    created_at: str = Field(default_factory=lambda: datetime.utcnow().isoformat())
