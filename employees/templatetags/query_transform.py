from django import template

register = template.Library()


@register.simple_tag
def query_transform(request, **kwargs):
    updated_query = request.GET.copy()
    for variable_name, value in kwargs.items():
        if value is not None:
            updated_query[variable_name] = value
        else:
            updated_query.pop(variable_name, 0)
    return updated_query.urlencode()
