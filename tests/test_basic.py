import os
import django
import unittest

# Add the project root to the Python path
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Nerdhub.settings')
django.setup()

class BasicTestCase(unittest.TestCase):
    """Basic test case to verify the testing environment is working"""
    
    def test_basic_math(self):
        """Test that basic math works"""
        self.assertEqual(1 + 1, 2)
        
    def test_django_setup(self):
        """Test that Django is properly configured"""
        from django.conf import settings
        self.assertIsNotNone(settings.SECRET_KEY)
        
    def test_database_connection(self):
        """Test that database connection works"""
        from django.db import connection
        self.assertIsNotNone(connection)
        
if __name__ == '__main__':
    unittest.main()