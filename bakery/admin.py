from django.contrib import admin
from .models import BreadCategories, BreadProduct, BreadPost, CustomerInfo, CustomerMessage

admin.site.register(BreadCategories)
admin.site.register(BreadProduct)
admin.site.register(BreadPost)
admin.site.register(CustomerInfo)
admin.site.register(CustomerMessage)
