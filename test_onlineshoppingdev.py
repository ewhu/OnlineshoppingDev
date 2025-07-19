# test_onlineshoppingdev.py
"""
Tests for OnlineshoppingDev module.
"""

import unittest
from onlineshoppingdev import OnlineshoppingDev

class TestOnlineshoppingDev(unittest.TestCase):
    """Test cases for OnlineshoppingDev class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = OnlineshoppingDev()
        self.assertIsInstance(instance, OnlineshoppingDev)
        
    def test_run_method(self):
        """Test the run method."""
        instance = OnlineshoppingDev()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
