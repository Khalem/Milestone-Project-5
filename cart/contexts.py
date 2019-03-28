from django.shortcuts import get_object_or_404
from animals.models import Animal


def cart_contents(request):
    """
        Ensures that the cart contents are availabe when rendering every page
    """
    
    cart = request.session.get('cart', {})
    
    cart_items = []
    total = 0
    product_count = 0
    for plan_name, quantity in cart.items():
        if "Basic Pack" in plan_name:
            product = get_object_or_404(Animal, adoptanimalone__plan_name=plan_name)
            total += quantity * product.adoptanimalone.price
        elif "Mega Pack" in plan_name:
            product = get_object_or_404(Animal, adoptanimaltwo__plan_name=plan_name)
            total += quantity * product.adoptanimaltwo.price
        elif "Ultimate Pack" in plan_name:
            product = get_object_or_404(Animal, adoptanimalthree__plan_name=plan_name)
            total += quantity * product.adoptanimalthree.price
        
        product_count += quantity
        cart_items.append({"plan_name": plan_name, "quantity": quantity, "product": product})
        
    return { "cart_items": cart_items, "total": total, "product_count": product_count }