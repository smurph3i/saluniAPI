import os
from sqlalchemy import create_engine
from app.db.base_class import Base
from app.core.config import settings
from app import models  # Ensure models are registered

# Force TESTING mode
os.environ["TESTING"] = "1"

# Create DB engine
engine = create_engine(settings.actual_database_url)

print("Creating tables in:", settings.actual_database_url)
print("Tables in metadata:", Base.metadata.tables.keys())

# Drop + recreate tables
Base.metadata.drop_all(bind=engine)
Base.metadata.create_all(bind=engine)

print("✅ Tables created.")
