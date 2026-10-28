"""
Curated destination knowledge base supporting intelligent itinerary synthesis,
route clustering, and offline heuristic model generation.
"""

DESTINATIONS = {
    "tokyo": {
        "name": "Tokyo",
        "country": "Japan",
        "currency": "JPY",
        "highlights": "Futuristic skyline meets ancient traditions, world-class street food, and ultra-efficient trains.",
        "transit_tip": "Get a Suica or Pasmo digital IC card for seamless metro and Yamanote Line hopping.",
        "accommodations": {
            "budget": {"name": "Nui. Hostel & Bar Lounge", "type": "Design Hostel", "neighborhood": "Kuramae", "estimated_nightly_cost": 42.0, "rating": 4.6},
            "moderate": {"name": "Hotel Gracery Shinjuku", "type": "Modern Hotel", "neighborhood": "Shinjuku", "estimated_nightly_cost": 135.0, "rating": 4.5},
            "luxury": {"name": "Hoshinoya Tokyo", "type": "Luxury Modern Ryokan", "neighborhood": "Otemachi", "estimated_nightly_cost": 480.0, "rating": 4.9}
        },
        "activities": [
            {
                "id": "tko-1",
                "title": "Senso-ji Temple & Nakamise Dori",
                "category": "culture",
                "time_slot": "morning",
                "duration_minutes": 105,
                "description": "Tokyo's oldest and most significant Buddhist temple. Stroll down Nakamise shopping street for warm melonpan and fresh matcha treats.",
                "location": "Asakusa",
                "estimated_cost": 10.0,
                "tags": ["culture", "sightseeing", "food"],
                "booking_tip": "Arrive before 9 AM for peaceful photos without the crowds."
            },
            {
                "id": "tko-2",
                "title": "Tsukiji Outer Market Tasting Tour",
                "category": "dining",
                "time_slot": "morning",
                "duration_minutes": 90,
                "description": "Sample fresh tamagoyaki (sweet rolled omelet), fatty tuna nigiri, and grilled scallop skewers straight from stall masters.",
                "location": "Chuo City",
                "estimated_cost": 25.0,
                "tags": ["food", "sightseeing"],
                "booking_tip": "Bring cash (yen) as small vendor stalls prefer coin/cash payments."
            },
            {
                "id": "tko-3",
                "title": "Meiji Jingu Shrine & Yoyogi Park Walk",
                "category": "attraction",
                "time_slot": "afternoon",
                "duration_minutes": 90,
                "description": "Enter through massive cypress torii gates into a tranquil 170-acre forested oasis in the heart of Tokyo.",
                "location": "Shibuya",
                "estimated_cost": 0.0,
                "tags": ["outdoors", "culture", "relaxation"],
                "booking_tip": "Free entry; respectful silent walking recommended."
            },
            {
                "id": "tko-4",
                "title": "Shibuya Sky Observation Deck",
                "category": "attraction",
                "time_slot": "afternoon",
                "duration_minutes": 75,
                "description": "A 360-degree open-air rooftop observation deck 229 meters above the iconic Shibuya Scramble crossing.",
                "location": "Shibuya Scramble Square",
                "estimated_cost": 22.0,
                "tags": ["sightseeing", "scenic", "photography"],
                "booking_tip": "Book timed-entry sunset tickets 4 weeks in advance."
            },
            {
                "id": "tko-5",
                "title": "Omoide Yokocho (Memory Lane) Yakitori Dinner",
                "category": "dining",
                "time_slot": "evening",
                "duration_minutes": 80,
                "description": "Atmospheric post-war alleyway lined with tiny 6-seater izakayas serving charcoal-grilled chicken skewers and cold draft beer.",
                "location": "Shinjuku",
                "estimated_cost": 28.0,
                "tags": ["food", "nightlife", "culture"],
                "booking_tip": "Look for stools opening up; seats rotate fast."
            },
            {
                "id": "tko-6",
                "title": "teamLab Planets Immersive Digital Art",
                "category": "culture",
                "time_slot": "morning",
                "duration_minutes": 120,
                "description": "Wade barefoot through water and interact with mesmerizing crystalline light projections in this world-renowned exhibition.",
                "location": "Toyosu",
                "estimated_cost": 36.0,
                "tags": ["culture", "photography", "technology"],
                "booking_tip": "Wear pants that easily roll above the knees."
            },
            {
                "id": "tko-7",
                "title": "Akihabara Electric Town & Retro Gaming",
                "category": "attraction",
                "time_slot": "afternoon",
                "duration_minutes": 90,
                "description": "Explore multi-level arcades at Super Potato, retro game emporiums, and specialty tech hardware shops.",
                "location": "Akihabara",
                "estimated_cost": 15.0,
                "tags": ["sightseeing", "technology", "pop-culture"],
                "booking_tip": "Exchange a few 100-yen coins for classic crane games."
            },
            {
                "id": "tko-8",
                "title": "Ginza Fine Dining & Craft Cocktail Bar",
                "category": "dining",
                "time_slot": "evening",
                "duration_minutes": 110,
                "description": "Experience hand-carved ice cubes, custom bespoke cocktail omakase, and refined seasonal kaiseki dishes.",
                "location": "Ginza",
                "estimated_cost": 95.0,
                "tags": ["food", "luxury", "romantic"],
                "booking_tip": "Smart-casual dress code strictly observed."
            }
        ]
    },
    "paris": {
        "name": "Paris",
        "country": "France",
        "currency": "EUR",
        "highlights": "Haussmannian boulevards, world-leading art galleries, riverbank promenades, and timeless culinary culture.",
        "transit_tip": "Use the Navigo Easy pass on the RATP Metro for smooth transfers across all central zones.",
        "accommodations": {
            "budget": {"name": "The People - Paris Marais", "type": "Boutique Hostel", "neighborhood": "4th Arrondissement", "estimated_nightly_cost": 50.0, "rating": 4.5},
            "moderate": {"name": "Hôtel Caron de Beaumarchais", "type": "Charming 3-Star", "neighborhood": "Le Marais", "estimated_nightly_cost": 175.0, "rating": 4.7},
            "luxury": {"name": "Le Meurice", "type": "Historic Palace Hotel", "neighborhood": "1st Arrondissement", "estimated_nightly_cost": 650.0, "rating": 4.9}
        },
        "activities": [
            {
                "id": "prs-1",
                "title": "Croissant & Coffee at a Classic Marais Café",
                "category": "dining",
                "time_slot": "morning",
                "duration_minutes": 60,
                "description": "Sit on wicker terrace chairs facing the cobblestone lane, sipping café au lait alongside warm flaky pain au chocolat.",
                "location": "Place des Vosges, Le Marais",
                "estimated_cost": 8.0,
                "tags": ["food", "relaxation"],
                "booking_tip": "Terrace seating fills early on sunny mornings."
            },
            {
                "id": "prs-2",
                "title": "Musée d'Orsay Impressionist Masterpieces",
                "category": "culture",
                "time_slot": "morning",
                "duration_minutes": 130,
                "description": "Housed inside a magnificent Beaux-Arts railway terminal, admire iconic works by Monet, Van Gogh, Degas, and Cézanne.",
                "location": "7th Arrondissement",
                "estimated_cost": 18.0,
                "tags": ["culture", "sightseeing"],
                "booking_tip": "Book timed entry to skip the general queue."
            },
            {
                "id": "prs-3",
                "title": "Jardin du Luxembourg & Latin Quarter Stroll",
                "category": "outdoors",
                "time_slot": "afternoon",
                "duration_minutes": 90,
                "description": "Pull up a green metal chair near the Medici Fountain, watch miniature wooden sailboats, and wander nearby bohemian bookshops.",
                "location": "6th Arrondissement",
                "estimated_cost": 0.0,
                "tags": ["outdoors", "relaxation", "scenic"],
                "booking_tip": "Pick up macarons at nearby Pierre Hermé on Rue Bonaparte."
            },
            {
                "id": "prs-4",
                "title": "Seine Sunset Cruise by Bateaux Parisiens",
                "category": "attraction",
                "time_slot": "afternoon",
                "duration_minutes": 75,
                "description": "Glide under Pont Neuf and past illuminated riverside monuments as dusk settles over Notre-Dame Cathedral.",
                "location": "Port de la Bourdonnais",
                "estimated_cost": 20.0,
                "tags": ["sightseeing", "romantic", "scenic"],
                "booking_tip": "Depart 30 minutes before official twilight for sunset glow."
            },
            {
                "id": "prs-5",
                "title": "Traditional Bistro Dinner & Wine Tasting",
                "category": "dining",
                "time_slot": "evening",
                "duration_minutes": 105,
                "description": "Savor duck confit, beef bourguignon, and crêpes Suzette paired with a velvety Côte du Rhône in a candlelit vaulted bistro.",
                "location": "Saint-Germain-des-Prés",
                "estimated_cost": 45.0,
                "tags": ["food", "romantic", "culture"],
                "booking_tip": "Reservations required at least 2 days prior."
            },
            {
                "id": "prs-6",
                "title": "Montmartre & Sacré-Cœur Panoramas",
                "category": "attraction",
                "time_slot": "morning",
                "duration_minutes": 110,
                "description": "Wander the winding vineyard lanes of Montmartre, explore Place du Tertre artists, and look over the rooftops of Paris from the basilica steps.",
                "location": "18th Arrondissement",
                "estimated_cost": 0.0,
                "tags": ["sightseeing", "scenic", "culture"],
                "booking_tip": "Take the Funiculaire de Montmartre if avoiding steep stairs."
            }
        ]
    },
    "florence": {
        "name": "Florence",
        "country": "Italy",
        "currency": "EUR",
        "highlights": "Cradle of the Renaissance, magnificent marble cathedrals, Tuscan trattorias, and breathtaking hilltop sunsets.",
        "transit_tip": "Florence is remarkably walkable; historical center is almost entirely pedestrian-only.",
        "accommodations": {
            "budget": {"name": "Ostello Bello Firenze", "type": "Social Hostel", "neighborhood": "San Lorenzo", "estimated_nightly_cost": 45.0, "rating": 4.7},
            "moderate": {"name": "Palazzo Guadagni", "type": "Historic Boutique Hotel", "neighborhood": "Santo Spirito", "estimated_nightly_cost": 160.0, "rating": 4.8},
            "luxury": {"name": "Four Seasons Hotel Firenze", "type": "Palatial Resort", "neighborhood": "San Marco", "estimated_nightly_cost": 620.0, "rating": 4.9}
        },
        "activities": [
            {
                "id": "flr-1",
                "title": "Duomo & Brunelleschi's Dome Ascent",
                "category": "culture",
                "time_slot": "morning",
                "duration_minutes": 120,
                "description": "Climb 463 historic stone steps inside the dual-shell dome to look out over the terracotta roofs of Tuscany.",
                "location": "Piazza del Duomo",
                "estimated_cost": 30.0,
                "tags": ["culture", "sightseeing", "scenic"],
                "booking_tip": "Mandatory Brunelleschi Pass reservation required weeks ahead."
            },
            {
                "id": "flr-2",
                "title": "Uffizi Gallery Masterpieces Tour",
                "category": "culture",
                "time_slot": "afternoon",
                "duration_minutes": 130,
                "description": "Behold Botticelli's 'The Birth of Venus', Michelangelo's works, and Da Vinci's Annunciation in the Medici palace halls.",
                "location": "Piazzale degli Uffizi",
                "estimated_cost": 26.0,
                "tags": ["culture", "sightseeing"],
                "booking_tip": "Afternoon slots around 2:30 PM have shorter security queues."
            },
            {
                "id": "flr-3",
                "title": "Piazzale Michelangelo Sunset & Chianti Aperitivo",
                "category": "attraction",
                "time_slot": "evening",
                "duration_minutes": 90,
                "description": "Watch the golden sun sink behind the Ponte Vecchio with street musicians playing acoustic melodies on the terrace steps.",
                "location": "Oltrarno Ridge",
                "estimated_cost": 15.0,
                "tags": ["scenic", "romantic", "relaxation"],
                "booking_tip": "Grab a chilled bottle of Prosecco and glasses from a local enoteca beforehand."
            },
            {
                "id": "flr-4",
                "title": "Osteria Dinner: Bistecca alla Fiorentina & Truffle Pasta",
                "category": "dining",
                "time_slot": "night",
                "duration_minutes": 110,
                "description": "Savor thick oak-grilled Chianina steak seasoned with coarse sea salt and rosemary, followed by cantucci dipped in Vin Santo.",
                "location": "San Frediano / Santo Spirito",
                "estimated_cost": 55.0,
                "tags": ["food", "romantic", "culture"],
                "booking_tip": "Order steak cooked 'al sangue' (rare) as Florentine tradition dictates."
            }
        ]
    },
    "barcelona": {
        "name": "Barcelona",
        "country": "Spain",
        "currency": "EUR",
        "highlights": "Gaudí's fantastical architecture, sun-drenched Mediterranean beaches, vibrant tapas crawls, and spirited nightlife.",
        "transit_tip": "The T-Casual card covers 10 trips across metro, buses, and urban rail.",
        "accommodations": {
            "budget": {"name": "Generator Barcelona", "type": "Modern Hostel", "neighborhood": "Gràcia", "estimated_nightly_cost": 38.0, "rating": 4.4},
            "moderate": {"name": "Yurbban Passage Hotel & Spa", "type": "Design Hotel", "neighborhood": "El Born", "estimated_nightly_cost": 150.0, "rating": 4.8},
            "luxury": {"name": "Hotel Arts Barcelona", "type": "Waterfront Luxury", "neighborhood": "Port Olímpic", "estimated_nightly_cost": 420.0, "rating": 4.7}
        },
        "activities": [
            {
                "id": "bcn-1",
                "title": "Basílica de la Sagrada Família Guided Visit",
                "category": "culture",
                "time_slot": "morning",
                "duration_minutes": 110,
                "description": "Stand beneath the forest-like stone columns bathed in prismatic stained-glass light inside Gaudí’s ongoing masterpiece.",
                "location": "Eixample",
                "estimated_cost": 32.0,
                "tags": ["culture", "sightseeing", "scenic"],
                "booking_tip": "Book the Nativity Tower audio guide ticket for panoramic skyline views."
            },
            {
                "id": "bcn-2",
                "title": "Park Güell Surreal Mosaic Terraces",
                "category": "outdoors",
                "time_slot": "afternoon",
                "duration_minutes": 90,
                "description": "Admire the undulating serpentine mosaic bench and the whimsical gingerbread-style porter lodges overlooking the city.",
                "location": "Carmel Hill, Gràcia",
                "estimated_cost": 13.0,
                "tags": ["outdoors", "sightseeing", "scenic"],
                "booking_tip": "Enter from Carretera del Carmel to minimize uphill walking."
            },
            {
                "id": "bcn-3",
                "title": "El Born & Gothic Quarter Tapas Crawl",
                "category": "dining",
                "time_slot": "evening",
                "duration_minutes": 120,
                "description": "Bar hop through centuries-old alleyways tasting crispy patatas bravas, Iberian bellota ham, pimientos de Padrón, and vermut.",
                "location": "El Born",
                "estimated_cost": 35.0,
                "tags": ["food", "nightlife", "group-friendly"],
                "booking_tip": "Start at Bar del Pla or El Xampanyet around 8:00 PM."
            },
            {
                "id": "bcn-4",
                "title": "Barceloneta Beachfront Sunset & Sangria",
                "category": "relaxation",
                "time_slot": "afternoon",
                "duration_minutes": 90,
                "description": "Relax on the sand, dip into the Mediterranean, or sit at an outdoor chiringuito enjoying chilled white sangria.",
                "location": "Barceloneta",
                "estimated_cost": 12.0,
                "tags": ["relaxation", "outdoors", "group-friendly"],
                "booking_tip": "Rent beach volleyball equipment right on the boardwalk."
            }
        ]
    },
    "banff": {
        "name": "Banff & Canadian Rockies",
        "country": "Canada",
        "currency": "CAD",
        "highlights": "Glacial turquoise lakes, rugged granite peaks, wildlife encounters, and pristine alpine wilderness.",
        "transit_tip": "Reserve Roam Transit Super Passes or Parks Canada shuttles in advance for Lake Louise & Moraine Lake.",
        "accommodations": {
            "budget": {"name": "HI Banff Alpine Centre", "type": "Alpine Hostel", "neighborhood": "Tunnel Mountain", "estimated_nightly_cost": 55.0, "rating": 4.5},
            "moderate": {"name": "Moose Hotel & Suites", "type": "Mountain Lodge", "neighborhood": "Banff Town Centre", "estimated_nightly_cost": 190.0, "rating": 4.7},
            "luxury": {"name": "Fairmont Banff Springs", "type": "Historic Castle Resort", "neighborhood": "Spray Valley", "estimated_nightly_cost": 550.0, "rating": 4.8}
        },
        "activities": [
            {
                "id": "bnf-1",
                "title": "Sunrise at Lake Moraine & Rockpile Trail",
                "category": "outdoors",
                "time_slot": "morning",
                "duration_minutes": 120,
                "description": "Watch early morning alpenglow illuminate the Valley of the Ten Peaks reflected in luminous teal waters.",
                "location": "Moraine Lake",
                "estimated_cost": 18.0,
                "tags": ["outdoors", "scenic", "photography"],
                "booking_tip": "Commercial Parks Canada shuttle booking opens 48 hours prior."
            },
            {
                "id": "bnf-2",
                "title": "Lake Louise Canoe Rental & Plain of Six Glaciers Hike",
                "category": "outdoors",
                "time_slot": "afternoon",
                "duration_minutes": 180,
                "description": "Paddle across Lake Louise then hike through larch forests up to the rustic alpine tea house overlooking hanging glaciers.",
                "location": "Lake Louise",
                "estimated_cost": 65.0,
                "tags": ["adventure", "outdoors", "hiking"],
                "booking_tip": "Bring cash for the backcountry tea house (no card machines)."
            },
            {
                "id": "bnf-3",
                "title": "Banff Upper Hot Springs Soak",
                "category": "relaxation",
                "time_slot": "evening",
                "duration_minutes": 75,
                "description": "Soothe sore muscles in natural thermal mineral pools with panoramic views of Mount Rundle.",
                "location": "Sulphur Mountain",
                "estimated_cost": 16.0,
                "tags": ["relaxation", "scenic"],
                "booking_tip": "First-come, first-served; evening soak right after hiking is magical."
            },
            {
                "id": "bnf-4",
                "title": "Wild Game & Craft Beer Group Feast at The Bison",
                "category": "dining",
                "time_slot": "night",
                "duration_minutes": 105,
                "description": "Farm-to-table dining with Alberta bison ribeye, wood-fired seasonal vegetables, and locally brewed IPA.",
                "location": "Bear Street, Banff Town",
                "estimated_cost": 50.0,
                "tags": ["food", "group-friendly"],
                "booking_tip": "Make group reservations for 4+ at least 1 week early."
            }
        ]
    }
}

