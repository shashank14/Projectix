from django.contrib import admin
from .models import Post
from .models import Likes

# Register your models here.


class PostAdmin(admin.ModelAdmin):

    list_display = ['title','author','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','author','created','publish')
    search_fields=('title','content')
    raw_id_fields=('author',)


    class Meta:
        model = Post


admin.site.register(Post,PostAdmin)
admin.site.register(Likes)
