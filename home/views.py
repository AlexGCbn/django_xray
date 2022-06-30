from django.shortcuts import render


def home_view(request):
    """Basic home view"""
    return render(request, 'home/home.html')
