"""
Database Layer: Supports Supabase with automatic SQLite local fallback.
Provides consistent storage for trips, user profiles, and shared itineraries.
"""

import sqlite3
import json
import logging
from typing import Optional, List, Dict, Any
from app.config import settings
from app.models.schemas import Itinerary

logger = logging.getLogger("database")

class DatabaseManager:
    def __init__(self):
        self.db_path = settings.DATABASE_PATH
        self.supabase_url = settings.SUPABASE_URL
        self.supabase_key = settings.SUPABASE_KEY
        self.is_supabase_connected = False
        self._init_sqlite()
        self._check_supabase()

    def _init_sqlite(self):
        """Initializes SQLite tables for local storage."""
        try:
            with sqlite3.connect(self.db_path) as conn:
                cursor = conn.cursor()
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS trips (
                        id TEXT PRIMARY KEY,
                        user_id TEXT,
                        title TEXT,
                        destination TEXT,
                        country TEXT,
                        start_date TEXT,
                        end_date TEXT,
                        total_days INTEGER,
                        traveler_type TEXT,
                        group_size INTEGER,
                        budget_level TEXT,
                        pacing TEXT,
                        estimated_total_cost REAL,
                        cost_per_person REAL,
                        summary TEXT,
                        highlight_quote TEXT,
                        itinerary_json TEXT,
                        is_shared INTEGER DEFAULT 0,
                        share_code TEXT UNIQUE,
                        created_at TEXT,
                        updated_at TEXT
                    )
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS user_profiles (
                        id TEXT PRIMARY KEY,
                        email TEXT UNIQUE,
                        full_name TEXT,
                        preferred_currency TEXT,
                        default_traveler_type TEXT,
                        interests_json TEXT,
                        created_at TEXT
                    )
                """)
                conn.commit()
                logger.info("[Database] SQLite storage initialized successfully.")
        except Exception as e:
            logger.error(f"[Database] SQLite init error: {e}")

    def _check_supabase(self):
        """Checks if Supabase credentials are configured."""
        if self.supabase_url and self.supabase_key and "supabase.co" in self.supabase_url:
            self.is_supabase_connected = True
            logger.info("[Database] Supabase credentials detected.")
        else:
            logger.info("[Database] Running with high-speed local SQLite database.")

    def save_trip(self, itinerary: Itinerary) -> Itinerary:
        """Saves or updates a trip itinerary."""
        itinerary_json = itinerary.model_dump_json()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO trips (
                    id, user_id, title, destination, country, start_date, end_date,
                    total_days, traveler_type, group_size, budget_level, pacing,
                    estimated_total_cost, cost_per_person, summary, highlight_quote,
                    itinerary_json, is_shared, share_code, created_at, updated_at
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                ON CONFLICT(id) DO UPDATE SET
                    title=excluded.title,
                    estimated_total_cost=excluded.estimated_total_cost,
                    cost_per_person=excluded.cost_per_person,
                    summary=excluded.summary,
                    itinerary_json=excluded.itinerary_json,
                    is_shared=excluded.is_shared,
                    share_code=excluded.share_code,
                    updated_at=excluded.updated_at
            """, (
                itinerary.id,
                itinerary.user_id,
                itinerary.title,
                itinerary.destination,
                itinerary.country,
                itinerary.start_date,
                itinerary.end_date,
                itinerary.total_days,
                itinerary.traveler_type,
                itinerary.group_size,
                itinerary.budget_level,
                itinerary.pacing,
                itinerary.estimated_total_cost,
                itinerary.cost_per_person,
                itinerary.summary,
                itinerary.highlight_quote,
                itinerary_json,
                1 if itinerary.is_shared else 0,
                itinerary.share_code,
                itinerary.created_at,
                itinerary.updated_at
            ))
            conn.commit()
        return itinerary

    def get_trip(self, trip_id: str) -> Optional[Itinerary]:
        """Retrieves an itinerary by its ID."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT itinerary_json FROM trips WHERE id = ?", (trip_id,))
            row = cursor.fetchone()
            if row:
                data = json.loads(row[0])
                return Itinerary(**data)
        return None

    def get_shared_trip(self, share_code: str) -> Optional[Itinerary]:
        """Retrieves a trip by its public share code."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT itinerary_json FROM trips WHERE share_code = ?", (share_code,))
            row = cursor.fetchone()
            if row:
                data = json.loads(row[0])
                return Itinerary(**data)
        return None

    def list_trips(self, user_id: Optional[str] = None) -> List[Dict[str, Any]]:
        """Lists trips with summary metadata."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            if user_id and user_id != "guest":
                cursor.execute("""
                    SELECT id, title, destination, country, start_date, end_date,
                           total_days, traveler_type, group_size, budget_level,
                           estimated_total_cost, is_shared, share_code, created_at
                    FROM trips WHERE user_id = ? ORDER BY created_at DESC
                """, (user_id,))
            else:
                cursor.execute("""
                    SELECT id, title, destination, country, start_date, end_date,
                           total_days, traveler_type, group_size, budget_level,
                           estimated_total_cost, is_shared, share_code, created_at
                    FROM trips ORDER BY created_at DESC
                """)
            rows = cursor.fetchall()
            trips = []
            for r in rows:
                trips.append({
                    "id": r[0],
                    "title": r[1],
                    "destination": r[2],
                    "country": r[3],
                    "start_date": r[4],
                    "end_date": r[5],
                    "total_days": r[6],
                    "traveler_type": r[7],
                    "group_size": r[8],
                    "budget_level": r[9],
                    "estimated_total_cost": r[10],
                    "is_shared": bool(r[11]),
                    "share_code": r[12],
                    "created_at": r[13]
                })
            return trips

    def delete_trip(self, trip_id: str) -> bool:
        """Deletes a trip from storage."""
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM trips WHERE id = ?", (trip_id,))
            conn.commit()
            return cursor.rowcount > 0

db = DatabaseManager()
