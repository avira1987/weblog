from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=30)
    text = models.TextField(blank=True)
    is_enable = models.BooleanField(default=False)
    publish_date = models.DateTimeField(blank=True, null=True)
    create_time=models.DateTimeField(auto_now_add=True)
    update_timne = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return '{} - {}'.format(self.pk, self.title)

class Comment(models.Model):
    #یعنی یک کامنتی که میزاری به یکی از پست ها وصلش کن
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_timne = models.DateTimeField(auto_now=True)


