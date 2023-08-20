from celery import shared_task

@shared_task()
def add(x, y):
    print("Adding %s + %s" % (x, y))
    return x + y

@shared_task
def hello_world():
    add.delay(1, 2)
    print("Hello World Task Executed!")