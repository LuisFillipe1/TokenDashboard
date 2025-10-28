# test_tokendashboard.py
"""
Tests for TokenDashboard module.
"""

import unittest
from tokendashboard import TokenDashboard

class TestTokenDashboard(unittest.TestCase):
    """Test cases for TokenDashboard class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = TokenDashboard()
        self.assertIsInstance(instance, TokenDashboard)
        
    def test_run_method(self):
        """Test the run method."""
        instance = TokenDashboard()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
