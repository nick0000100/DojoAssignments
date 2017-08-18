# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from ..login_app.models import User

# Create your models here.

class CommentManager(models.Manager):
    def newComment(self, postData, user):
        comment = postData["comment"]
        Comment.objects.create(content = comment,
                                user = user
        )

class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, related_name = "comments")
    objects = CommentManager()