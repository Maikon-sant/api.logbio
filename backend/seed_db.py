from app.database import SessionLocal
from app.models.ship import Ship
from app.models.logbook import Logbook
from datetime import datetime, timedelta
import random

def seed_db():
    db = SessionLocal()
    try:
        # Check if ship exists
        ship = db.query(Ship).filter(Ship.imo == "1234567").first()
        if not ship:
            print("Creating test ship...")
            ship = Ship(
                name="Transpetro Voyager", 
                imo="1234567",
                ship_class="Suezmax"
            )
            db.add(ship)
            db.commit()
            db.refresh(ship)
            print(f"Ship created with ID: {ship.id}")
        else:
            print(f"Ship already exists with ID: {ship.id}")
            
        # Create Logbooks
        if db.query(Logbook).count() == 0:
            print("Seeding logbooks...")
            base_date = datetime.now() - timedelta(days=30)
            
            events = ["Port", "Sailing", "Anchored", "Drifting"]
            ports = ["Santos", "Rio de Janeiro", "Rotterdam", "Singapore"]
            
            for i in range(20):
                start_date = base_date + timedelta(days=i)
                end_date = start_date + timedelta(hours=random.randint(4, 24))
                event = random.choice(events)
                
                logbook = Logbook(
                    ship_id=ship.id,
                    session_id=f"SES-{2023000+i}",
                    event_name=event,
                    start_date=start_date,
                    end_date=end_date,
                    duration=(end_date - start_date).total_seconds() / 3600,
                    distance=random.uniform(50, 500) if event == "Sailing" else 0,
                    aft_draft=random.uniform(10, 15),
                    fwd_draft=random.uniform(10, 15),
                    mid_draft=random.uniform(10, 15),
                    trim=random.uniform(-1, 1),
                    displacement=random.uniform(100000, 150000),
                    beaufort_scale=str(random.randint(1, 8)),
                    sea_condition=str(random.randint(1, 5)),
                    beaufort_scale_desc="Moderate Breeze",
                    sea_condition_desc="Moderate",
                    speed=random.uniform(10, 18) if event == "Sailing" else 0,
                    speed_gps=random.uniform(10, 18) if event == "Sailing" else 0,
                    port=random.choice(ports) if event == "Port" else None,
                    latitude=random.uniform(-23, 0),
                    longitude=random.uniform(-45, -30)
                )
                db.add(logbook)
            
            db.commit()
            print("Logbooks seeded.")
            
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
