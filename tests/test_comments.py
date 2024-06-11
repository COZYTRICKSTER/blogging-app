import unittest
from tests import BaseTestCase
from app.models import Post, Comment, db

class CommentTestCase(BaseTestCase):
    def test_create_comment(self):
        with self.app.app_context():
            post = Post(title='Test Post', content='This is a test post.')
            db.session.add(post)
            db.session.commit()

            response = self.client.post(f'/posts/{post.id}/comments', json={
                'content': 'This is a test comment.'
            })
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], 'Comment created successfully')

    def test_get_comments(self):
        with self.app.app_context():
            post = Post(title='Test Post', content='This is a test post.')
            db.session.add(post)
            db.session.commit()

            comment = Comment(content='This is a test comment.', post_id=post.id)
            db.session.add(comment)
            db.session.commit()

            post_id = post.id

        response = self.client.get(f'/posts/{post_id}/comments')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['content'], 'This is a test comment.')

if __name__ == '__main__':
    unittest.main()
