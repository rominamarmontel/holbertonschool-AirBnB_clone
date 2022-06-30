#!/usr/bin/python3
""" Unittest for class BaseModel """


import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
        test for BaseModel
    """
    def test_id(self):
        """Test attribute id"""
        b1 = BaseModel()
        b2 = BaseModel(None)
        b3 = BaseModel("name")
        b4 = BaseModel(3)
        b5 = BaseModel(2.5)
        b6 = BaseModel(float('inf'))
        b7 = BaseModel([1, 2, 3])
        b8 = BaseModel({"name": "Jay", "age": 20})

        self.assertRegex(b1.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b2.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b3.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b4.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b5.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b6.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b7.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")
        self.assertRegex(b8.id,
                         "[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*-[0-9a-z]*")

    def test_created_at(self):
        """Test attribute created_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel(None)
        b4 = BaseModel(3)
        b5 = BaseModel(3.2)
        b6 = BaseModel("John")
        b7 = BaseModel(float('inf'))
        b8 = BaseModel([1, 2, 3])
        b9 = BaseModel({"name": "Jay", "age": 20})

        self.assertNotEqual(b1.created_at, b2.created_at)
        self.assertRegex(b1.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b3.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b4.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b5.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b6.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b7.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b8.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b9.created_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")

    def test_updated_at(self):
        """Test attribute updated_at"""
        b1 = BaseModel()
        b2 = BaseModel()
        b3 = BaseModel(None)
        b4 = BaseModel(3)
        b5 = BaseModel(3.2)
        b6 = BaseModel("Lucile")
        b7 = BaseModel(float('inf'))
        b8 = BaseModel([1, 2, 3])
        b9 = BaseModel({"name": "Jay", "age": 20})

        self.assertNotEqual(b1.updated_at, b2.updated_at)
        self.assertRegex(b1.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b3.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b4.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b5.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b6.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b7.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b8.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")
        self.assertRegex(b9.updated_at,
                         "[0-9]{4}-[0-9]{2}-[0-9]{2} [0-9]{2}:\
[0-9]{2}:[0-9]{2}.[0-9]*")

    def test_str(self):
        """Test the __str__ method"""
        b1 = BaseModel()
        b2 = BaseModel(None)
        b3 = BaseModel("name")
        b4 = BaseModel(3)
        b5 = BaseModel(2.5)
        b6 = BaseModel(float('inf'))
        b7 = BaseModel([1, 2, 3])
        b8 = BaseModel({"name": "Jay", "age": 20})
        
        correct_str = f"[BaseModel] ({b1.id}) {b1.__dict__}"
        correct_str = f"[BaseModel] ({b2.id}) {b2.__dict__}"
        correct_str = f"[BaseModel] ({b3.id}) {b3.__dict__}"
        correct_str = f"[BaseModel] ({b4.id}) {b4.__dict__}"
        correct_str = f"[BaseModel] ({b5.id}) {b5.__dict__}"
        correct_str = f"[BaseModel] ({b6.id}) {b6.__dict__}"
        correct_str = f"[BaseModel] ({b7.id}) {b5.__dict__}"
        correct_str = f"[BaseModel] ({b8.id}) {b6.__dict__}"
        
        self.assertEqual(correct_str, str(b1))
        self.assertEqual(correct_str, str(b2))
        self.assertEqual(correct_str, str(b3))
        self.assertEqual(correct_str, str(b4))
        self.assertEqual(correct_str, str(b5))
        self.assertEqual(correct_str, str(b6))
        self.assertEqual(correct_str, str(b7))
        self.assertEqual(correct_str, str(b8))

    def test_save(self):
        """Test __save__ method"""
        b1 = BaseModel()
        b1.save()
        b2 = BaseModel(None)
        b2.save()
        b3 = BaseModel("name")
        b3.save()
        b4 = BaseModel(3)
        b4.save()
        b5 = BaseModel(2.5)
        b5.save()
        b6 = BaseModel(float('inf'))
        b6.save()
        b7 = BaseModel([1, 2, 3])
        b7.save()
        b8 = BaseModel({"name": "Jay", "age": 20})
        b8.save()
        
        self.assertNotEqual(b1.created_at, b1.updated_at)
        self.assertNotEqual(b2.created_at, b2.updated_at)
        self.assertNotEqual(b3.created_at, b3.updated_at)
        self.assertNotEqual(b4.created_at, b4.updated_at)
        self.assertNotEqual(b5.created_at, b5.updated_at)
        self.assertNotEqual(b6.created_at, b6.updated_at)
        self.assertNotEqual(b5.created_at, b7.updated_at)
        self.assertNotEqual(b6.created_at, b8.updated_at)

    def test_to_dict(self):
        """Test to_dict method"""
        b1 = BaseModel()
        b2 = b1.to_dict()

        self.assertEqual(b1.id, b2['id'])


if __name__ == '__main__':
    unittest.main()
