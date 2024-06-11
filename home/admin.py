from django.contrib import admin
from django.contrib.admin.sites import site

# Register your models here.
from .models import TeamMember , UserProfile ,Internship

# To display titles/parameters in admin panel...
class TeamMemberAdmin(admin.ModelAdmin):
    list_display=('link','image','title','subtitle','location')

admin.site.register(TeamMember,TeamMemberAdmin)

class UserProfiledb(admin.ModelAdmin):
    list_display=('first_name','last_name','email','phone','password')

admin.site.register(UserProfile,UserProfiledb)

class Internshipdb(admin.ModelAdmin):
    list_display=('category','title','image','link')

admin.site.register(Internship,Internshipdb)

