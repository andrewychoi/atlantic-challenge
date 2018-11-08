from decimal import Decimal
from dateutil.parser import parse as parse_datetime

from django.shortcuts import render
from django.http import HttpResponseRedirect

from orders.forms import UploadFileForm
from orders.models import Customer, Product, Purchase


def home(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/")
    else:
        form = UploadFileForm()
    return render(request, "uploader.html", {"form": form})


def handle_uploaded_file(uploaded_file):
    # UNSAFE! NEED TO VERIFY CHARACTER ENCODING!
    encoding = uploaded_file.charset if uploaded_file.charset else "utf-8"
    for line_bytes in uploaded_file:
        line = line_bytes.decode(encoding)
        splits = line.split("\t")
        (
            customer_id,
            first_name,
            last_name,
            address,
            state,
            zipcode,
            status,
            product_id,
            product_name,
            amount,
            datetime
        ) = splits

        # convert to proper types:
        customer_id = int(customer_id)
        product_id = int(product_id)
        amount = Decimal(amount)
        datetime = parse_datetime(datetime)

        # update logic for customer addresses would need to go here
        # try to get customer on basis of ID or name, and update otherwise
        # currently we throw away an update to name or address
        customer, created = Customer.objects.get_or_create(
            customer_id=customer_id,
            defaults={
                "first_name": first_name,
                "last_name": last_name,
                "address": address,
                "state": state,
                "zipcode": zipcode,
            })

        product, created = Product.objects.get_or_create(
            product_id=product_id,
            defaults={
                "name": product_name,
            })

        # validation for purchase should go here:
        # untested, but something like:
        """
        if status == "canceled":
            latest_purchase = Purchase.objects.filter(
                amount=amount, customer=customer, product=product
                ).latest("datetime")
            if not latest_purchase.exists():
                raise ValueError("No purchase to cancel")
            if latest_purchase.status == "canceled"
                raise ValueError("Purchase already canceled")

        """
        purchase, created = Purchase.objects.get_or_create(
            status=status,
            amount=amount,
            datetime=datetime,
            customer=customer,
            product=product
        )


def success(request):
    return render(request, "uploaded.html")
