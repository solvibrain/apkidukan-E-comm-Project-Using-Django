from django.urls import path
from . import views
urlpatterns = [
    path('',views.index, name="shophome"),
    path('Contact',views.Contact, name="Contact"),
    path('Aboutus',views.Aboutus, name="Aboutus"),
    path('tracker',views.tracker, name="tracker"),
    path('productview',views.productview, name="productview"),
    path('search',views.search, name="search"),
    path('checkout',views.checkout, name="checkout")
    ]
