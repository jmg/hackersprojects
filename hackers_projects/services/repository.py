from base import BaseService
from hackers_projects.models import Repository


class RepositoryService(BaseService):

    entity = Repository
    
    def save_repos(self, profile, repos):

        repositories = []

        for repo in repos:

            repository = self.get_or_new(remote_id=repo["id"])

            data = {
                "name": repo["name"],
                "url": repo["html_url"],
                "description": repo["description"],
                "user": profile,
            }

            for key, value in data.iteritems():
                setattr(repository, key, value)

            repository.save()

            repositories.append(repository)

        return repositories