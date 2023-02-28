from fastapi import APIRouter, HTTPException, Path, status
from fastapi import Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from fastapi.responses import JSONResponse
from schemas import TweetSchema, Request, Response, RequestTweet
from fastapi.encoders import jsonable_encoder

import crud

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create")
async def create_tweet_service(request: RequestTweet, db: Session = Depends(get_db)):
    print("request:",request)
    newtweet = crud.create_tweet(db, tweet = request)
    newtweetJson = jsonable_encoder(newtweet)
    print("newtweet:",newtweet)
    return JSONResponse(status_code = status.HTTP_201_CREATED, content=newtweetJson)

@router.get("/")
async def get_tweets(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    alltweets = crud.get_tweets(db, skip, limit)
    return alltweets

@router.get("/{id}")
async def get_tweet_by_id(id, db: Session = Depends(get_db)):
    thistweet = crud.get_tweet_by_id(db, id)
    return thistweet

@router.patch("/update/{id}")
async def update_tweet(id, request: RequestTweet, db: Session = Depends(get_db)):
    updtweet = crud.update_tweet(db, tweet_id=id,
                             title=request.title, desc=request.desc)
    updtweetJson = jsonable_encoder(updtweet)
    return JSONResponse(status_code = status.HTTP_201_CREATED, content=updtweetJson)

@router.delete("/delete/{id}")
async def delete_tweet(id, db: Session = Depends(get_db)):
    crud.remove_tweet(db, tweet_id=id)
    return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"message": "Tweet has been deleted successfully."})
