#Create the container from ubuntu image
FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
SHELL ["/bin/bash", "-c"]
#Set the working directory to usr/src/app
#WORKDIR /usr/src/app
#Copy the project files to container
#COPY . .
ARG ALLOWED_HOST_PARAM
ENV ALLOWED_HOST=$ALLOWED_HOST_PARAM
#RUN echo "ALLOWEDHOST es $ALLOWED_HOST"
#RUN echo "ALLOWED_HOST_PARAM $ALLOWED_HOST_PARAM"
#Install python and pip
#RUN apt-get update -y
#RUN apt-get install python3-pip apache2 libapache2-mod-wsgi-py3 -y
RUN apt-get update && apt-get -y install python3-pip apache2 libapache2-mod-wsgi-py3 ufw sudo vim
#Install virtualenv
WORKDIR /var/www/html
COPY . .
RUN pip3 install virtualenv
#Activate virtual environment
RUN virtualenv ./venv
#RUN source venv/bin/activate
#Install dependencies
RUN source venv/bin/activate \
&& pip install --no-cache-dir --upgrade pip \
&& pip install --no-cache-dir -r requirements.txt \
&& python3 manage.py collectstatic
#RUN sudo mkdir /var/log/apache2

#RUN chmod 664 /var/www/html/db.sqlite3
#RUN chmod 775 /var/www/html/space_missions
RUN chmod 750 /var/log/apache2
RUN chmod 770 /var/www/html
#RUN chmod 770 /var/www
#RUN chmod 770 /var
RUN chmod 770 /var/www/html/db.sqlite3
RUN chown :www-data /var/www/html/
RUN chown :www-data /var/www/html/space_missions
RUN chown :www-data /var/www/html/db.sqlite3
RUN sudo chown root:www-data /var/log/apache2
RUN sed -i "s/ALLOWED_HOSTS = \[\]/ALLOWED_HOSTS = \['"$ALLOWED_HOST"'\]/" space_missions/settings.py
ADD ./configuration_virtualhost.conf /etc/apache2/sites-available/000-default.conf
ADD ./configuration_alias.conf /etc/apache2/mods-available/alias.conf
#RUN source venv/bin/activate/ \&& python3 manage.py collectstatic
RUN sudo ufw allow "Apache Full"
#RUN ufw allow "Apache Full"
#RUN systemctl restart apache2
#Expose container for apache and django
EXPOSE 80 8000

#Run the command
CMD ["apache2ctl", "-D", "FOREGROUND"]
#CMD ["/bin/bash"]
#CMD ["python3","manage.py","runserver","8000"]
#CMD ["service","apache2","restart"]