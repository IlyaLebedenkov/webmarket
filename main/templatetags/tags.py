from django import template
from main.models import Product
register = template.Library()
@register.simple_tag(name="my_tag")
def resolve_product(id):
    product = Product.objects.get(pk=id)
    return f"{product.name}"