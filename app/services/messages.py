from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models.messages import MessageCreate
from .. import tables
from typing import List


class MessagesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get(self, username: str, history_of_message: str) -> List[tables.Message]:
        """
        Get history of messages for user.
        :param username: name of user
        :param history_of_message: count of history messages
        :return: list of messages
        """
        if history_of_message.split()[0] == "history":
            count = history_of_message.split()[1]
            messages = self.session.query(tables.Message).filter(
                tables.Message.username == username
            )
            mes = messages[:count]
            if not mes:
                raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
            return mes
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='History of mrssages must be like "history 10"',
        )

    def create(self, massage_data: MessageCreate) -> tables.Message:
        """
        Create new message in database.
        :param massage_data: message body
        :return: table instance
        """
        messages = tables.Message(**massage_data.dict())
        self.session.add(messages)
        self.session.commit()
        return messages
