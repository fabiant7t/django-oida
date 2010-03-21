from django import template
from django.core.exceptions import ImproperlyConfigured
from django.db import models


def do_if_app(parser, token):
    """
    An if statement that validates to True if an app is loaded.

    Example (the else tag is optional):
        {% if_app "tagging" %}
            <p>tagging is installed</p>
        {% else %}
            <p>tagging is not installed</p>
        {% endif_app %}
    """
    bits = token.contents.split()
    if len(bits) != 2:
        raise template.TemplateSyntaxError("%s tag takes one argument" % \
            bits[0])
    nodelist_true = parser.parse(('else', 'endif_app'))
    token = parser.next_token()
    if token.contents == 'else':
        nodelist_false = parser.parse(('endif_app', ))
        parser.delete_first_token()
    else:
        nodelist_false = template.NodeList()
    return IfAppTemplateNode(bits[1], nodelist_true, nodelist_false)


class IfAppTemplateNode(template.Node):

    def __init__(self, app_name, nodelist_true, nodelist_false):
        self.app_name = app_name.replace('"', '').replace("'", '')
        self.nodelist_true = nodelist_true
        self.nodelist_false = nodelist_false

    def render(self, context):
        try:
            app = models.get_app(self.app_name)
        except ImproperlyConfigured:
            return self.nodelist_false.render(context)
        return self.nodelist_true.render(context)


register = template.Library()
register.tag('if_app', do_if_app)

