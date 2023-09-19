import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    def test_id_assignment_when_none(self):
        """Test if the 'id' attribute is
        assigned correctly when id is None"""
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(obj_1.id, 1)
        self.assertEqual(obj_2.id, 2)
        
    def test_id_assignment_when_not_none(self):
        """Test if the 'id' attribute
        is assigned correctly when id is not None."""
        obj = Base(12)
        self.assertEqual(obj.id, 12)
        
    def test_nb_objects_increment(self):
        """Test that the private attribute __nb_objects
        increments as expected"""
        obj_1 = Base()
        obj_2 = Base()
        self.assertEqual(Base()._Base__nb_objects, 5)
        
if __name__ == "__main__":
    unittest.main()