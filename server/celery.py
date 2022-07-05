# # from celery.schdules import crontab
# import os
# from celery import Celery

# os.environ.setdefault('DJANGO_SETTINGS_MODULE','core.settings')
# app = Celey('core')

# app = Celery('core')
# app.config_from_object('django.conf:settings',namespace ='CELERY')
# app.authodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Hello from celery')
    

# app.conf.beat_schedule = {
#     'send-mail-every-day-at-8pm' : {
#         'task' : 'send_mail_app.task',
#         'schedule': crontab(hour=8,minute=0),
        
#     }

# }
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')

# app = Celery('demo_project', backend='redis://localhost', broker='pyamqp://')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))

# from __future__ import absolute_import, unicode_literals
# from celery import Celery
# from decouple import config
# import django
# import os

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo_project.settings')

# app = Celery('demo_project', backend='redis://localhost', broker='pyamqp://')





# # Using a string here means the worker doesn't have to serialize
# # the configuration object to child processes.
# # - namespace='CELERY' means all celery-related configuration keys
# #   should have a `CELERY_` prefix.
# app.config_from_object('django.conf:settings', namespace='CELERY')

# # Load task modules from all registered Django app configs.
# app.autodiscover_tasks()

# @app.task(bind=True)
# def debug_task(self):
#     print('Request: {0!r}'.format(self.request))