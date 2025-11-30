from app.database import SessionLocal
from app.models.ship import Ship

def seed_db():
    db = SessionLocal()
    try:
        # Check if ship exists
        ship = db.query(Ship).filter(Ship.imo == "1234567").first()
        if not ship:
            print("Creating test ship...")
            ship = Ship(name="Test Ship", imo="1234567")
            db.add(ship)
            db.commit()
            print(f"Ship created with ID: {ship.id}")
        else:
            print(f"Ship already exists with ID: {ship.id}")
    finally:
        db.close()

if __name__ == "__main__":
    seed_db()
