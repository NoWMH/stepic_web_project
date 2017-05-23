# bash /home/box/web/init.sh
# gunicorn -c <this-config-file-with-full-PATH> hello:application

thepath = '/home/box/web'
bind = "0.0.0.0:8080"
workers = 2
daemon = True

