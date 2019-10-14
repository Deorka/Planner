from calendar import monthrange

from django.shortcuts import render, get_object_or_404, redirect
from .models import SettingPlanner

month_mapping = {1: "Января", 2: "Февраля", 3: "Марта", 4: "Апреля", 5: "Мая", 6: "Июня", 7: "Июля", 8: "Августа",
                 9: "Сентября", 10: "Октября", 11: "Ноября", 12: "Декабря"}


# week_mapping = {1: "Понедельник", 2: "Вторник", 3: "Среда", 4: "Четверг", 5: "Пятница", 6: "Суббота", 7: "Воскресенье"}


def settings(request):
    if request.method == "POST":
        data = request.POST
        print(data)
        days = {}
        if data["year"]:
            for month in range(11):
                days[month + 1] = [str(monthrange(int(data["year"]), month + 1)[1]), month_mapping[month + 1]]

        return render(request, 'detail.html', {'my_settings': data, 'days': days})
    else:
        return render(request, 'settings.html')
