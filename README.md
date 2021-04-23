# eshop
AN E-commerce site built with django

Functionalities includes:

# Shopping cart
# payment gateway
# Asynchronous email service update when an order has been completed

to get started with the project,ensure you have setup and activated a virtual environment, guides on that [here](https://realpython.com/python-virtual-environments-a-primer/)

clone the repository via the command

```
$ git clone https://github.com/E-wave112/eshop.git
```
install the dependencies

```
$ pip install -r requirements.txt
```

then you run migrations,
```
$ python manage.py migrate
```

create an admin superuser
```
$ python manage.py create superuser
```
start the server
```
$ python manage.py runserver
```
the server will be running on http://localhost:8000

and that's it !, you are free to customize any of the project or app's configs to suit your needs.
