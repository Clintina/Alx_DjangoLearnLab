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
