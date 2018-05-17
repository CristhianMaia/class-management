from django.views.generic import TemplateView


class PaginaInicial(TemplateView):
    template_name = 'index_base.html'

