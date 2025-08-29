📘 Social Media API — Django Backend
A RESTful API for user authentication and account management, built with Django and Django REST Framework. This project is part of the ALX Backend Development capstone.

🚀 Features
- User registration, login, and logout
- Token-based authentication (JWT or DRF tokens)
- Modular URL structure (/api/accounts/)
- Swagger UI for interactive API documentation

🛠️ Tech Stack
|  |  | 
|  |  | 
|  |  | 
|  |  | 
|  |  | 



📦 Installation
# Clone the repo
git clone https://github.com/yourusername/social_media_api.git
cd social_media_api

# Create virtual environment
python -m venv .env
source .env/Scripts/activate  # Windows
# or
source .env/bin/activate      # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python manage.py migrate

# Run server
python manage.py runserver



🔐 API Endpoints
|  |  |  | 
|  | /api/accounts/register/ |  | 
|  | /api/accounts/login/ |  | 
|  | /api/accounts/logout/ |  | 

🔐 Authentication
- Explain token-based auth using POST /api/accounts/register/ and POST /api/accounts/login/
- Show how to include the token in headers:
Authorization: Token your_token_here


👥 Follow System
- POST /api/accounts/follow/<user_id>/ — Follow a user
- POST /api/accounts/unfollow/<user_id>/ — Unfollow a user
- Note: Users can’t follow themselves
📝 Posts & Comments
- CRUD endpoints for posts:
- GET /api/posts/, POST /api/posts/, PUT /api/posts/<id>/, DELETE /api/posts/<id>/
- Same for comments: GET /api/comments/, etc.
- Mention permissions: only authors can edit/delete their own content
📰 Feed Endpoint
- GET /api/feed/ — Returns posts from followed users, newest first
🧪 Testing
- Mention any unit tests or manual testing done
- Confirm endpoints return correct status codes and error messages



