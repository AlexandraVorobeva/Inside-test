from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session
from ..database import get_session
from ..models.messages import MessageCreate
from .. import tables
from typing import List


class MessagesService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def get_list(self) -> List[tables.Message]:
        messages = (self.session.query(tables.Message).all())
        return messages

# Доделать возврат 10
    def get(self, username) -> tables.Message:
        messages = (self.session
                    .query(tables.Message)
                    .filter(tables.Message.username == username).first()
                    )
        if not messages:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
        return messages


    def create(self, massage_data: MessageCreate) -> tables.Message:
        messages = tables.Message(**massage_data.dict())
        self.session.add(messages)
        self.session.commit()
        return messages
