from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model

user = get_user_model()



# Create your models here.

STATUS_CHOICES = [('draft','Draft'),('published','Published')]

class Post (models.Model):

    title           = models.CharField(max_length=264)
    slug            = models.SlugField(max_length=264,unique_for_date='publish')
    author          = models.ForeignKey(User,related_name='blog_posts')
    content         = models.TextField()
    publish         = models.DateTimeField(auto_now=False,default=timezone.now)
    created         = models.DateTimeField(auto_now_add=True)
    updated         = models.DateTimeField(auto_now=True)
    status          = models.CharField(max_length=50,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering = ('-publish',)

        verbose_name = 'Blog Post'
        #verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title;

    def get_absolute_url(self):
        return reverse('blog:detail',args=[self.id])
        #return reverse('blog:detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

    def get_absolute_urlx(self):
        return reverse('blog:detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

    # def get_absolute_url(self):
    #     return reverse('post_detail',args=[self.publish.year,self.publish.strftime('%m'),self.publish.strftime('%d'),self.slug])

class Likes(models.Model):
    post = models.ForeignKey(Post)
    like = models.NullBooleanField(null=True,blank=True)
    liked_by = models.ForeignKey(user)
