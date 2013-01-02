from base import BaseService
from hackers_projects.models import Project

from django.contrib.contenttypes.models import ContentType


class ProjectService(BaseService):

    entity = Project
    _page_size = 30

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-id")[offset:limit]

    def new_from_repo(self, repo):

        project = self.get_or_new(repository=repo)
        project.user = repo.user
        project.save()

        return project


class TrendingProjectService(ProjectService):

    def _get_page_query(self, offset, limit, **kwargs):

        mysql_query = "SELECT COALESCE(votes / pow(TIMESTAMPDIFF(MINUTE, submited, UTC_TIMESTAMP()), 1.8), 0) FROM hackers_projects_project h WHERE hackers_projects_project.id = h.id"
        qs = self.extra(select={"score": mysql_query }).order_by("-score", "-submited")[offset:limit]
        return qs