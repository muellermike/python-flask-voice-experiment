# coding: utf-8

from __future__ import absolute_import

from typing import List, Dict  # noqa: F401

from models.base_model_ import Model
import util
from models.recording import Recording


class User(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, unique_id: int=None):  # noqa: E501
        """User - a model defined in Swagger

        :param id: The id of this User.  # noqa: E501
        :type id: str
        """
        self.swagger_types = {
            'id': str,
            'unique_id': int
        }

        self.attribute_map = {
            'id': 'id',
            'unique_id': 'uniqueId'
        }

        self._id = id
        self._unique_id = unique_id

    @classmethod
    def from_dict(cls, dikt) -> 'User':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The User of this User.  # noqa: E501
        :rtype: User
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> str:
        """Gets the id of this User.


        :return: The id of this User.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id: str):
        """Sets the id of this User.


        :param id: The id of this User.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def unique_id(self) -> int:
        """Gets the unique_id of this User.


        :return: The unique_id of this User.
        :rtype: int
        """
        return self._unique_id

    @id.setter
    def unique_id(self, unique_id: int):
        """Sets the unique_id of this User.


        :param id: The unique_id of this User.
        :type unique_id: int
        """

        self._unique_id = unique_id