from django.contrib import admin
from .models import Person, Tweet
# Register your models here.


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'birth', 'is_active')

# admin.site.register(Person, PersonAdmin)

@admin.register(Tweet)
class TweetAdmin(admin.ModelAdmin):
    list_display = ('author','message','created_at','modified_at')