DEFAULT_FALLBACK_DESTINATION = {
    "name": "Global Destination",
    "country": "International",
    "currency": "USD",
    "highlights": "Dynamic destination rich in culture, scenic vistas, and culinary delights.",
    "transit_tip": "Check local transit apps or hire trusted local rideshare for efficient travel.",
    "accommodations": {
        "budget": {"name": "Central Traveler's Lodge", "type": "Hostel / Guesthouse", "neighborhood": "City Center", "estimated_nightly_cost": 40.0, "rating": 4.4},
        "moderate": {"name": "Grand Boutique Hotel", "type": "Boutique Hotel", "neighborhood": "Cultural Quarter", "estimated_nightly_cost": 140.0, "rating": 4.6},
        "luxury": {"name": "The Heritage Palace Resort", "type": "5-Star Luxury", "neighborhood": "Scenic Waterfront", "estimated_nightly_cost": 420.0, "rating": 4.9}
    },
    "activities": [
        {
            "id": "gen-1",
            "title": "Historic Old Town & Market Exploration",
            "category": "culture",
            "time_slot": "morning",
            "duration_minutes": 110,
            "description": "Immerse yourself in centuries of history, local artisan stalls, and fragrant coffee shops.",
            "location": "Old Town Core",
            "estimated_cost": 12.0,
            "tags": ["culture", "sightseeing", "food"],
            "booking_tip": "Wear comfortable walking shoes for cobblestone streets."
        },
        {
            "id": "gen-2",
            "title": "Signature Regional Culinary Lunch Experience",
            "category": "dining",
            "time_slot": "afternoon",
            "duration_minutes": 75,
            "description": "Taste authentic delicacies, farm-fresh appetizers, and iconic regional specialties.",
            "location": "Market District",
            "estimated_cost": 22.0,
            "tags": ["food", "culture"],
            "booking_tip": "Ask your server for the chef's seasonal recommendation."
        },
        {
            "id": "gen-3",
            "title": "Panoramic City Viewpoint & Botanical Gardens",
            "category": "attraction",
            "time_slot": "afternoon",
            "duration_minutes": 90,
            "description": "Ascend to the highest accessible ridge or tower for sprawling skyline panoramas.",
            "location": "Hilltop Promenade",
            "estimated_cost": 10.0,
            "tags": ["scenic", "photography", "outdoors"],
            "booking_tip": "Perfect lighting for photography 1-2 hours before sunset."
        },
        {
            "id": "gen-4",
            "title": "Evening Ambient Dining & Local Entertainment",
            "category": "dining",
            "time_slot": "evening",
            "duration_minutes": 100,
            "description": "Candlelit dinner featuring local ingredients, ambient acoustic music, and curated regional drinks.",
            "location": "Riverfront / Historic District",
            "estimated_cost": 38.0,
            "tags": ["dining", "relaxation", "nightlife"],
            "booking_tip": "Book evening seating in advance."
        }
    ]
}
