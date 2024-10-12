from django.urls import path
from .views import index, root_link, add_link

urlpatterns = [
    path('', index, name='home'),
    path('create/', add_link, name='create-link'),  # URL for creating a new link
    path('<slug:link_slug>/', root_link, name='root-link'),  # URL for root redirection
]
