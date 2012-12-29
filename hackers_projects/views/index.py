from base import BaseView
from hackers_projects.services.github import GitHubService
from hackers_projects.services.project import TrendingProjectService


class IndexView(BaseView):

    url = r"^$"

    def get(self, *args, **kwargs):

        context = {}
        context["GITHUB_AUHT_URL"] = GitHubService().get_auth_url()

        trendings = TrendingProjectService().get_page(size=6)
        context["projects_columns"] = [trendings[0:3], trendings[3:6]]

        return self.render_to_response(context)


class AboutView(BaseView):

    url = r"^about$"

