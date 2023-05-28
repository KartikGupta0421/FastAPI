from fastapi import APIRouter
from app.schemas.analysisSchema import category
from app.db.database import SessionLocal
from app.models.models import USVideo
from sqlalchemy import  desc, func

router = APIRouter()

@router.get("/most_liked")
async def get_most_liked():
    session = SessionLocal()
    video = session.query(USVideo).order_by(desc(USVideo.likes)).first()
    session.close()
    return video

@router.get("/most_dislikes")
async def get_most_dislikes():
    session = SessionLocal()
    video = session.query(USVideo).order_by(desc(USVideo.dislikes)).first()
    session.close()
    return video
   
@router.get("/most_viewed")
async def get_most_viewed():
    session = SessionLocal()
    video = session.query(USVideo).order_by(desc(USVideo.views)).first()
    session.close()
    return video


class CategoryStats:
    def __init__(self, total_views: int, total_likes: int, total_dislikes: int, total_comments: int):
        self.total_views = total_views
        self.total_likes = total_likes
        self.total_dislikes = total_dislikes
        self.total_comments = total_comments


@router.post("/category_stats/")
async def stats_by_category_id(category: category):
    session = SessionLocal()

    print("category",category.category_id)
    stats = session.query(
        func.sum(USVideo.views).label("total_views"),
        func.sum(USVideo.likes).label("total_likes"),
        func.sum(USVideo.dislikes).label("total_dislikes"),
        func.sum(USVideo.comment_count).label("total_comments")
    ).filter(USVideo.category_id == int(category.category_id)).first()

    session.close()
    print(stats)

    if stats:
        category_stats = CategoryStats(
            total_views=stats.total_views or 0,
            total_likes=stats.total_likes or 0,
            total_dislikes=stats.total_dislikes or 0,
            total_comments=stats.total_comments or 0
        )
        return category_stats.__dict__
    else:
        return {}
    return stats