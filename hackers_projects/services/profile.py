from base import BaseService
from hackers_projects.models import Profile


class ProfileService(BaseService):

    entity = Profile

    def save_profile(self, user, token):

        profile = self.get_or_new(username=user.get("login"))
        profile.email = user.get("email")
        profile.url = user.get("html_url")
        profile.access_token = token
        profile.save()

        return profile