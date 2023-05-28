from fastapi import APIRouter
from app.db.database import SessionLocal
from app.models.models import USVideo
from app.schemas.readSchema import category, filter
from sqlalchemy import and_


router = APIRouter()

@router.get("/")
async def get_items():
    # Logic to fetch and return items
    return {"message": "Get all items"}

@router.post("/filter_by_category")
async def filter_videos_by_category(filters: category):
    session = SessionLocal()
    query = session.query(USVideo).filter(USVideo.category_id == filters.category_id)
    videos = query.all()
    session.close()
    return videos


@router.post("/filters_max_20")
async def filter_max_20(filters: filter):

    session = SessionLocal()
    query = session.query(USVideo)
    conditions = []
    print(filter)
    if filters.views is not None:
        print("view 225211923",filters.views)
        conditions.append(USVideo.views > filters.views)

    if filters.likes is not None:
        print("likes 5613827",filters.likes)
        conditions.append(USVideo.likes > filters.likes)

    if filters.dislikes is not None:
        print("dislikes 1674420 ",filters.dislikes)
        conditions.append(USVideo.dislikes > filters.dislikes)

    if conditions:
        print("conditions",conditions)
        query = query.filter(and_(*conditions))

    session.close()
    videos = query.all()

    return videos[:20]

