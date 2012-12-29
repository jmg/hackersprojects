from base import BaseService
from hackers_projects.models import Project


class ProjectService(BaseService):

    entity = Project
    _page_size = 30

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-id")[offset:limit]


class TrendingProjectService(ProjectService):

    def _get_page_query(self, offset, limit, **kwargs):

        return self.order_by("-votes")[offset:limit]