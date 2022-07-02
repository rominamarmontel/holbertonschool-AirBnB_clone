#!/usr/bin/python3
""" Unit test for FileStorage """

from multiprocessing import dummy
import unittest
import pycodestyle
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os
import json


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
        self.assertIsNotNone(test1)
        self.assertEqual(type(test1), dict)

    def test_save1(self):
        """Test method save if the type of file is dictionary"""
        storage = FileStorage()
        storage.save()
        with open("file.json", "r", encoding="utf-8") as f:
            file = json.load(f)
        self.assertTrue(type(file), dict)

    def test_save2(self):
        """Test method save to verify json file exists"""
        storage = FileStorage()
        storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def reload1(self):
        """Test method reload"""
        self.assertEqual(storage.reload(), None)

    def reload2(self):
        """Test method reload"""
        jsontype = '{"__class__": "BaseModel"}'
        list = json.loads(jsontype)
        self.assertTrue(type(list) is dict)


if __name__ == '__main__':
    unittest.main()
