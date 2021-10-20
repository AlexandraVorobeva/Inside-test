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
    prefix="/messages",
)


@router.post("/", response_model=Message)
def post_message(
    message_data: MessageCreate,
    service: MessagesService = Depends(),
    user: User = Depends(get_current_user),
):
    """
    Create new message in database.
    :param message_data: message body
    :param service: MessagesService
    :param user: authentication
    :return: table instance
    """
    return service.create(message_data)


@router.get("/{username}/", response_model=List[Message])
def get_history_of_messages(
    username: str,
    history_of_message: str,
    service: MessagesService = Depends(),
    user: User = Depends(get_current_user),
):
    """
    Get history of messages for user.
    :param username: name of user
    :param history_of_message: count of history messages
    :param service: MessagesService
    :param user: authentication
    :return: list of messages
    """
    return service.get(username, history_of_message)
