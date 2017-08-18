# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class CourseManager(models.Manager):
    def validate(self, postData):
        errors = {}
        name = postData['name']
        desc = postData['desc']
        if len(name) < 10:
            errors["name"] = "Name of course must be more than 10 characters long."
        if len(desc) < 15:
            errors["desc"] = "Description must be more than 15 characters long."
        return errors
    def createCourse(self, postData):
        name = postData['name']
        desc = postData['desc']
        newCourse = Course.objects.create(name=name)
        newDesc = Description.objects.create(content = desc, course = newCourse)
        return self

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = CourseManager()

class Description(models.Model):
    content = models.TextField()
    course = models.ForeignKey(Course, related_name = "descriptions")
    objects = CourseManager()

# class Comment(models.Model):
#     content = models.TextField()
#     course = models.ForeignKey(Course, related_name = "course")