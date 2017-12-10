from django.shortcuts import render
from django.shortcuts import HttpResponse
from .forms import ContactForm

def home_page(request):
    context_ = {
        "title": "Home Page",
        "text": "Text from context",
        "content": "Welcome to the home page"
    }
    return render(request, "home_page.html", context_)

def about_page(request):
    # Create instance of contact form class
    context_ = {
        "title": "About Page",
        "content": "About Us",        
    }
    return render(request, "home_page.html", context_)

def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context_ = {
        "title": "Contact Page",
        "content": "Our contact details",
        "form": contact_form
    }    
    if contact_form.is_valid():
        print(contact_form.cleaned_data)

    # # Not needed for Django forms
    # if request.method == "POST":
    #     print(request.POST)
    #     print(request.POST.get('fullname'))
    #     print(request.POST.get('email'))
    return render(request, "contact/view.html", context_)

def home_page_old(request):
    html_ = """
        <!doctype html>
        <html lang="en">
        <head>
            <title>Hello, world!</title>
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            <!-- Bootstrap CSS -->
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
        </head>
        <body>
            <div class='text-center'>
            <h1>Hello, world!</h1>
            </div>

            <!-- Optional JavaScript -->
            <!-- jQuery first, then Popper.js, then Bootstrap JS -->
            <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js" integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh" crossorigin="anonymous"></script>
            <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js" integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ" crossorigin="anonymous"></script>
        </body>
        </html>
    """
    return HttpResponse(html_)