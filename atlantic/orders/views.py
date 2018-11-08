from django.shortcuts import render
from django.http import HttpResponseRedirect

from orders.forms import UploadFileForm


def home(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES["file"])
            # handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("/success/")
    else:
        form = UploadFileForm()
    return render(request, "uploader.html", {"form": form})


def success(request):
    return render(request, "uploaded.html")
