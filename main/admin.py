from django.contrib import admin
from .models import Link, BlogPost, TeamMember, Page, Author, Category, Offer
# Register your models here.

class OfferAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'order')  # Assuming 'order' is the field for ordering


class PageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'page')  # Assuming 'name' is the field for the page name

admin.site.register(Link)
admin.site.register(BlogPost)
admin.site.register(TeamMember)
admin.site.register(Page, PageAdmin)
admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Offer, OfferAdmin)