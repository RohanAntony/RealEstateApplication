from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='listings'),    #root path
    path('<int:listing_id>', views.listing, name='listing'),  # root path
    path('search', views.search, name='search'),  # search
]