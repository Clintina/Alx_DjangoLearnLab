Authentication Flow
This document explains how user authentication works in the project: registration, login, logout, and profile.
Registration
URL: /register/
View:
- Uses a custom CustomUserCreationForm in forms.py
- Saves the new user and redirects to the login page
Form (blog/forms.py):
- Extends Django’s UserCreationForm
- Adds an email field
- Fields: username, email, password1, password2
Template: templates/registration/register.html
Login
URL: /login/
View:
- Uses Django’s built‑in LoginView
Template: templates/registration/login.html
Logout
URL: /logout/
View:
- Uses Django’s built‑in LogoutView
Template: templates/registration/logout.html
Profile
URL: /profile/
View:
- Protected with @login_required
- Displays the logged‑in user’s username and email
Template: templates/profile.html
URL Configuration
In blog/urls.py:
- /register/ → register view
- /profile/ → profile view
- Includes Django’s auth URLs for login/logout
Template Structure
templates/
- base.html
- profile.html
- registration/
- login.html
- logout.html
- register.html
Notes
- All forms use {% csrf_token %} for security
- @login_required ensures only logged‑in users can access /profile/
- After registration, users are redirected to the login page
- After login, users are redirected to /profile/ (set in LOGIN_REDIRECT_URL in settings.py)
- Passwords are hashed automatically by Django
Settings
In settings.py:
LOGIN_REDIRECT_URL = 'profile'
LOGOUT_REDIRECT_URL = 'login'


Future Enhancements
- Add password reset
- Add email verification
- Improve styling with CSS framework
