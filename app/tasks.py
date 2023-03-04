from app.models import Invoker
from Newsite.celd import app


# @app.task
# def invoke_invoker():
#     Invoker.objects.create()
#     return "Hi"


@app.task
def invoke_invoker1():
    Invoker.objects.create(title='New')
    return "Hi"