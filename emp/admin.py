from django.contrib import admin

from .models import Emp,Testimonial
# Register your models here.


class showEmployeeData(admin.ModelAdmin):
    list_display=("name","working","address","phone","emp_id","department")
    list_editable=("name","working","address","phone","emp_id","department")
    list_display_links = None 
    search_fields=('name',)
    list_filter=('working',);   
 
admin.site.register(Emp,showEmployeeData)
admin.site.register(Testimonial)

