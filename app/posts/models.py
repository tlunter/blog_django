from django.db import models
from django.contrib.auth.models import User
from posts.exceptions import IsNotStaffException

class PostManager(models.Manager):
    def create_post(self, user, subject, body):
        if not user.is_staff:
            raise IsNotStaffException

        post = self.model(created_by=user, updated_by=user, subject=subject, body=body)
        post.save()
        return post


class Post(models.Model):
    subject    = models.CharField(max_length=255, default='No subject')
    body       = models.TextField(default='No body')
    visible    = models.BooleanField(default=True)
    created_on = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='created posts')
    updated_on = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, related_name='updated posts')

    objects    = PostManager()

    def __unicode__(self):
        return "{0} {1} {2}".format(self.subject, self.created_on, self.updated_on)
