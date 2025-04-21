from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.config.config_loader import load_config

config = load_config()
DATABASE_URL = config["database"].get("url", "sqlite:///emails.db")

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
