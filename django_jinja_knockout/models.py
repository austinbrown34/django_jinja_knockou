from django.apps import apps

def get_verbose_name(obj, fieldname):
    if type(obj) is str:
        Model = apps.get_model(*obj.split('.'))
        return Model._meta.get_field_by_name(fieldname)[0].verbose_name
    else:
        return obj._meta.get_field_by_name(fieldname)[0].verbose_name


class ContentTypeLinker(object):

    def __init__(self, obj, typefield, idfield):
        self.model = None
        self.url = None
        self.description = ''
        self.obj_type = getattr(obj, typefield)
        if self.obj_type is not None:
            model_class = self.obj_type.model_class()
            self.model = model_class.objects.filter(pk=getattr(obj, idfield)).first()
            if self.model is not None:
                if hasattr(self.model, 'get_canonical_link') and callable(self.model.get_canonical_link):
                    self.description, self.url = self.model.get_canonical_link()
                else:
                    self.description = str(self.model)