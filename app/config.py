import os
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()

class Settings:
    APP_NAME: str = "Personalized Travel Itinerary Planner"
    APP_VERSION: str = "1.0.0"
    ENVIRONMENT: str = os.getenv("ENVIRONMENT", "development")
    
    # Supabase Configuration
    SUPABASE_URL: str = os.getenv("SUPABASE_URL", "")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY", "")
    
    # AI / LLM Configuration
    GEMINI_API_KEY: str = os.getenv("GEMINI_API_KEY", "")
    LLAMA_API_KEY: str = os.getenv("LLAMA_API_KEY", "")
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "auto") # "gemini", "llama", "local", or "auto"
    
    # Local Transformer Models Configuration (.keras / .pkl)
    MODELS_DIR: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "models_cache")
    ENABLE_LOCAL_TRANSFORMERS: bool = True
    
    # Database
    DATABASE_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "travel_planner.db")
    
    # Server Configuration
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", "8000"))
    CORS_ORIGINS: List[str] = ["*"]

settings = Settings()
