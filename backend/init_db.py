from app.database import engine, Base
# Models must be imported to register them with Base before create_all()

from app.models import Ship, Logbook  # noqa: F401

def init_db():
    print("Criando tabelas no banco de dados...")
    Base.metadata.create_all(bind=engine)
    print("Tabelas criadas com sucesso!")

if __name__ == "__main__":
    init_db()
