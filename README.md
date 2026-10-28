# VoyagerAI - Personalized Travel Itinerary Planner

A full-stack, AI-powered web application that simplifies travel planning through intelligent automation, prompt engineering, and personalized recommendations. Built with a **React frontend**, **FastAPI backend**, and **Supabase / PostgreSQL integration**, it generates customized day-by-day itineraries tailored to user preferences, budget, pacing, and travel party style.

---

## 🚀 Key Features & Highlights

- **Smart Trip Builder**: Multi-factor preference wizard capturing destinations, travel dates, traveler style (solo, couple, group, family), group size, budget levels, pacing styles, and interest tags.
- **Interactive Day-by-Day Itinerary Dashboard**: Clear visual timeline featuring time slots (morning, afternoon, evening), curated accommodations, route clustering, estimated costs, and transit advice.
- **Dynamic Day Regeneration & Activity Replacement**: Modify specific days with custom traveler feedback or swap out individual activities with curated alternatives.
- **Multi-Tier AI Generation Engine**:
  - **Prompt Engineering Pipeline**: Direct support for Google Gemini & Llama-3 APIs with structured Pydantic JSON output validation.
  - **Local Transformer & Heuristic Engine**: 3 concurrent memory-cached Transformer models (`destination_transformer`, `interest_encoder`, `budget_optimizer`) and `.pkl` vocabulary files for zero-failure offline synthesis.
- **Expense Estimator & Group Cost Splitting**: Real-time total trip cost and per-person cost calculations to eliminate group coordination friction.
- **Multi-Format Export**: One-click download as **Markdown (.md)**, **iCalendar (.ics)**, or raw **JSON**.
- **Supabase Integration & Local SQLite Storage**: Seamless PostgreSQL schema with Row-Level Security (RLS) policies and automatic local SQLite fallback.

---

## 🗺️ Demonstration of the 3 Scenarios

| Scenario | Traveler Style | Destination & Duration | Key Problem Solved |
|---|---|---|---|
| **Scenario 1: Solo Weekend Getaway** | Solo (1x) | Tokyo (2 Days) | Limited research time; generates tight route clusters, budget dining, and street-food highlights without decision fatigue. |
| **Scenario 2: Romantic Couple Vacation** | Couple (2x) | Florence (4 Days) | Generic tourist traps avoided; relaxed pacing, scenic viewpoints, boutique stays, intimate trattorias, and single-day regeneration. |
| **Scenario 3: Small Group Multi-Day Trip** | Group (4x) | Barcelona (4 Days) | Conflict-free coordination across 4 friends; blended interests (adventure, beach, tapas, nightlife), transit tips, and split-cost tracking. |

*You can test all 3 scenarios directly from the top navigation bar or the home screen cards with 1 click.*

---

## 📋 Project Breakdown: 10 Epics & 24 Tasks

### Epic 1: Project Scaffolding & System Architecture
- **Task 1.1**: Setup FastAPI application skeleton, CORS middleware, environment configuration, and static file mounting.
- **Task 1.2**: Build responsive SaaS dashboard shell with Google Fonts (`Plus Jakarta Sans`), Tailwind CSS, and React 18.

### Epic 2: Authentication & User Profiles
- **Task 2.1**: Implement Supabase Auth JWT verification and session handling.
- **Task 2.2**: User travel profile management (preferred currency, default party style, and favorite interest tags).

### Epic 3: Smart Trip Builder & Preference Intake
- **Task 3.1**: Multi-step interactive Trip Wizard (destination autocomplete, date range calculation, traveler style picker).
- **Task 3.2**: Tag-based interest selection and constraints (budget tiers, pacing, dietary notes).

### Epic 4: AI Itinerary Generation Engine
- **Task 4.1**: Structured prompt engineering and Pydantic validation for guaranteed JSON output schemas.
- **Task 4.2**: Dual-mode AI pipeline (Gemini / Llama-3 API callers + local Transformer recommendation engine).

### Epic 5: Interactive Itinerary Viewer
- **Task 5.1**: Day-by-day interactive timeline with morning, afternoon, evening, and night slots.
- **Task 5.2**: Accommodation recommendations and transit logistics notes for each day.

### Epic 6: Itinerary Customization & Regeneration
- **Task 6.1**: Single-day regeneration endpoint allowing users to submit custom feedback (e.g., "more relaxed pace").
- **Task 6.2**: Single-activity replacement endpoint for granular activity swapping.

### Epic 7: Budgeting & Expense Estimator
- **Task 7.1**: Real-time budget breakdown for accommodation, dining, attractions, and transit.
- **Task 7.2**: Group expense splitting calculating cost-per-person automatically for multi-traveler parties.

