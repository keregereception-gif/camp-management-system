from django.contrib import admin
from .models import Company, Block, Room, Employee, Accommodation

admin.site.register(Company)
admin.site.register(Block)
admin.site.register(Room)
admin.site.register(Employee)
admin.site.register(Accommodation)

# Register your models here.
