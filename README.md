### Space app is a web site for astronomy classes.
On a main page added a picture of the day - NASA API project, which shows every day a picture (or video)
and an explanation.

![image](https://github.com/u-shev/space-app/assets/96250059/a1033444-373f-42b3-8038-5682d70467e2)

Also added posts, 4 on each page.

![image](https://github.com/u-shev/space-app/assets/96250059/74443770-1fbd-4e81-9d6f-6a0e202b9a80)

Pupils can register, login and add posts

![image](https://github.com/u-shev/space-app/assets/96250059/ce784905-9eba-49de-ae91-85294fd1af8a)

with one added picture which is used as preview on a main page.
Pupils can edit or delete their posts (only author can see links). Every post got views counter.

![image](https://github.com/u-shev/space-app/assets/96250059/c7b67d73-80f9-43a5-8892-ec4032433d4a)

Pages got pagination

![image](https://github.com/u-shev/space-app/assets/96250059/5a973002-4ec9-4384-8cfa-94ecb24b5c5f)

Pupils cannot change or delete their profiles, that's up to teaher. Every Monday at 8.30 each of those who added posts get statistic of views sent to email.

## Installation
### Prerequisites
#### Python
Before installing the package make sure you have Python version 3.8 or higher installed:
```
python --version
```
#### Poetry
The project uses the Poetry dependency manager. To install Poetry use its [official instruction](https://python-poetry.org/docs/#installing-with-pipx).

#### PostgreSQL
PostgreSQL is used as the main database management system. You have to install it first. It can be downloaded from [official website](https://www.postgresql.org/download/)
### Application
#### Clone the project
```
git clone git@github.com:u-shev/space-app.git
cd space-app
```
#### Create virtual environment
```
python -m venv /path/to/new/virtual/environment
```
#### Create .env file in the root folder and add following variables
```
DATABASE_URL=postgresql://{username}:{password}@{host}:{port}/{databasename}  
SECRET_KEY='{your secret key}'
EMAIL_HOST_USER='{your email adress, if you use different from mail.ru post, you should change EMAIL_HOST, EMAIL_PORT, EMAIL_USE_TLS, EMAIL_USE_SSL varaibles in settings.py}'
EMAIL_HOST_PASSWORD='{it's not your post password! you shoul get special password for application in settings of your post operator}'
```
#### To create the necessary tables in the database, start the migration process
```
make migrate
```
### Usage
#### Start the Uviicorn Web-server by running:
```
make start
```
By default, the server will be available at http://0.0.0.0:8000.

#### It is also possible to start it local in development mode using:
```
make run
```
The dev server will be at http://127.0.0.1:8000.

To use Celery you should open different terminals for:
 - (global env) Redis with command
   ```
   redis-server
   ```
 - (virtual env) Celery worker with command
   ```
   make worker
   ```
 - (virtual env) Celery beat with command
   ```
   make beat
   ```

### Additional makefile commands
#### make lint
starts linter check
#### make test
starts tests