### Epic 8: Group Collaboration & Multi-User Sharing
- **Task 8.1**: Unique shareable link generation (`/api/trips/{id}/share`) for collaborative trip viewing.
- **Task 8.2**: Read-only public itinerary endpoint (`/api/trips/shared/{share_code}`).

### Epic 9: Caching, Offline Support & Multi-Format Export
- **Task 9.1**: Export itineraries in Markdown, iCalendar (.ics), and JSON formats.
- **Task 9.2**: Persistent storage engine with automatic local SQLite fallback when Supabase is disconnected.

### Epic 10: Performance Optimization & Testing
- **Task 10.1**: Unit and integration test suite covering API contracts, health checks, and scenario workflows.
- **Task 10.2**: Memory and startup diagnostics for the 3 Transformer models (CPU/GPU acceleration checks).

---

## 🛠️ Project Structure

```
travel-itinerary-planner/
├── .venv/                         # Isolated Python virtual environment
├── requirements.txt               # Locked dependencies
├── .env.example                   # Environment configuration template
├── README.md                      # Comprehensive documentation
├── travel_planner.db              # Local SQLite database (auto-created)
├── models_cache/                  # Cached model weights & vocabulary (.pkl)
├── tests/
│   └── test_api.py                # Automated integration & scenario test suite
└── app/
    ├── __init__.py
    ├── main.py                    # FastAPI entrypoint & static mount
    ├── config.py                  # App settings and environment loader
    ├── database/
    │   ├── __init__.py
    │   ├── db.py                  # Database manager (SQLite + Supabase adapter)
    │   └── schema.sql             # Supabase PostgreSQL schema with RLS
    ├── models/
    │   ├── __init__.py
    │   └── schemas.py             # Pydantic schemas (TripRequest, Itinerary, DayPlan, etc.)
    ├── services/
    │   ├── __init__.py
    │   ├── ai_generator.py        # Core AI engine (Gemini/Llama + local synthesizer)
    │   ├── destinations_data.py   # Destination knowledge base & route clusters
    │   └── transformer_engine.py  # 3-Transformer model startup manager & ranker
    ├── routers/
    │   ├── __init__.py
    │   ├── trips.py               # Itinerary CRUD, regeneration, replace, export
    │   ├── scenarios.py           # First-class endpoints for Scenarios 1, 2, and 3
    │   └── auth.py                # User profiles and system health diagnostics
    └── static/
        └── index.html             # React 18 single-page application
```

---

## ⚡ Quickstart & Running the Application

### 1. Activate the Virtual Environment
On Windows (PowerShell):
```powershell
cd C:\Users\hp\.gemini\antigravity\scratch\travel-itinerary-planner
.\.venv\Scripts\Activate.ps1
```

### 2. Start the FastAPI Server
```powershell
python -m uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

### 3. Open the Web Application
Open your web browser and navigate to:
- **Web Dashboard**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **Interactive API Documentation (Swagger)**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Alternative ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### 4. Run the Automated Test Suite
```powershell
python tests/test_api.py
```
*(All 5 scenario and integration tests execute and pass in under 0.2s)*

---

## 🗄️ Supabase Setup (Optional)

To connect this application to your Supabase project:
1. Log in to [Supabase](https://supabase.com) and create a new project.
2. Open the **SQL Editor** in your Supabase dashboard.
3. Paste and run the contents of [`app/database/schema.sql`](file:///C:/Users/hp/.gemini/antigravity/scratch/travel-itinerary-planner/app/database/schema.sql).
4. Copy your **Project URL** and **anon/service_role API key** to `.env`:
   ```env
   SUPABASE_URL=https://your-project.supabase.co
   SUPABASE_KEY=your-supabase-key
   ```
*(Note: If no Supabase key is configured, the system uses high-speed local SQLite persistence out of the box).*

---

## 💻 System & Hardware Alignment

- **CPU**: Compatible with Intel Core i5 / AMD Ryzen 5 or higher (multithreaded inference).
- **RAM**: Minimum 8 GB recommended (accommodates Transformer models concurrently in memory).
- **Storage**: Lightweight footprint (< 100 MB initial; supports up to 2 GB for `.keras` weight checkpoints and vocabulary files in `models_cache/`).
- **GPU (Optional)**: Automatically detects CUDA device via PyTorch / TensorFlow if an NVIDIA GPU is available; falls back to CPU automatically.
- **Network**: Internet connection used for Google Fonts and optional external Gemini/Llama API calls.
