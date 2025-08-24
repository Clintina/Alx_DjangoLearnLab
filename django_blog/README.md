## Blog Post Management Features

This module allows authenticated users to create, edit, and delete blog posts. All users can view posts.

### Permissions
- Only logged-in users can create posts.
- Only post authors can edit or delete their posts.

### Comment System

- Authenticated users can add comments to blog posts.
- Only the comment author can edit or delete their own comments.
- Comments appear on the post detail page.
- URLs:
  - Add: `/post/<post_id>/comment/`
  - Edit: `/comment/<comment_id>/edit/`
  - Delete: `/comment/<comment_id>/delete/`

## Tagging and Search Features

### Tagging
- Add tags to posts using the post creation/edit form.
- Tags are comma-separated and auto-saved.
- Click on any tag to view related posts.

### Search
- Use the search bar to find posts by title, content, or tags.
- Results are displayed on a dedicated search results page.