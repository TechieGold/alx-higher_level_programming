import unittest
from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    
    def test_construtor_with_id(self):
        # Test constructor when id is provided.
        rectangle_obj = Rectangle(10, 15, 5, 5, id=42)
        self.assertEqual(rectangle_obj.id, 42)
        self.assertEqual(rectangle_obj.width, 10)
        self.assertEqual(rectangle_obj.height, 15)
        self.assertEqual(rectangle_obj.x, 5)
        self.assertEqual(rectangle_obj.y, 5)
        
        def test_constructor_without_id(self):
            # Test constructor when no id is provided
            rectangle_obj = Rectangle(10, 15, 5, 5)
            self.assertTrue(hasattr(rectangle_obj, 'id'))
            self.assertIsInstance(rectangle_obj.id, int)
            self.assertEqual(rectangle_obj.width, 10)
            self.assertEqual(rectangle_obj.height, 15)
            self.assertEqual(rectangle_obj.x, 5)
            self.assertEqual(rectangle_obj.y, 5)
            
        def test_invalid_width(self):
            # Test setting an invalid width.
            with self.assertRaises(ValueError):
                Rectangle(-10, 15, 5, 5)
                
        def test_invalid_height(self):
                # Test setting invalid height
                with self.assertRaises(ValueError):
                    Rectangle(10, 0, 5, 5)
            
        def test_invalid_x(self):
            # Test setting an invalide x-coordinate.
            with self.assertRaises(ValueError):
                Rectangle(10, 15, -5, 5)
                
        def test_invalid_y(self):
            # Test setting an invalid y-coordinate.
            with self.assertRaises(ValueError):
                Rectangle(10, 15, 5, -5)
                
if __name__ == '__main__':
    unittest.main()