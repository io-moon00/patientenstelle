from django.contrib import admin
from .models import Link, BlogPost, TeamMember, Page, Author, Category
# Register your models here.

admin.site.register(Link)
admin.site.register(BlogPost)
admin.site.register(TeamMember)
admin.site.register(Page)
admin.site.register(Author)
admin.site.register(Category)