from datetime import datetime
import unittest
from app.models import Post


class Post(unittest.TestCase):
    
  def setUp(self) -> None:
      self.new_blog_post = Post(id=1, title='blog',  content='This blog is great', date=datetime.now)



  def test_instance(self):
    self.assertTrue(isinstance(self.new_post, Post))
    
  
if __name__ == '__main__':
  unittest.main()  
    