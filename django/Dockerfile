#Create the container from ubuntu image
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]
#Define ARG variable and ENV variable for build
ARG ALLOWED_HOST_PARAM
ENV ALLOWED_HOST=$ALLOWED_HOST_PARAM

#Install python, pip, apache, wsgi module, ufw and sudo
RUN apt-get update && apt-get -y install python3-pip apache2 libapache2-mod-wsgi-py3 ufw sudo vim

#Set working directory in container to /var/www/html
WORKDIR /var/www/html

#Copy the project files to container
COPY . .

#Install virtualenv
RUN pip3 install virtualenv

#Activate virtual environment
RUN virtualenv ./venv

#Install python dependencies
RUN source venv/bin/activate \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& python3 manage.py collectstatic

#Grant permissions for logs
RUN chmod 750 /var/log/apache2

#Grant permissions to www-data for writing and reading
RUN chmod 770 /var/www/html

#Grant permissions to www-data for writing and reading to sqlite3
RUN chmod 770 /var/www/html/db.sqlite3
RUN chown :www-data /var/www/html/

#Modify group for folders and files
RUN chown :www-data /var/www/html/space_missions
RUN chown :www-data /var/www/html/db.sqlite3
RUN sudo chown root:www-data /var/log/apache2

#Add ALLOWED_HOST to settings in Django project to allow request from apache server
RUN sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['"$ALLOWED_HOST"'\]/" space_missions/settings.py

#Add configuration for virtual host
ADD ./configuration_virtualhost.conf /etc/apache2/sites-available/000-default.conf

#Add configuration for aliases
ADD ./configuration_alias.conf /etc/apache2/mods-available/alias.conf

#Allow apache services through firewall
RUN sudo ufw allow "Apache Full"

#Expose container for apache and django
EXPOSE 80 8000

#Run the command
CMD ["apache2ctl", "-D", "FOREGROUND"]
