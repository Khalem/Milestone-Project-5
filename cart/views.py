from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_cart(request):
    """
        This view renders everything in the cart
    """
    return render(request, "cart.html")
    
def add_to_cart(request, plan_name):
    """
        Add a quantity of specified product to cart
    """
    quantity=int(request.POST.get("quantity"))
    
    cart = request.session.get("cart", {})
    
    if plan_name in cart:
        cart[plan_name] = int(cart[plan_name]) + quantity
    else:
        cart[plan_name] = cart.get(plan_name, quantity)
    
    request.session["cart"] = cart
    return redirect(reverse("index"))
    
def adjust_cart(request, plan_name):
    """
        Adjust the quantity of a specified product by a specified amount
    """
    quantity = int(request.POST.get("quantity"))
    cart = request.session.get("cart", {})
    
    if quantity > 0:
        cart[plan_name] = quantity
    else:
        cart.pop(plan_name)
    
    request.session["cart"] = cart
    return redirect(reverse("view_cart"))