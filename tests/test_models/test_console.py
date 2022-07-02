#!/usr/bin/python3
""" Unit test for  HBNBCommand """

import unittest
import pycodestyle
from console import HBNBCommand
from models.base_model import BaseModel
from datetime import datetime
import console


class TestHBNBCommand(unittest.TestCase):
    """ Test class HBNBCommand """
    def test_class_style(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['console.py'])
        self.assertEqual(result.total_errors, 0)

    def test_prompt(self):
        """test the prompt format"""
        self.assertEqual(HBNBCommand.prompt, "(hbnb) ")

    """def test_do_quit(self, arg):
        tests for quit
        self.assertEqual("quit()", "")"""

    """def test_do_EOF(self, arg):

    def test_emptyline(self):

    def test_do_create(self, arg):

    def test_do_show(self, arg):

    def test_do_destroy(self, arg):

    def test_do_all(self, arg):

    def test_do_update(self, arg):

    def test_do_count(self, arg):

    def test_default(self, arg):"""


if __name__ == '__main__':
    unittest.main()
