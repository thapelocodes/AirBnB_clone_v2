#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import shlex


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')

    @property
    def cities(self):
        """
        returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import storage
        from models.city import City

        c_list = []
        c_dict = storage.all(City)

        for city in c_dict.values():
            if city.state_id == self.id:
                c_list.append(city)
        return c_list
