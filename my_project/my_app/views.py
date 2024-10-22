from django.http import HttpResponse
from datetime import datetime, timedelta

def index(request):
    current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return HttpResponse(f"Current date and time: {current_datetime}")

def multiplication_table(request):
    result = ''
    for i in range(1, 11):
        for j in range(1, 11):
            result += f'{i} * {j} = {i * j}\t\t'
        result += '\n'
    return HttpResponse(f"<pre>{result}</pre>")


def programmer_day(request):
    current_year = datetime.now().year
    programmer_day_date = datetime(current_year, 1, 1) + timedelta(days=255)  # 256-й день
    formatted_date = programmer_day_date.strftime('%Y-%m-%d')
    return HttpResponse(f"Programmer's Day: {formatted_date}")