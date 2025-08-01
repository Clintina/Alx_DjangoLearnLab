
---

### ✅ `security_review.md`

```markdown
# Security Review Report

## HTTPS & Secure Redirects

- `SECURE_SSL_REDIRECT = True` ensures that all HTTP requests are redirected to HTTPS automatically.
- `SECURE_HSTS_SECONDS = 31536000` enables HTTP Strict Transport Security (HSTS) for 1 year.
- `SECURE_HSTS_INCLUDE_SUBDOMAINS = True` and `SECURE_HSTS_PRELOAD = True` enforce HTTPS across all subdomains and allow browser preloading.
- Cookies are protected using:
  - `SESSION_COOKIE_SECURE = True`
  - `CSRF_COOKIE_SECURE = True`

## Secure Headers

- `X_FRAME_OPTIONS = 'DENY'` blocks clickjacking attacks by preventing the site from being rendered inside an iframe.
- `SECURE_CONTENT_TYPE_NOSNIFF = True` prevents browsers from guessing content types, reducing XSS risk.
- `SECURE_BROWSER_XSS_FILTER = True` enables the browser’s XSS filtering mechanism.

## Deployment

- SSL is terminated at the web server (e.g., Nginx) using Let's Encrypt certificates.
- A 301 redirect is enforced from HTTP to HTTPS at the server level.

## Potential Improvements

- A Content Security Policy (CSP) has been implemented in a previous task.
- For local testing over HTTPS, consider using tools like `mkcert` or `django-sslserver`.

---

All settings have been configured in `LibraryProject/settings.py` with inline comments for clarity.
