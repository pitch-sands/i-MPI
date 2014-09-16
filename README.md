A social network 
========================

Basic user registration package for Flask.

- Flask==0.10.1
- Flask-SQLAlchemy==0.16
- Flask-WTF==0.8.4
- Jinja2==2.7
- MarkupSafe==0.18
- SQLAlchemy==0.8.2
- WTForms==1.0.4
- Werkzeug==0.9.1
- itsdangerous==0.22
- wsgiref==0.1.2





## Todo

1. normal register, login&logout with sqlite database(completed 16th Sep)
2. remember split normal user and admin, creat chatting group(wirklich)
3. adding friends(optional)
4. ...
5. ...


## Project structure

    ```
    ├── app
    │   ├── __init__.py
    │   ├── forms.py
    │   ├── models.py
    │   ├── templates
    │   │   ├── 404.html
    │   │   ├── 500.html
    │   │   ├── base.html
    │   │   ├── login.html
    │   │   ├── members.html
    │   │   └── register.html
    │   └── views.py
    ├── config.py
    ├── db_create.py
    ├── error.log
    ├── requirements.txt
    └── run.py
    ```
