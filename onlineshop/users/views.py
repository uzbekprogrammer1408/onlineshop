from traceback import print_tb
from django.shortcuts import render, redirect
from .forms import Login, Register, LoginForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponse

from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from products.models import Kitobjanri, Product
from django.shortcuts import get_list_or_404



def register(request):
    form_r = Register()
    if request.method == 'POST':
        form_r = Register(request.POST)

        if form_r.is_valid():
            user = form_r.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('acc_active.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form_r.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')

    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:18]

    
    context = {
        'form_r': form_r,
        "janrlar":janrlar,
        "products": products
    }
    return render(request, 'register.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('/')


##############################
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('/')
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()

    janrlar = Kitobjanri.objects.all()
    products = get_list_or_404(Product, status = True)[:18]

    
    context = {
        "form_l": form,
        "janrlar":janrlar,
        "products": products
    }
    return render(request, 'login.html', context=context)



def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')