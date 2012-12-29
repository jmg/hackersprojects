# -*- coding: utf-8 -*-
from django.shortcuts import get_object_or_404


class BaseService(object):

    _repo = property(fget=lambda self: self.entity.objects)
    _page_size = 10

    default_query_params = {}

    def __getattr__(self, name):
        """
            Delegates all the undefined methods to the repository.
            The entity property must be overwritten in all the subclasses.
        """

        def decorator(*args, **kwargs):

            method = getattr(self._repo, name)
            return method(*args, **kwargs)

        return decorator

    def get_page(self, page=0, size=None, min_page=None, **kwargs):

        if size is None:
            size = self._page_size

        page = int(page)

        if min_page is not None:
            min_page = int(min_page)
            limit = (page + 1) * size
            offset = min_page * size
        else:
            limit = (page + 1) * size
            offset = size * page

        return self._get_objects(self._get_page_query(offset, limit, **kwargs))

    def _get_page_query(self, offset, limit, **kwargs):

        return self.all()[offset:limit]

    def list(self, start, size, **kwargs):
        page = int(start / size)
        return self.get_page(page=page, size=size, min_page=None, **kwargs)

    def _get_objects(self, objects):
        """ Override it to add behaviour """

        return objects

    def get_one(self, *args, **kwargs):

        objects = self.filter(*args, **kwargs)
        return objects[0] if objects else None

    def new(self, *args, **kwargs):

        return self.entity(*args, **kwargs)

    def _get_or_new(self, *args, **kwargs):

        try:
            obj, created = self.get_or_create(*args, **kwargs)
        except:
            obj, created = self.entity(*args, **kwargs), True
        return obj, created

    def get_or_new(self, *args, **kwargs):

        obj, _ = self._get_or_new(*args, **kwargs)
        return obj

    def get_or_new_created(self, *args, **kwargs):

        return self._get_or_new(*args, **kwargs)

    def get_form(self):

        return None

    def _get_data(self, request):

        data = dict([(key, value) for key, value in request.POST.iteritems() if key != "csrfmiddlewaretoken"])
        data.update(self._get_additional_data(request))
        return data

    def _get_additional_data(self, request):

        return {}

    def _get_entity(self, request):

        return self.get_or_new(**self._get_data(request))

    def _set_data(self, entity, request):

        data = self._get_data(request)
        for key, value in data.iteritems():
            setattr(entity, key, value)
        return entity

    def save_entity(self, entity):

        entity.save()

    def save(self, request):

        entity = self._get_entity(request)

        self._set_data(entity, request)
        self.save_entity(entity)
        self._post_save(entity, request)

        return entity

    def _post_save(self, entity, request):

        pass

    def get_object_or_404(self, **kwargs):

        return get_object_or_404(self.entity, **kwargs)

    def delete(self, *args, **kwargs):

        logical_delete = kwargs.pop("logical", False)

        objs = self.filter(*args, **kwargs)

        if not objs:
            return False

        for obj in objs:
            if not logical_delete:
                obj.delete()
            else:
                obj.active = False
                obj.save()

        return True