from django.contrib import admin
from .models import Product
from .models import VolumeType
from .models import Comment

# Register your models here.
admin.site.register(Product)
admin.site.register(VolumeType)
admin.site.register(Comment)

