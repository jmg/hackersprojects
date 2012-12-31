from base import BaseView
from hackers_projects.services.project import ProjectService, TrendingProjectService
from hackers_projects.services.github import GitHubService


class BaseProjectsView(BaseView):

    def get(self, *args, **kwargs):

        page = self.request.GET.get("page", 0)

        context = {}
        projects = self.service.get_page(page=page)
        context["projects"] = projects
        context["view_name"] = self.view_name
        context["next_page"] = int(page) + 1

        context["GITHUB_AUHT_URL"] = GitHubService().get_auth_url()

        return self.render_to_response(context)


class TrendingView(BaseProjectsView):

    service = TrendingProjectService()
    view_name = "trending"
    url = r"^{0}/$".format(view_name)


class NewView(BaseProjectsView):

    service = ProjectService()
    view_name = "new"
    url = r"^{0}/$".format(view_name)


class Comments(BaseView):

    url = r"^projects/(?P<project_id>\d+)/comments/$"

    def get(self, *args, **kwargs):

        context = {}

        project = ProjectService().get(id=self.kwargs["project_id"])
        context["project"] = project
        context["comments"] = project.comment_set.all()

        return self.render_to_response(context)