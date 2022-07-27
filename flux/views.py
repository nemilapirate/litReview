from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from review.models import Review
from ticket.models import Ticket


@login_required
def flux(request):
    return render(request, "flux/flux.html")


@login_required
def user_post(request):
    html = "flux/post.html"
    current_user = request.user
    context = {
        "review": Review.objects.filter(user=current_user),
        "ticket": Ticket.objects.filter(user=current_user)
    }
    return render(request, html, context)


