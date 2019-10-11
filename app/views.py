from django.shortcuts import render, get_object_or_404, redirect
from .models import SettingPlanner


def settings(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        return render(request, 'detail.html', {'my_settings': data})
    else:
        return render(request, 'settings.html')
