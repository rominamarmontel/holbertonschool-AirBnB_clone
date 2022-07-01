#!/usr/bin/python3
""" Unit test for FileStorage """

import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime


class TestFileStorage(unittest.TestCase):
    """ Test class FileStorage """

    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/engine/file_storage.py'])
        self.assertEqual(result.total_errors, 0)

    def test_all(self):
        """Test method all"""
        storage = FileStorage()
        test1 = storage.all()
        self.assertEqual(type(test1), dict)

    def test_new(self):
        """Test method new"""
        storage = FileStorage()
        test2 = storage.new()
        model = BaseModel()
        storage.new(model)





    def test_save(self):
        """Test method save"""
        storage = FileStorage()
        storage.save()

    def reload(self):
        """Test method reload"""


if __name__ == '__main__':
    unittest.main()
