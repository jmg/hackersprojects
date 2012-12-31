from base import BaseService
from hackers_projects.models import Comment


class CommentService(BaseService):

    entity = Comment