# eshop
AN E-commerce web application built with Django

Functionalities includes:

- The ability for users to store items in a cart session before they checkout
- The ability for users to filter products based on their categories and purchase any quantity of any product.
- The ability for users to make live payments via the integrated [Braintree](https://www.braintreepayments.com/) payment gateway
- A notification email sent asynchronously via [celery](https://docs.celeryproject.org/en/stable/) and Redis as a message broker to users on completion of ordering or fully purchasing a product.
- [Redis](https://redis.io/) cache for storing product data and cart details of each product and potential purchases

To get started with the project,ensure you have setup and activated a virtual environment, guides on that [here](https://realpython.com/python-virtual-environments-a-primer/)

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

and that's it!, you are free to customize and extend any of the project features or app's configs to suit your needs.
