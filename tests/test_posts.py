import unittest
from tests import BaseTestCase
from app.models import Post, db

class PostTestCase(BaseTestCase):
    def test_create_post(self):
        response = self.client.post('/posts', json={
            'title': 'Test Post',
            'content': 'This is a test post.'
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json['message'], 'Post created successfully')

    def test_get_posts(self):
        with self.app.app_context():
            post = Post(title='Test Post', content='This is a test post.')
            db.session.add(post)
            db.session.commit()
            post_id = post.id

        response = self.client.get('/posts')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json), 1)
        self.assertEqual(response.json[0]['title'], 'Test Post')
        self.assertEqual(response.json[0]['id'], post_id)

if __name__ == '__main__':
    unittest.main()
