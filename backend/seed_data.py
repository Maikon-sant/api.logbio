from app.database import SessionLocal, Base, engine
from app.models.ship import Ship

Base.metadata.create_all(bind=engine)

ships_seed = [
    {"name": "Atlântico I", "type": "Bulk Carrier", "last_cleaning_date": None, "coating_type": "Ablative"},
    {"name": "Pacífico II", "type": "Tanker", "last_cleaning_date": None, "coating_type": "Silicone"},
    {"name": "Índico III", "type": "Container", "last_cleaning_date": None, "coating_type": "Epoxy"},
]

def main():
    db = SessionLocal()
    try:
        count = db.query(Ship).count()
        if count == 0:
            for s in ships_seed:
                db.add(Ship(**s))
            db.commit()
            print("Seed inserido.")
        else:
            print("Ships já existem, nada a fazer.")
    finally:
        db.close()

if __name__ == "__main__":
    main()
