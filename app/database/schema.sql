-- Supabase / PostgreSQL Database Schema for Personalized Travel Itinerary Planner
-- Run this in your Supabase SQL Editor

-- 1. Enable UUID Extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 2. User Profiles Table
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID REFERENCES auth.users(id) ON DELETE CASCADE PRIMARY KEY,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    preferred_currency TEXT DEFAULT 'USD',
    default_traveler_type TEXT DEFAULT 'solo',
    interests TEXT[] DEFAULT ARRAY['sightseeing', 'food'],
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 3. Trips & Itineraries Table
CREATE TABLE IF NOT EXISTS public.trips (
    id TEXT PRIMARY KEY,
    user_id TEXT NOT NULL,
    title TEXT NOT NULL,
    destination TEXT NOT NULL,
    country TEXT,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    total_days INT NOT NULL,
    traveler_type TEXT NOT NULL,
    group_size INT DEFAULT 1,
    budget_level TEXT NOT NULL,
    pacing TEXT DEFAULT 'balanced',
    estimated_total_cost NUMERIC(10, 2) NOT NULL,
    cost_per_person NUMERIC(10, 2) NOT NULL,
    summary TEXT,
    highlight_quote TEXT,
    itinerary_data JSONB NOT NULL,
    is_shared BOOLEAN DEFAULT FALSE,
    share_code TEXT UNIQUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT timezone('utc'::text, now()) NOT NULL
);

-- 4. Enable Row Level Security (RLS)
ALTER TABLE public.profiles ENABLE ROW LEVEL SECURITY;
ALTER TABLE public.trips ENABLE ROW LEVEL SECURITY;

-- 5. Row Level Security Policies
-- Profiles: Users can view and update their own profile
CREATE POLICY "Users can read own profile" 
ON public.profiles FOR SELECT 
USING (auth.uid() = id);

CREATE POLICY "Users can update own profile" 
ON public.profiles FOR UPDATE 
USING (auth.uid() = id);

-- Trips: Users can manage their own trips, or view publicly shared trips
CREATE POLICY "Users can manage their own trips" 
ON public.trips FOR ALL 
USING (auth.uid()::text = user_id OR user_id = 'guest');

CREATE POLICY "Anyone can view shared trips" 
ON public.trips FOR SELECT 
USING (is_shared = true);

-- 6. Indexes for Performance
CREATE INDEX IF NOT EXISTS idx_trips_user_id ON public.trips(user_id);
CREATE INDEX IF NOT EXISTS idx_trips_destination ON public.trips(destination);
CREATE INDEX IF NOT EXISTS idx_trips_share_code ON public.trips(share_code);
