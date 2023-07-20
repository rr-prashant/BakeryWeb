import re
from django.shortcuts import redirect, render
from bakery_app.models import IntroSlider, about, accessories, Banner, cakeOnSale, cakes, contact_info, contact_us
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import phone
from bakery_main import settings
from django.core.mail import send_mail, EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from . token import generate_token

# View for registration and login
def registration(request):
    
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        
        if User.objects.filter(email=email).exists() and User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username and Email already exists'})

        elif User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists'})
        
        elif User.objects.filter(email=email).exists():
            return render(request, 'register.html', {'error': 'Email already exists'})
        elif len(username)>10:
            return render(request, 'register.html', {'error': 'Username must be under 10 characters'})
        elif pass1 != pass2:
            return render(request, 'register.html', {"error': 'Password didn't match"})
        else:
            myuser = User.objects.create_user(username=username, email=email, password=pass1)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_active = False
            
            myuser.save()
            messages.success(request, "Your account has been successfully created. We have sent you a confirmation email, please confirm your email inorder to activate your account.")
            
            
            # Welcome email
            
            subject = "Welcome to Sweet Wave Bakery"
            message = "Hello " + myuser.first_name + "!! \n" + "Welcome to Sweet Wave Bakery!! \nThank you for visiting our website \nWe have sent you a confirmation email, please confirm your email address in order to activate your account. \n\n Thank you \n Team Sweet Wave "
            from_email = settings.EMAIL_HOST_USER
            to_list = [myuser.email]
            send_mail(subject, message, from_email, to_list, fail_silently=True)
            
            
            # Email address confirmation
            
            current_site = get_current_site(request)
            email_subject = "Confirm your email @ Sweet Wave Bakery!!"
            message2 = render_to_string('emailconfirmation/email_confirmation.html', {
                'name': myuser.first_name,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
                'token': generate_token.make_token(myuser),
                
            })
            email = EmailMessage(
                email_subject,
                message2,
                settings.EMAIL_HOST_USER,
                [myuser.email],
            )
            email.fail_silently = True
            email.send()
            
            return redirect('login')
        
        
            
    
    return render(request, 'register.html', locals())


def signin(request):
    
    if request.method == "POST":
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            user=request.user
            return redirect('home')
        else:    
            return render(request, 'login.html', {'error': 'Username or Password incorrect!'})
            
            
    return render(request, 'login.html')



def main(request):
    return render(request, 'mainLayout.html')
    
def profile(request):
    
    if request.user.is_authenticated:
        try:
            phone_obj = phone.objects.get(user=request.user)
            phone_num = phone_obj.phone_number
            
            return render(request, 'profile.html', {'phn': phone_num})
        except phone.DoesNotExist:
            if request.method == 'POST':
                user = request.user
                phn = request.POST.get('phone')  # Get the phone number from the form

        # Validate the phone number using a regular expression
                phone_pattern = r'^(98|97)\d{8}$'
                if not re.match(phone_pattern, phn):
            # Phone number is invalid, handle the error (e.g., show an error message)
                    return render(request, 'profile.html', {'error_message': 'Invalid phone number'})

        # Phone number is valid, save it to the Phone model
                phone_obj, created = phone.objects.get_or_create(user=user)
                phone_obj.phone_number = phn
                phone_obj.save()

                return redirect('profile')  # Redirect to the profile page or any other page
    else:
        # If the user is not logged in, set phone_num to None
        phone_num = None
        
    

    return render(request, 'profile.html')

def signout(request):
    logout(request)
    return redirect('home')


# View for all the pages
def index(request):
    slider = IntroSlider.objects.all()
    banner = Banner.objects.all()
    featured_cake = cakes.objects.filter(is_featured=True).order_by('-id')
    

        
    return render(request, 'index.html', {'slide': slider, 'ban': banner, 'fcake': featured_cake})

def cake(request):
    cke = cakes.objects.all()
    return render(request, 'product.html', locals())

def cakes_details(request, cakeslug):
    cke = cakes.objects.filter(slug=cakeslug)
    return render(request, 'product-detail.html', {'ck': cke})

def accessory_model(request):
    accessory = accessories.objects.all()
    return render(request, 'accessories.html', locals())

def acc_details(request, accslug):
    accessory = accessories.objects.filter(slug=accslug)
    return render(request, 'accessories-detail.html', {'acc': accessory})

def sales(request):
    sl = cakeOnSale.objects.all()
    return render(request, 'sale.html', locals())

def sale_details(request, saleslug):
    sl = cakeOnSale.objects.filter(slug=saleslug)
    return render(request, 'sale-details.html', {'sle': sl})


def contacts(request):
    cnct = contact_info.objects.all()
    
    if request.method=="POST":
        email = request.POST['email']
        msg = request.POST['msg']
        
        cnt = contact_us(client_email=email, client_message=msg)
        cnt.save()
        return redirect('contact')
    
    return render(request, 'contact.html', locals())

def abouts(request):
    abt = about.objects.all()
    return render(request, 'about.html', locals())

def cart(request):
    return render(request, 'shoping-cart.html', locals())

def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None
    
    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        myuser.save()
        login(request, myuser)
        return redirect('home')
    else:
        return render(request, 'emailconfirmation/activation_failed.html')