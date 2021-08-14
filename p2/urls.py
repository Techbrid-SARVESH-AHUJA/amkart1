"""p2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.index, name="index"),
    
    path('contact/', views.contact, name="contact"),
    
    path('products/', views.products, name="products"),
    
    path('cart/', views.cart, name="cart"),
    
    path('shipping_rates/', views.shipping_rates, name="shipping_rates"),
    
    path('login/', views.login, name="login"),
    
    path('signup/', views.signup, name="signup"),

    path('mobile_phones/<str:pk_prod>/', views.mobile_phones, name="mobile_phones"),
    
    path('lego_models/<str:pk_prod>/', views.lego_models, name="lego_models"),
    
    path('bedsheets/<str:pk_prod>/', views.bedsheets, name="bedsheets"),
    
    path('clocks/<str:pk_prod>/', views.clocks, name="clocks"),

    path('blog/', views.blog, name="blog"),

    path('checkout/', views.checkout, name="checkout"),

    path('preview/', views.preview, name="preview"),
    
    path('logout/', views.logout, name="logout"),


    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)