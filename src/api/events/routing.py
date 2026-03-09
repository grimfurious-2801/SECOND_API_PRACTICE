import os
from dotenv import load_dotenv
from fastapi import APIRouter
from .models import (
    EventModel,
    EventListSchema,
    EventCreateSchema,
    EventUpdateSchema
    )




router = APIRouter()

from api.db.config import DATABASE_URL

@router.get("/")
def read_events() -> EventListSchema:
    print(os.environ.get("DATABASE_URL"), DATABASE_URL)
    return{
        "results":[
             {"id": 1}, {"id": 2}, {"id": 3}
         ],
        "count":3
    }



@router.post("/")
def create_event(payload:EventCreateSchema) -> EventModel:
    data = payload.model_dump()
    return{"id":123, **data}



@router.get("/{event_id}")
def get_event(event_id:int) -> EventModel:
     return{"id": event_id}



@router.put("/{event_id}")
def update_event(event_id:int, payload:EventUpdateSchema) -> EventModel:
     data = payload.model_dump()
     return{"id": event_id, **data}