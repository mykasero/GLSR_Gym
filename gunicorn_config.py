workers = 4
bind = "0.0.0.0:8000"
chdir = "/app/"
module = "app.wsgi:application"

# certfile = "/etc/letsencrypt/live/glsr.com/fullchain.pem"
# keyfile = "etc/letsencrypt/live/glsr.com/privkey.pem"