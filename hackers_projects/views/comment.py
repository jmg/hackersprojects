from datetime import datetime

from base import BaseView
from hackers_projects.services.comment import CommentService


class NewView(BaseView):

    template_name = "project/_comment.html"

    def post(self, *args, **kwargs):

        project = self.request.POST.get("project")
        content = self.request.POST.get("comment")

        comment = CommentService().new(content=content, project_id=project, submited=datetime.utcnow(), user=self.get_user())
        comment.save()

        return self.render_to_response({"comment": comment })