from hn import Story
import unittest

class TestStoryGetComments(unittest.TestCase):

    def test_get_nested_comments(self):
    	self.story = Story.fromid(7404389)
        self.comments = self.story.get_comments()
        comment = self.comments[0].body
        self.assertTrue(len(comment) >= 5508)

    def test_get_nested_comments_old_story(self):
    	self.story = Story.fromid(7410260)
        self.comments = self.story.get_comments()
    	comment = self.comments[0].body
    	self.assertEqual(len(comment), 2131)

if __name__ == '__main__':
     unittest.main()
