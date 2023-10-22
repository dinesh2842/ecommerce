from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)

'''This admin.py is used to store all the tables in the adminsite'''
'''If we forget to register here it wont show in our adminsite'''
'''This admin site is customized using Jazzmin'''