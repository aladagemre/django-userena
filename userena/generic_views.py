from django.views.generic import TemplateView
from django.template.context import RequestContext
from django.views.generic.list import ListView


class ExtraContextTemplateView(TemplateView):
    extra_context = None

    def get_context_data(self, *args, **kwargs):
        context = super(ExtraContextTemplateView, self).get_context_data(*args, **kwargs)
        if self.extra_context:
            context.update(self.extra_context)
        return context