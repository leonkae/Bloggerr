from msilib.schema import Class
import unittest

from main import models,User, Post

'''writing tests'''

class User(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User ("john","Doe","JohnDoe","john@gmail.com","john1234")
        
    def test_init(self):
        self.assertTrue(self.new_user.first_name,"john")
        self.assertTrue(self.new_user.last_name,"Doe")
        self.assertTrue(self.new_user.username,"johnDoe")
        self.asserTrue(self.new_user.email,"john@gmail.com")
        self.assertTrue(self.new_user.password,"john1234")
        
    
    def tearDown(self):
        User.user_list =[]
        
    def test_save(self):
        '''tests saving of an account'''
        self.new_account.save_account()
        self.assertTrue(len(User.user_list),1)
        
    def test_save_multiple_accounts(self):
        '''tests saving of multiple accounts'''
        self.new_account.save_account()
        extra_account = User("john","Doe","johnDoe","john@gmail.com","john1234")
        extra_account.save_account()
        
        self.assertTrue(len(User.user_list),2)
    
    def test_account_exists(self):
        '''test if account exits'''
        self.new_account.save_account()
        new_account = User ("john","Doe","johnDoe","john@gmail.com","john1234")
        email_exists = User ("pseudo@gmail.com")
        self.assertTrue(email_exists)
        
    def test_account_login(self):
        account1 = self.new_account.save_account()
        account1_present = User.account_login("pseudo@gmail.com","john1234")  
        
        self.assertTrue(account1_present)
      
    def test_show_account(self):
        '''tests for show'''
        self.assertEqual(User.show_account(),User.user_list)        
        
class Post (unittest.TestCase):
    '''tests for post'''
    def setUp(self):
        self.new_post = Post("title","date","this is content")
        
        
    def test_init(self):
        self.assertTrue(self.post.title,'title')
        self.assertTrue(self.post.date_posted,'date')
        self.assertTrue(self.post.content,'this is content')
        
    def test_store_post(self):
        self.new_post.store_post()
        self.assertEqual(len(Post.posts_list),3)
        
    def test_find_post(self):
        '''test for post'''
        self.new_post.store_post()
        post_check = Post ("title","date","content")   
        post_check.store_post()
        
        post = Post.find_post("title")
        
        self.assertTrue(post_check.account1_present)    
    
class Comments(unittest.TestCase):
    '''tests for comments'''
    def setUp(self):
        self.new_comment= Comments("comment")       
        
    def test_init(self):
        self.asssertTrue(self.Comments.comment,"comment")   
           
if __name__== '__main__':
    unittest.main()