from django.views.generic import TemplateView
from django.http import HttpResponseRedirect, HttpResponse
import simplejson as json


class BaseView(TemplateView):

    csrf_exempt = True

    def dispatch(self, request, *args, **kwargs):

        return TemplateView.dispatch(self, request, *args, **kwargs)

    def redirect(self, url):

        return HttpResponseRedirect(url)

    def response(self, response, headers={}):
        
        http_response = HttpResponse(response)

        for key, value in headers.iteritems():
            http_response[key] = value
            
        return http_response

    def response_error(self, response):

        return HttpResponseServerError(response)

    def json_response(self, response):

        return self.response(json.dumps(response))

    def json_loads(self, data):

        return json.loads(data)

    def json_dumps(self, data):

        return json.dumps(data)

    def render(self, template, context):

        return renderer.render(template, context)

    def render_string(self, string, context):

        return renderer.render_string(string, context)

    def get_list_args(self, startswith):

        return [key[len(startswith):] for key, value in self.request.POST.iteritems() if key.startswith(startswith)]

    def export(self, format, filename, content):

        response = HttpResponse(mimetype='text/%s' % format)
        response['Content-Disposition'] = 'attachment; filename=%s.%s' % (filename, format)
        Exporter().export(format, response, content)
        return response

    def get_params(self, data, params):

        dict_params = {}
        for param in params:
            dict_params[param] = data.get(param)
        return dict_params

    def set_user(self, user):

        self.request.session["user"] = user

    def get_user(self):

        return self.request.session.get("user")