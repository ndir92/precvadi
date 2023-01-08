from django.contrib import admin
from .models import Attendance, Course, DimAgroAssurance, DimAgroCulture, DimAgroFinance, DimAgroOrganisation, DimAgroProduction, DimAgroVarieteCultive, Post, Slider, Student, Students
# Register your models here.



admin.site.register(Post)
admin.site.register(DimAgroAssurance)
admin.site.register(DimAgroVarieteCultive)
admin.site.register(DimAgroProduction)
admin.site.register(DimAgroOrganisation)
admin.site.register(DimAgroFinance)
admin.site.register(DimAgroCulture)
admin.site.register(Student)
admin.site.register(Students)
admin.site.register(Attendance)
admin.site.register(Course)
class SliderAdmin(admin.ModelAdmin):
    list_displays='id' , 'image', 'title' 
admin.site.register(Slider)
