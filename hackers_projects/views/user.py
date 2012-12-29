from datetime import datetime

from base import BaseView
from hackers_projects.services.github import GitHubService
from hackers_projects.services.profile import ProfileService
from hackers_projects.services.repository import RepositoryService
from hackers_projects.services.project import ProjectService
from django.contrib.auth import logout, login, authenticate


class NewView(BaseView):

    def get(self, *args, **kwargs):

        token = GitHubService().get_access_token(code=self.request.GET.get("code"))
        user = GitHubService().get_user(token)

        profile = ProfileService().save_profile(user, token)

        self.set_user(profile)
        
        return self.redirect("/user/projects")


class ImportReposView(BaseView):

    def post(self, *args, **kwargs):

        profile = self.get_user()

        repos = GitHubService().get_repos(profile.access_token)
        repositories = RepositoryService().save_repos(profile, repos)

        profile.imported_repos = True
        profile.save()

        self.set_user(profile)

        return self.render_to_response({"repositories": repositories})


class ProjectsView(BaseView):

    def get(self, *args, **kwargs):

        context = {}

        profile = self.get_user()
        if profile.imported_repos:
            context["repositories"] = profile.repository_set.all()

        return self.render_to_response(context)
        

class ShareView(BaseView):

    def post(self, *args, **kwargs):

        repo = RepositoryService().get(id=self.request.POST.get("repo"))

        project = ProjectService().new(repository=repo, user=self.get_user(), submited=datetime.utcnow())
        project.save()

        repo.shared = True
        repo.save()

        return self.json_response({"status": "ok"})


class VoteView(BaseView):

    def post(self, *args, **kwargs):

        project = ProjectService().get(id=self.request.POST.get("project"))

        project.votes += 1
        project.voted_by.add(self.get_user())
        project.save()

        return self.json_response({"status": "ok", "votes": project.votes })