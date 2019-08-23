from django.shortcuts import get_object_or_404, render

from users.models import User


def profile(request, username):
    user = get_object_or_404(User, username=username)

    return render(
        request,
        'profile.html',
        context={'user': user}
    )
