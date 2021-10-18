from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..models.messages import Message, MessageCreate
from typing import List
from ..database import get_session
from .. import tables
from ..services.messages import MessagesService
from ..services.auth import get_current_user
from ..models.auth import User

router = APIRouter(
    prefix='/messages',
)


# @router.get("/", response_model=List[Message])
# def get_history_of_messages(
#         service: MessagesService = Depends(),
# ):
#     return service.get_list()


@router.post("/", response_model=Message)
def post_message(
        message_data: MessageCreate,
        service: MessagesService = Depends(),
        user: User = Depends(get_current_user),
):
    return service.create(message_data)


@router.get("/{username}/", response_model=Message)
def get_history_of_messages(
        username,
        service: MessagesService = Depends(),
        user: User = Depends(get_current_user),
):
    return service.get(username)
