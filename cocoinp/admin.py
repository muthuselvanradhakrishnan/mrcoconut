from django.contrib import admin
from .models import Buyer


# Register your models here.
@admin.register(Buyer)
class AuthorAdmin(admin.ModelAdmin):
  list_display = ('date_required','name','address','mobile_number','qty_required')
  list_filter = ('date_required',)
