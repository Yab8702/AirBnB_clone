#!/usr/bin/python3
"""base model modules"""

import uuid
from datetime import datetime
from models.engine.file_storage import storage


class BaseModel:
    """BaseModel class serves as the base class for other classes and
    defines common attributes and methods"""

    def __init__(self, *args, **kwargs):
        """Initializes a new instance of the BaseModel class.

        Args:
        - **kwargs: A dictionary of attribute names.

        If kwargs is not empty:
        - Each key in kwargs is treated as an attribute name.
        - Each value in kwargs is assigned as the value of\
        the corresponding attribute.
        - 'created_at' and 'updated_at' strings in \
        kwargs are converted to datetime objects.

        If kwargs is empty:
        - A new instance is created with a unique identifier and\
        current datetime.
        """

        if kwargs is not None and kwargs != {}:
            for key in kwargs:
                if key == "created_at":
                    self.__dict__["created_at"] = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.__dict__["updated_at"] = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returns a string representation of the object.
        Format: [<class name>] (<self.id>) <self.__dict__> """

        return "[{}] ({}) {}".\
            format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """Updates the 'updated_at' attribute with the current datetime."""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary representation \
        of the object for serialization"""

        dict_obj = self.__dict__.copy()
        dict_obj['__class__'] = self.__class__.__name
        dict_obj['created_at'] = self.created_at.isoformat()
        dict_obj['updated_at'] = self.updated_at.isoformat()
        return dict_obj
