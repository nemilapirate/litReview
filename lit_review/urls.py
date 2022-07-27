from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from authentication.views import LoginView, SignupView, logout_user
from flux.views import flux, user_post
from ticket.views import CreateTicket, UpdateTicket, DeleteTicket
from review.views import review_create_view, review_create_view_answer_ticket, delete_review_view, update_review_view
from user.views import follow_view, unfollow_view


urlpatterns = [
                path('admin/', admin.site.urls),
                path('', LoginView.as_view(), name='login'),
                path('signup/', SignupView.as_view(), name='signup'),
                path('logout/', logout_user, name='logout'),

                path('flux/', flux, name='flux'),
                path('post/', user_post, name='post'),

                path('create_ticket/', CreateTicket.as_view(), name='create_ticket'),
                path('update_ticket<int:pk>/', UpdateTicket.as_view(), name='update_ticket'),
                path('delete_ticket<int:pk>', DeleteTicket.as_view(), name="delete_ticket"),

                path('create_review/', review_create_view, name='create_review'),
                path('create_review_answer_ticket/<int:ticket_id>/', review_create_view_answer_ticket,
                     name='create_review_answer_ticket'),
                path('update_review/<int:review_id>/', update_review_view, name='update_review'),
                path('delete_review/<int:review_id>/', delete_review_view, name="delete_review"),

                path('follow/', follow_view, name='follow'),
                path('unfollow/', unfollow_view, name='unfollow'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL,
                                                                                           document_root=settings.MEDIA_ROOT)
