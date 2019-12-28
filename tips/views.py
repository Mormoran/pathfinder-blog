import stripe
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required(login_url='/accounts/login')
def tips(request):
    stripe_key = settings.STRIPE_PUBLISHABLE_KEY

    tip_amounts = [
        {"stripe_amount": 150, "display_amount": "1.50", "description": "candy bar"},
        {"stripe_amount": 350, "display_amount": "3.50", "description": "coffee"},
        {"stripe_amount": 1200, "display_amount": "12.00", "description": "movie ticket"},
        {"stripe_amount": 1550, "display_amount": "15.00", "description": "ramen bowl"},
        {"stripe_amount": 25600000, "display_amount": "256,000.00", "description": "Ferrari"},
    ]

    args = {'stripe_key': stripe_key, 'tip_amounts': tip_amounts}

    if request.method == 'POST':
        try:
            charge = stripe.Charge.create(
                amount=request.POST['stripe_amount'],
                currency='eur',
                description=request.POST['description'],
                source=request.POST['stripeToken']
            )
        except (stripe.error.CardError):
            messages.error(request, "Your card was declined!")
            return render(request, 'tips.html', args)

        if charge.paid:
            messages.success(request, "Your tip has been successfully processed! Thank you very much for supporting the site. We hope to bring you many more useful tools in the near future!")
        return render(request, 'tips.html', args)
    else:
        return render(request, 'tips.html', args)
