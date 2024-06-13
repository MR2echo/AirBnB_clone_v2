#!/usr/bin/env bash
# sets up the web servers for the deployment of web_static

# install Nginx 
apt-get -y update
apt-get -y install nginx

# create folders if they don't already exist
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

# create fake HTML file
echo "Holberton School" > /data/web_static/releases/test/index.html

# create a symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# give ownership of the /data/ folder to the ubuntu user and group
chown -R ubuntu /data/
chgrp -R ubuntu /data/

# update the Nginx configuration to serve the content of /data/web_static/current/ to hbnb_static
sed -i '41i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t\tautoindex off;\n\t}\n' /etc/nginx/sites-available/default

# restart Nginx
service nginx restart

