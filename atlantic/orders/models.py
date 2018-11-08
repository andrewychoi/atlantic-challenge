from django.db import models

"""
From spec:

Customer id (an integer)
Customer first name
Customer last name
Customer street address (assume US addresses only)
Customer state (assume US addresses only)
Customer zip code (assume US addresses only)
Change in purchase status - this will be either 'new' or 'canceled'
Product id for purchase (an integer)
Product name (a string, not longer than 100 characters)
Product purchase amount (in US dollars)
Date and time in ISO8601 format, i.e. 2007-04-05T14:30Z
"""


class Customer(models.Model):
    """
    Notes:
    We store customer zipcodes as text because they don't generally carry value as integers
    """
    customer_id = models.IntegerField()
    first_name = models.TextField()
    last_name = models.TextField()
    address = models.TextField()
    state = models.TextField()
    zipcode = models.TextField()


class Product(models.Model):
    product_id = models.IntegerField()
    name = models.TextField(max_length=100)


class Purchase(models.Model):
    """
    models.DecimalField is a fixed point number representation, because dollars and cents are exact.
    For max_digits, we use 1 quadrillion dollars--10e15 + 2 decimal places
    """
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)

    NEW = 'new'
    CANCELED = 'canceled'
    STATUS_CHOICES = (
        (NEW, 'New'),
        (CANCELED, 'Canceled'),
    )
    status = models.TextField(
        choices=STATUS_CHOICES,
        default=NEW,
    )
    status = models.TextField()
    amount = models.DecimalField(max_digits=15 + 2, decimal_places=2)
    datetime = models.DateTimeField()
