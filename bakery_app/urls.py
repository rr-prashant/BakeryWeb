from django.urls import path

from bakery_app import views

urlpatterns = [
    path('', views.index, name='home'),
    path('main/', views.main, name='main'),
    path('cakes/', views.cake, name='cakes'),
    path('cakes/<slug:cakeslug>/', views.cakes_details, name='cake-details'),
    path('accessories/', views.accessory_model, name='accessories'),
    path('accessories/<slug:accslug>/', views.acc_details, name='acc-detail'),
    path('sale/', views.sales, name='sales'),
    path('sale/<slug:saleslug>', views.sale_details, name='sale-info'),
    path('contact/', views.contacts, name='contact'),
    path('about/', views.abouts, name='about'),
    path('cart/', views.cart, name='cart'),
    path('profile/', views.profile, name='profile'),
    
    # registration and login urls
    path('register/', views.registration, name='register'),
    path('login/', views.signin, name='login'),
    path('logout/', views.signout, name='logout'),
    
    
    # email activation url
    path('activate/<uidb64>/<token>', views.activate, name='activate'),
]
