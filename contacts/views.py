from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail

from .models import Contacts


def contact(request):
    if request.method == 'POST':
        print(request.POST)
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        # Check if inquiry already made
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contacts.objects.all().filter(listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already enquired about this property')
                return redirect('/listings/'+listing_id)

        contact = Contacts(listing=listing, listing_id=listing_id, name=name, email=email, phone=phone, message=message, user_id=user_id)

        contact.save()
#        send_mail(subject="Property listing inquiry", message="There has been an inquiry for " + listing + ". Sign into the admin panel for more info.",
#                  from_email="rohan271995@gmail.com", recipient_list=[realtor_email], fail_silently=False)

        messages.success(request, 'Your request has been submitted!')
        return redirect('/listings/'+listing_id)