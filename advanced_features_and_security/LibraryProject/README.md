📘 LibraryProject
This is a Django web app that helps manage books in a library. You can add books, authors, genres, and keep track of whether a book is available or borrowed.

## Permissions and Groups Setup

Custom permissions were added to the `Book` model:
- can_view
- can_create
- can_edit
- can_delete

Groups created via Django admin:
- Viewers: can_view
- Editors: can_view, can_create, can_edit
- Admins: all permissions

Views were protected using `@permission_required` decorators.

## Security Enhancements

- `DEBUG = False` to avoid exposing debug info.
- CSRF and Session cookies are restricted to HTTPS only.
- Enabled browser protections via `X_FRAME_OPTIONS`, `SECURE_BROWSER_XSS_FILTER`, and `SECURE_CONTENT_TYPE_NOSNIFF`.
- Implemented CSP headers to restrict script/style origins.
- All forms include `{% csrf_token %}` to prevent CSRF.
- User inputs are sanitized via Django Forms.
- Database access is ORM-only to prevent SQL injection.
