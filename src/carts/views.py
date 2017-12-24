from django.shortcuts import render
from .models import Cart

def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    print('New Cart Created with id: ')
    print(cart_obj.id)
    return cart_obj

def cart_home(request):
    # delete session
    # del request.session['cart_id']
    # Check if cart id already exists
    print("Starting Cart ID: ")
    print(request.session.get("cart_id"))
    cart_id = request.session.get("cart_id", None)
    if cart_id is None: # and isinstance(cart_id, int): #Check if exists and integer
        cart_obj = cart_create()
        request.session['cart_id'] = cart_obj.id
    else:
        # if isinstance(cart_id, int): # not needed
        qs = Cart.objects.filter(id=cart_id)
        if qs.count() == 1:
            print('cart id exists')
            cart_obj = qs.first()
        else:
            cart_obj = cart_create()
            request.session['cart_id'] = cart_obj.id

        # cart_obj = Cart.objects.get(id=cart_id)
        
    # print(request.session) #saved on request object by default

    # print available methods for session
    # print(dir(request.session))
    #request.session.set_expiry(300) #300 seconds
    # print(request.session.session_key)

    # key = request.session.session_key
    # print(key)

    # print(request.session.get("first_name")) # Getter
    # request.session['first_name'] = "Robbo" # Setter
    return render(request, "carts/home.html", {})