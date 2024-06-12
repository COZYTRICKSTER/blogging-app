import unittest
from tests import BaseTestCase
from app.models import Post, Comment, db

class CommentTestCase(BaseTestCase):
    def test_create_comment(self):
        print("---------> test_create_comment")
        with self.app.app_context():
            post = Post(title='Test Post', content='This is a test post.')
            db.session.add(post)
            db.session.commit()

            response = self.client.post(f'api/posts/{post.id}/comments', json={
                'content': 'This is a test comment.'
            })
            self.assertEqual(response.status_code, 201)
            self.assertEqual(response.json['message'], 'Comment created successfully')

    def test_get_comments(self):
        print("---------> test_get_comments")
        with self.app.app_context():
            post = Post(title='Test Post', content='This is a test post.')
            db.session.add(post)
            db.session.commit()

            comment = Comment(content='This is a test comment.', post_id=post.id)
            db.session.add(comment)
            db.session.commit()

            post_id = post.id

        response = self.client.get(f'api/posts/{post_id}/comments')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['content'], 'This is a test comment.')

    def test_reply_to_comment(self):
        print("---------> test_reply_to_comment")
        with self.app.app_context():
            with self.app.test_request_context():
                post = Post(title='Sample Post', content='This is a sample post.')
                db.session.add(post)
                db.session.commit()

                comment = Comment(content='This is a sample comment.', post_id=post.id)
                db.session.add(comment)
                db.session.commit()

                response = self.client.post(f'/api/comments/{comment.id}/reply', json={
                    'content': 'This is a reply to the sample comment.'
                })
                self.assertEqual(response.status_code, 201)
                self.assertIn('Reply created', response.get_data(as_text=True))

                response = self.client.get(f'/api/posts/{post.id}/comments')
                self.assertEqual(response.status_code, 200)
                data = response.get_json()
                self.assertEqual(len(data[0]['replies']), 1)
                self.assertEqual(data[0]['replies'][0]['content'], 'This is a reply to the sample comment.')


if __name__ == '__main__':
    unittest.main()
