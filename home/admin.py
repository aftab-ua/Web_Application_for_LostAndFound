from django.contrib import admin
from .models import Reward, YoutubeVideo

# Register your models here.

admin.site.register(Reward)


class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ['title',  'video', 'timestamp']

    class Meta:
        model: YoutubeVideo


admin.site.register(YoutubeVideo, YoutubeVideoAdmin)