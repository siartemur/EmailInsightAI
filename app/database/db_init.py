from app.database.db_connection import engine
from app.database.email_models import Base

def init_db():
    Base.metadata.create_all(bind=engine)
    print("✅ Veritabanı başarıyla oluşturuldu.")

if __name__ == "__main__":
    init_db()
