import requests
from hackersprojects.settings import GITHUB_CLIENT_ID, GITHUB_SECRET_KEY, GITHUB_REDIRECT_URI
from urllib import urlencode
from urlparse import parse_qs
import simplejson as json


class GitHubService(object):    

    def get_auth_url(self):

        base_url = "https://github.com/login/oauth/authorize"

        params = {
            "client_id": GITHUB_CLIENT_ID,
            "redirect_uri": GITHUB_REDIRECT_URI,
        }

        return "{0}/?{1}".format(base_url, urlencode(params))

    def get_access_token(self, code):

        url = "https://github.com/login/oauth/access_token"

        params = {
            "client_id": GITHUB_CLIENT_ID,
            "client_secret": GITHUB_SECRET_KEY,
            "code": code,
            "redirect_uri": GITHUB_REDIRECT_URI,   
        }

        response = requests.post(url, params=params)

        data = parse_qs(response.text)
        return data["access_token"]

    def api_method(self, path, params):

        url = "https://api.github.com/{0}".format(path)

        response = requests.get(url, params=params)
        return json.loads(response.text)

    def get_repos(self, token):

        params = {
            "type": "public",
            "access_token": token,
        }        

        return self.api_method("user/repos", params)

    def get_user(self, token):

        params = {
            "access_token": token,
        }

        return self.api_method("user", params)