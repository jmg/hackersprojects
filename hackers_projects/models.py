from django.db import models
from hackers_projects.utils.date import get_time_since


class BaseModel(models.Model):

    def object_age(self):
        return get_time_since(self.submited)

    class Meta:
        abstract = True


class Profile(BaseModel):

    username = models.CharField(max_length=300)
    email = models.CharField(max_length=300, null=True, blank=True)
    remote_id = models.CharField(max_length=300)
    url = models.CharField(max_length=300, null=True, blank=True)
    access_token = models.CharField(max_length=300, blank=True, null=True)

    imported_repos = models.BooleanField(default=False)


class Repository(BaseModel):

    name = models.CharField(max_length=300, null=True, blank=True)
    url = models.CharField(max_length=300, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    remote_id = models.CharField(max_length=300)
    shared = models.BooleanField(default=False)

    user = models.ForeignKey("Profile")


class Project(BaseModel):

    submited = models.DateTimeField()
    votes = models.PositiveIntegerField(default=0)

    repository = models.ForeignKey("Repository")
    user = models.ForeignKey("Profile")

    voted_by = models.ManyToManyField("Profile", related_name="votes")


class Comment(BaseModel):

    content = models.TextField()
    project = models.ForeignKey("Project")
    submited = models.DateTimeField(null=True)

    user = models.ForeignKey("Profile", null=True)