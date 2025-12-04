# seed.py
import json
from pathlib import Path

from sqlalchemy.orm import Session

from db.db_connect import SessionLocal, Base, engine
from models.models import Campaign


def load_json():
    json_path = Path(__file__).parent / "data.json"
    if not json_path.exists():
        raise FileNotFoundError(f"data.json not found at: {json_path}")

    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)


def seed():
    db: Session = SessionLocal()

    try:
        # Check if already seeded
        Base.metadata.create_all(bind=engine)
        count = db.query(Campaign).count()
        if count > 0:
            print(f"✔️ Already seeded ({count} records)")
            return

        data = load_json()
        print(f"⚡ Seeding {len(data)} records...")

        for row in data:
            obj = Campaign(
                id=row["id"],
                name=row["name"],
                status=row["status"],
                clicks=row["clicks"],
                cost=row["cost"],
                impressions=row["impressions"],
            )
            db.add(obj)

        db.commit()
        print("✅ Seeding completed")

    except Exception as e:
        db.rollback()
        print(f"❌ Error: {e}")

    finally:
        db.close()


if __name__ == "__main__":
    seed()
