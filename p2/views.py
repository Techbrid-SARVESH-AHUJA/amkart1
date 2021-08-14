from app.decorators import verification
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app.models import *
from app.forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as logi, logout as logo
from django.contrib import messages
from app.decorators import *
from django.contrib.auth.decorators import login_required



def index(request):
    Slides=slider.objects.all()
    Categories=categorie.objects.all()
    Details=company.objects.all()
    context={"Slides": Slides, "Categories": Categories, "Details": Details}
    return render(request, "helo/index.html", context)


@login_required(login_url="login")
def contact(request):
    form=contact_us_form
    if request.method=='POST':
        form=contact_us_form(request.POST)
        if form.is_valid:
            form.save()
    Details=company.objects.all()
    context={"Details": Details, "form": form}
    return render(request, 'helo/contact.html', context)


@login_required(login_url="login")
def products(request):
    Mobiles=mobile_phone.objects.all()
    Legos=lego_model.objects.all()
    Bedsheets=bedsheet.objects.all()
    Clocks=clock.objects.all()
    Details=company.objects.all()
    products={"Legos": Legos, "Mobiles": Mobiles, "Bedsheets": Bedsheets, "Clocks": Clocks, "Details": Details}
    return render(request, 'helo/products.html', products)


@login_required(login_url="login")
def cart(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/cart.html', context)


@login_required(login_url="login")
def shipping_rates(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/shipping_rates.html', context)


@verification
def login(request):
    if request.method=='POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request, username=username, password=password)
        if user is not None:
            logi(request, user)
            return redirect('index')
        else:
            messages.info(request, "invalid user")
            Details=company.objects.all()
            context={"Details": Details}
            return render(request, 'helo/login.html', context)
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/login.html', context)


@login_required(login_url="login")
def signup(request):
    form=signup_data()
    if request.method=='POST':
        form=signup_data(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    Details=company.objects.all()
    context={"Details": Details, "form": form}
    return render(request, 'helo/signup.html', context)


@login_required(login_url="login")
def mobile_phones(request, pk_prod):
    Product=mobile_phone.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/mobile_phones.html', context)


@login_required(login_url="login")
def lego_models(request, pk_prod):
    Product=lego_model.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/lego_models.html', context)


@login_required(login_url="login")
def bedsheets(request, pk_prod):
    Product=bedsheet.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/bedsheets.html', context)


@login_required(login_url="login")
def clocks(request, pk_prod):
    Product=clock.objects.get(id=pk_prod)
    Details=company.objects.all()
    context={"Product": Product, "Details": Details}
    return render(request, 'helo/clocks.html', context)



@login_required(login_url="login")
def checkout(request):
    form=checkout_details
    if request.method=='POST':
        form=checkout_details(request.POST)
        if form.is_valid():
            form.save()
            return redirect('preview')
    Details=company.objects.all()
    context={"Details": Details, "form": form}
    return render(request, 'helo/checkout.html', context)


@login_required(login_url="login")
def blog(request):
    form=add_blog_data
    if request.method=='POST':
        form=add_blog_data(request.POST)
        if form.is_valid:
            form.save()
    blogs=blog_data.objects.all()
    Details=company.objects.all()
    context={"Details": Details, "blogs": blogs, "form": form}
    return render(request, 'helo/blog.html', context)




@login_required(login_url="login")
def preview(request):
    Details=company.objects.all()
    context={"Details": Details}
    return render(request, 'helo/preview.html', context)


def logout(request):
    logo(request)
    return redirect('index')