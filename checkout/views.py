from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from animals.models import Animal
import stripe


# Create your views here.

stripe.api_key = settings.STRIPE_SECRET

@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)
        
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            
            cart = request.session.get("cart", {})
            total = 0
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
                order_line_item = OrderLineItem(
                    order = order,
                    product = product,
                    quantity = quantity
                    )
                order_line_item.save()
            
            try:
                customer = stripe.Charge.create(
                    amount = int(total * 100), 
                    currency = "EUR",
                    description = request.user.email,
                    card = payment_form.cleaned_data["stripe_id"],
                )
            except stripe.error.CardError:
                messages.error(request, "Your card has been declined.")
                
            if customer.paid:
                # If customer paid, loop over the products they bought, and append them to adopted
                user = get_object_or_404(User, username=request.user)
                products = OrderLineItem.objects.filter(order=order)
                for animal_product in products:
                    if animal_product.product.name not in user.profile.adopted:
                        user.profile.adopted.append(animal_product.product.name)
                    elif not user.profile.adopted:
                        user.profile.adopted = [animal_product.product.name]
                
                # If length of adopted is greater than or equal to a certain number, they will recieve a new rank
                if len(user.profile.adopted) == 1:
                    user.profile.rank = "Adopter"
                elif len(user.profile.adopted) >= 3 and len(user.profile.adopted) < 5:
                    user.profile.rank = "Hero"
                elif len(user.profile.adopted) >= 5 and len(user.profile.adopted) < 10:
                    user.profile.rank = "Legend"
                elif len(user.profile.adopted) >= 10:
                    user.profile.rnak = "Saviour"
                    
                user.profile.save()
                messages.error(request, "You have successfuly paid. Thank you for your generosity!")
                request.session["cart"] = {}
                return redirect(reverse("all_animals"))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(request, "We were unable to take a payment with that card.")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()
    
    return render(request, "checkout.html", { "order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE })