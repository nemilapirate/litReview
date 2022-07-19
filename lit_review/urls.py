"""lit_review URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import LoginView, SignupView, logout_user
from flux.views import flux
from ticket.views import CreateTicket, UpdateTicket, DeleteTicket
from review.views import review_create_view, review_create_view_with_ticket, delete_review_view, update_review_view
urlpatterns = [
                path('admin/', admin.site.urls),
                path('', LoginView.as_view(), name='login'),
                path('signup/', SignupView.as_view(), name='signup'),
                path('logout/', logout_user, name='logout'),

                path('flux/', flux, name='flux'),

                path('create_ticket/', CreateTicket.as_view(), name='create_ticket'),
                path('update_ticket<int:pk>/', UpdateTicket.as_view(), name='update_ticket'),
                path('delete_ticket<int:pk>', DeleteTicket.as_view(), name="delete_ticket"),

                path('create_review/', review_create_view, name='create_review'),
                path('create_review_with_ticket/<int:ticket_id>/', review_create_view_with_ticket,
                     name='create_review_with_ticket'),
                path('update_review/<int:review_id>/', update_review_view, name='update_review'),
                path('delete/<int:review_id>/', delete_review_view, name="delete_review"),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
