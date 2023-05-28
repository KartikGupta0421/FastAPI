from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import csv 
from app.models.models import USVideo
from app.static import Constants




SQLALCHEMY_DATABASE_URL = "sqlite:///./database.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def create_tables():
    from app.models.models import Base
    Base.metadata.create_all(bind=engine)


def load_csv_data():
    session = SessionLocal()

    with open(Constants.CSV_File_PATH, "r") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            video = USVideo(
                title=row['title'],
                channel_title=row['channel_title'],
                category_id=row['category_id'],
                views=row['views'],
                likes=row['likes'],
                dislikes=row['dislikes'],
                comment_count=row['comment_count'],
                comments_disabled=row['comments_disabled'],
                ratings_disabled=row['ratings_disabled'],
                video_error_or_removed=row['video_error_or_removed'],
            )
            session.add(video)

    session.commit()
    session.close()
