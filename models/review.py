#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """  Review Class for the project """
    place_id = ""
    user_id = ""
    text = ""
