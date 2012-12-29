from django.db import models


class Profile(models.Model):

    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300)    
    remote_id = models.CharField(max_length=300)
    access_token = models.CharField(max_length=300, blank=True, null=True)

    imported_repos = models.BooleanField(default=False)


class Repository(models.Model):

    name = models.CharField(max_length=300)
    url = models.CharField(max_length=300)
    description = models.TextField()

    remote_id = models.CharField(max_length=300)
    shared = models.BooleanField(default=False)

    user = models.ForeignKey("Profile")


class Project(models.Model):

    submited = models.DateTimeField()
    votes = models.PositiveIntegerField(default=0)

    repository = models.ForeignKey("Repository")
    user = models.ForeignKey("Profile")

    voted_by = models.ManyToManyField("Profile", related_name="votes")


class Comment(models.Model):

    content = models.TextField()
    project = models.ForeignKey("Project")