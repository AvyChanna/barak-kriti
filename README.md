# barak-kriti

## Installation

- Run the following script

```bash
# python.__version__ >= 3.6 (for fmt strings)

python -m pip install --user -r requirements/local.txt      # for debug build
python -m pip install --user -r requirements/production.txt # for release build
sudo apt install postgresql
su - postgres # change user
psql # open sql shell
>> create database aspire;
>> create user $USER with password $PASSWORD;
>> grant all privileges on database aspire to $USER;
>> \l # Print databases
>> \du # Print users
>> \q

logout # switch back to $USER 's prompt


python manage.py makemigrations
python manage.py migrate
# database done

python manage.py createsuperuser

python manage.py runserver $IP:$PORT
#( ip and port optional, default are 127.0.0.1:8000 )

```

- Goto <http://$IP:$PORT/admin>

- Add a DepartmentalHead Group(with correct permissions) and add some accounts into them.

- Add data to different fields ( if required )

- Server is ready 😍

- For the app, goto strings.xml and edit the ip. App is also ready.
