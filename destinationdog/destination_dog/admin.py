from django.contrib import admin
from destination_dog.models import Article, UserProfile, Dotm, Service, Event, Dog

class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}


admin.site.register(Article, ArticleAdmin)
admin.site.register(UserProfile)
admin.site.register(Dotm)
admin.site.register(Service)
admin.site.register(Event)
admin.site.register(Dog)
