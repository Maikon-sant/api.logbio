from app.database import engine, Base
# Import models to register them with Base.metadata for table creation
from app.models import Ship, Logbook  # noqa: F401

def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_db()
