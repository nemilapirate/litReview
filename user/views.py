from django.contrib.auth.models import User
from django.shortcuts import render, redirect,get_object_or_404

from user.forms import UserfollowForm, UnfollowForm
from user.models import Userfollows


# Create your views here.
def follow_view(request):
    if request.method == 'GET':
        form_follows = UserfollowForm
        html = 'user/user_follow.html'
        user_follows = Userfollows.objects.filter(user=request.user)
        followers = Userfollows.objects.filter(followed_user=request.user)
        context = {
            'form_follows': form_follows, 'user_follows': user_follows,
            'followers': followers,
        }
        return render(request, html, context)

    elif request.method == 'POST':
        form_follows = UserfollowForm(data=request.POST, files=request.POST)
        html = 'user/user_follow.html'
        context = {
            'form_follows': form_follows
        }
        if form_follows.is_valid():
            user = form_follows.cleaned_data['followed_user']
            current_user = request.user
            if user and user != current_user:
                relation_check = Userfollows.objects.filter(user=current_user) \
                    .filter(followed_user=user).first()
                if not relation_check:
                    new_follow = Userfollows(user=current_user,
                                             followed_user=user)
                    new_follow.save()
                    return redirect('follows')
        return render(request, html, context)


def unfollow_view(request):
    if request.method == 'POST':
        form_unfollow = UnfollowForm(data=request.POST)
        if form_unfollow.is_valid():
            followed_user_id = form_unfollow.cleaned_data['followed_user']
            followed_user = get_object_or_404(User, id=followed_user_id)
            user_follows = Userfollows.objects.filter(
                followed_user=followed_user).filter(user=request.user).first()
            if user_follows:
                user_follows.delete()
    return redirect('follows')