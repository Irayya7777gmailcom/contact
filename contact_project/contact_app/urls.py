from django.urls import path
from .views import contact_list, add_contact
from . import views
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('',views.login,name='login'),
    path('logout',views.logout_view,name='logout'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('contacts/', views.contact_list, name='contact_list'),
    path('contacts/add/', views.add_contact, name='add_contact'),
    path('advance_search',views.advance_search,name='search')
]
