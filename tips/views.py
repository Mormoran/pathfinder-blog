from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required


@login_required(login_url='/accounts/login')
def tips(request):
    return render(request, 'tips.html')

# customer_id = request.user.profile.stripe_id

# if request.method == 'POST':
#     try:
#         gig = Gig.objects.get(id=request.POST.get('gig_id'))
#     except Gig.DoesNotExist:
#         return redirect('/')


#     token = request.POST['stripeToken']

#     # Create a charge: this will charge the user's card
#     try:
#         customer = stripe.Customer.retrieve(customer_id)
#         customer.sources.create(source=token)

#         destination_id = gig.user.socialaccount_set.get().uid 

#         charge = stripe.Charge.create(
#             amount=5000,  # Amount in cents
#             currency="chf",
#             customer=customer,
#             description=gig.title,
#             application_fee=123,
#             destination=destination_id, #'acct_**************'
#         )

#     except stripe.error.CardError as e:
#         # The card has been declined
#         pass