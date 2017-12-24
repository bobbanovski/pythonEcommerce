from django.shortcuts import render

# Create your views here.
def cart_home(request):
    print(request.session) #saved on request object by default
    # print available methods for session
    print(dir(request.session))
    #request.session.set_expiry(300) #300 seconds
    # print(request.session.session_key)
    key = request.session.session_key
    print(key)
    print(request.session.get("first_name")) # Getter
    # request.session['first_name'] = "Robbo" # Setter
    return render(request, "carts/home.html", {})