from django.contrib import admin

# Register your models here.
from .models import Review
class ReveiwAdmin(admin.ModelAdmin):
    list_display = ('user', 'product', )

admin.site.register(Review, ReveiwAdmin)