#!/usr/bin/python3
import json
from os.path import isfile


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets obj in __objects with key <obj class name>.id."""
        key = f"{obj.__class__.____name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (__file_path)."""
        data = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def reload(self):
        """Deserializes the JSON file to __objects \
        if the file (__file_path) exists; otherwise, do nothing."""
        if isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split(".")
                    self.__objects[key] = globals()[class_name](**value)


storage = FileStorage()
