from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse

import stripe
stripe.api_key = "sk_test_51MGPnmACvCGI7S3SBwCXuloJOBWIjNjdofkucSbG7z1OTxOEGTBRvUpdlVsiaAUlsypVDa8eekpNAxMDwTiFbbC600SeA38J2W"

# Create your views here.

def index(request):
	return render(request, 'base/index.html')


def charge(request):
	if request.method == 'POST':
		print('Data:', request.POST)

		amount = int(request.POST['amount'])

		customer = stripe.Customer.create(
			email=request.POST['email'],
			name=request.POST['username'],
			source=request.POST['stripeToken']
		)

		charge = stripe.Charge.create(
			customer=customer,
			amount=amount*100,
			currency='eur',
			description='Payment'
		)

	return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
	amount = args
	return render(request, 'base/success.html', {'amount':amount})