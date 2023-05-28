from sqlalchemy import Column, Integer, String, Index
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel, validator

Base = declarative_base()

class USVideo(BaseModel):
    
    title : str
    channel_title : str
    category_id : int
    views : int
    likes : int
    dislikes : int
    comment_count = int
    comments_disabled : str
    ratings_disabled : str
    video_error_or_removed : str
    
    class Config:
        orm_mode = True

class USVideo(Base):
    __tablename__ = "USvideos"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    channel_title = Column(String)
    category_id = Column(Integer)
    views = Column(Integer)
    likes = Column(Integer)
    dislikes = Column(Integer)
    comment_count = Column(Integer)
    comments_disabled = Column(String)
    ratings_disabled = Column(String)
    video_error_or_removed = Column(String)


# Create the index
#index = Index('idx_integer_channel', USVideo.views, USVideo.likes, USVideo.dislikes, USVideo.comment_count)

