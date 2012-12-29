from base import BaseView
from hackers_projects.services.github import GitHubService


class IndexView(BaseView):

    url = r"^$"

    def get(self, *args, **kwargs):

        context = {}
        context["GITHUB_AUHT_URL"] = GitHubService().get_auth_url()

        return self.render_to_response(context)


class AboutView(BaseView):

    url = r"^about$"

