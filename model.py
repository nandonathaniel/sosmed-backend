from sqlalchemy import Column, Integer, String, Date
from config import Base

class Tweet(Base):
    __tablename__ = 'tweet'

    id = Column(Integer, primary_key = True)
    title = Column(String)
    desc = Column(String)
    date = Column(Date)