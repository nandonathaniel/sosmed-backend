from sqlalchemy.orm import Session
from model import Tweet
import datetime
from schemas import TweetSchema

def get_tweets(db:Session, skip:int = 0, limit:int = 100):
    return db.query(Tweet).order_by(Tweet.id).offset(skip).limit(limit).all()

def get_tweet_by_id(db: Session, tweet_id: int):
    print("oposeh")
    return db.query(Tweet).filter(Tweet.id == tweet_id).first()

def create_tweet(db: Session, tweet: TweetSchema):
    
    dateNow = datetime.datetime.now()
    # id = max(i[0] for i in get_tweets(db, 0, 100)) + 1
    print("dateNow:",dateNow)
    
    thistweet = Tweet(title=tweet.title, desc=tweet.desc, date=dateNow)
    db.add(thistweet)
    db.commit()
    db.refresh(thistweet)
    return thistweet

def remove_tweet(db:Session, tweet_id:int):
    print("brp", tweet_id)
    foundtweet = get_tweet_by_id(db=db, tweet_id=tweet_id)
    db.delete(foundtweet)
    db.commit()

def update_tweet(db:Session, tweet_id: int, title: str, desc: str):
    thisbook = get_tweet_by_id(db=db, tweet_id=tweet_id)
    thisbook.title = title
    thisbook.desc = desc
    thisbook.date = datetime.datetime.now()
    db.commit()
    db.refresh(thisbook)
    return thisbook


