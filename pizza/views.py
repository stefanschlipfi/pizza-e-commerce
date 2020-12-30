
from django.views.generic import TemplateView


class ProductsView(TemplateView):
    template_name = 'pizza/products.html'

class BasketView(TemplateView):
    template_name = 'pizza/basket.html'