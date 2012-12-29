from base import BaseView
from hackers_projects.services.project import ProjectService, TrendingProjectService


class TrendingView(BaseView):

    url = r"^trending$"

    def get(self, *args, **kwargs):

        return self.render_to_response({"projects": TrendingProjectService().get_page()})


class NewView(BaseView):

    url = r"^new$"

    def get(self, *args, **kwargs):

        return self.render_to_response({"projects": ProjectService().get_page()})