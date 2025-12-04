# main.py
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from contextlib import asynccontextmanager
from typing import Literal
from db.db_connect import get_db, Base, engine
from models.models import Campaign as CampaignModel
from schemas.schemas import Campaign as CampaignSchema
from sqlalchemy import text

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ----- Startup -----
    print("🚀 Application starting...")

    try:
        # create tables if not exist
        Base.metadata.create_all(bind=engine)

        # test DB connection
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        print("✅ Database connected")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")

    yield  # <-- app runs here

    # ----- Shutdown -----
    print("⚙️ Application shutting down...")
    try:
        engine.dispose()
        print("🛑 Database engine disposed (connections closed)")
    except Exception as e:
        print(f"⚠️ Error closing DB engine: {e}")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/campaigns", response_model=list[CampaignSchema])
def get_campaigns(
    status: Literal["Active", "Paused"] | None = None,
    db: Session = Depends(get_db)
):
    query = db.query(CampaignModel)

    if status:
        query = query.filter(CampaignModel.status == status)

    return query.all()
