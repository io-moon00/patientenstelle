from django.contrib import admin
from .models import Link, Newsletter, TeamMember, Page
# Register your models here.

admin.site.register(Link)
admin.site.register(Newsletter)
admin.site.register(TeamMember)
admin.site.register(Page)