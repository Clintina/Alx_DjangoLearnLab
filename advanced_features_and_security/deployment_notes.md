# Deployment Notes for HTTPS Configuration

## SSL Setup
To secure the Django application with HTTPS in production, SSL/TLS certificates must be installed and properly configured at the web server level. Free certificates can be obtained using Let's Encrypt.

### Example Nginx Configuration (SSL Enabled)
```nginx
server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8000;
        include proxy_params;
    }
}

server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}
