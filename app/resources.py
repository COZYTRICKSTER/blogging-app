from flask import Blueprint, jsonify, request
from app import db
from app.models import Post, Comment

resources_bp = Blueprint('resources', __name__, url_prefix='/api')

@resources_bp.route('/posts', methods=['GET', 'POST'])
def posts():
    if request.method == 'GET':
        posts = db.session.query(Post).all()
        result = [{'id': post.id, 'title': post.title, 'content': post.content} for post in posts]
        return jsonify(result)
    elif request.method == 'POST':
        data = request.json
        new_post = Post(title=data['title'], content=data['content'])
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'}), 201

@resources_bp.route('/posts/<int:post_id>/comments', methods=['GET', 'POST'])
def comments(post_id):
    if request.method == 'GET':
        post = db.session.get(Post, post_id)
        if not post:
            return jsonify({'message': 'Post not found'}), 404
        comments = Comment.query.filter_by(post_id=post_id, parent_id=None).all()
        result = [{'id': comment.id, 'content': comment.content, 'replies': get_replies(comment)} for comment in comments]
        return jsonify(result)
    elif request.method == 'POST':
        data = request.json
        new_comment = Comment(content=data['content'], post_id=post_id)
        if 'parent_id' in data:
            parent_comment = Comment.query.get(data['parent_id'])
            new_comment.parent = parent_comment
        db.session.add(new_comment)
        db.session.commit()
        return jsonify({'message': 'Comment created successfully'}), 201

@resources_bp.route('/comments/<int:comment_id>/reply', methods=['POST'])
def reply_to_comment(comment_id):
    data = request.json
    content = data.get('content')
    if not content:
        return jsonify({'error': 'Content is required'}), 400

    parent_comment = db.session.get(Comment, comment_id)
    if not parent_comment:
            return jsonify({'message': 'Comment not found'}), 404
    reply = Comment(content=content, post_id=parent_comment.post_id, parent_id=comment_id)
    db.session.add(reply)
    db.session.commit()
    return jsonify({'message': 'Reply created'}), 201        

def get_replies(comment):
    replies = []
    for reply in comment.replies:
        replies.append({'id': reply.id, 'content': reply.content, 'replies': get_replies(reply)})
    return replies
