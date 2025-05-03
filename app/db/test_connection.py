from sqlalchemy import text
from app.db.session import engine


def test_db_connection():
    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connection successful.")
    except Exception as e:
        print("❌ Database connection failed:", e)


if __name__ == "__main__":
    test_db_connection()
