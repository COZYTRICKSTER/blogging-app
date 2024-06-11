# Flask Blogging Application

This is a simple Flask application that provides a set of APIs for a blogging platform. Users can create posts, comment on posts, reply to comments, and view posts and their associated comments.

## Requirements

- Python 3.9.11
- Flask
- Flask SQLAlchemy
- SQLite (for local development)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/blogging-app.git
   ```

2. Navigate to the project directory:

   ```bash
   cd blogging-app
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the Flask application:

   ```bash
   flask run
   ```

2. The API endpoints are accessible at `http://localhost:5000/api`.

## API Endpoints

- `GET /api/posts`: Retrieve all posts.
- `POST /api/posts`: Create a new post.
- `GET /api/posts/<post_id>/comments`: Retrieve comments and their replies for a specific post.
- `POST /api/posts/<post_id>/comments`: Create a new comment or reply comment on a post.

## Testing

To run unit tests, execute the following command:

```bash
python -m unittest discover tests
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
