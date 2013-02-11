from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Comment(models.Model):
    post       = models.ForeignKey(Post, related_name='comments')
    body       = models.TextField(blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created comments')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='updated comments')

    def __unicode__(self):
        return "{0} {1} {2} {3}".format(self.post.subject, self.body, self.created_on, self.updated_on)
