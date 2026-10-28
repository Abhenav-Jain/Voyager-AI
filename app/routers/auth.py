"""
Auth & System Health Router:
Handles Supabase profile verification and returns runtime health diagnostics
including Transformer engine status and CPU/GPU memory detection.
"""

from fastapi import APIRouter
from app.models.schemas import UserProfile, TravelerType
from app.services.transformer_engine import transformer_engine
from app.database.db import db
from app.config import settings

router = APIRouter(prefix="/api/auth", tags=["Auth & System"])

@router.get("/profile", response_model=UserProfile)
def get_user_profile():
    """Returns the current user profile (or demo traveler profile)."""
    return UserProfile(
        id="usr_demo_882",
        email="traveler@example.com",
        full_name="Alex Morgan",
        preferred_currency="USD",
        default_traveler_type=TravelerType.SOLO,
        interests=["sightseeing", "food", "culture"]
    )

@router.get("/health")
def get_health_status():
    """Returns system status including the 3 Transformer models and database state."""
    engine_health = transformer_engine.get_system_health()
    return {
        "app_name": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "environment": settings.ENVIRONMENT,
        "transformer_engine": engine_health,
        "database": {
            "supabase_configured": db.is_supabase_connected,
            "storage_type": "Supabase PostgreSQL" if db.is_supabase_connected else "Local SQLite Engine"
        },
        "llm_provider": settings.LLM_PROVIDER,
        "has_gemini_key": bool(settings.GEMINI_API_KEY),
        "has_llama_key": bool(settings.LLAMA_API_KEY)
    }
