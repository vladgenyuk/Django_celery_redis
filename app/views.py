from django.shortcuts import render

from app.tasks import invoke_invoker1


def home(request):
    # invoke_invoker1.delay()
    return render(request, 'app/home.html')
