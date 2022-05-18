from datetime import datetime
import unittest
from app.models import User


class TestUser(unittest.TestCase):


  def setUp(self) :
      self.new_user = User(password = 'beth')


  def test_password_verification(self):
    self.assertTrue(self.new_user.verify_password('beth'))


  def test_user_instance(self):
    self.assertTrue(isinstance(self.new_user, User))
    
    
if __name__ == '__main__':
  unittest.main()