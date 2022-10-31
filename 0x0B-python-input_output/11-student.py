#!/usr/bin/python3
"""
    This module contains a class Student
"""


class Student:
    """A class representation of a student"""

    def __init__(self, first_name, last_name, age) -> None:
        """Initialize an instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dict representation of the class"""
        my_dict = dict({})
        if not attrs:
            return self.__dict__

        if type(attrs) == list:
            for att in attrs:
                if att in self.__dict__:
                    my_dict[att] = self.__dict__.get(att)
            return my_dict

    def reload_from_json(self, json):
        """realods from json"""
        for key, value in json.items():
            self.__dict__[key] = value
