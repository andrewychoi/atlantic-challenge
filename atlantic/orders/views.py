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
    # UNSAFE! NEED TO VERIFY THIS!
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
        purchase, created = Purchase.objects.get_or_create(
            status=status,
            amount=amount,
            datetime=datetime,
            customer=customer,
            product=product
        )


def success(request):
    return render(request, "uploaded.html")
