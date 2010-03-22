from django.conf import settings
from django.template import Context, Template 
from django.test import TestCase

IS_INSTALLED_TEXT = "Fix Oida!"
IS_MISSING_TEXT = "Jessas naaa!"


class AppsIsAppTemplateTagTestCase(TestCase):
   
   def setUp(self):
      self.installed_app_name = settings.INSTALLED_APPS[0].split('.')[-1]
      self.missing_app_name = 'jeck5gad7lix7raf1pi2uck5fod5tok4vas3fu2wrerl3oz'

   def get_ifappelse_template(self, app_name):
      return Template("""
         {%% load apps %%}
         {%% if_app "%s" %%}
            %s
         {%% else %%}
            %s
         {%% endif_app %%}
      """ % (app_name, IS_INSTALLED_TEXT, IS_MISSING_TEXT))
   
   def get_ifapp_template(self, app_name):
      return Template("""
         {%% load apps %%}
         {%% if_app "%s" %%}
            %s
         {%% endif_app %%}
      """ % (app_name, IS_INSTALLED_TEXT))

   def test_ifappelse_with_installed_app(self):
      template = self.get_ifappelse_template(self.installed_app_name)
      response = template.render(Context({}))

      self.assertTrue(IS_INSTALLED_TEXT in response)
      self.assertFalse(IS_MISSING_TEXT in response)

   def test_ifappelse_with_missing_app(self):
      template = self.get_ifappelse_template(self.missing_app_name)
      response = template.render(Context({}))

      self.assertFalse(IS_INSTALLED_TEXT in response)
      self.assertTrue(IS_MISSING_TEXT in response)

   def test_ifappelse_with_empty_app_name(self):
      template = self.get_ifappelse_template('')
      response = template.render(Context({}))

      self.assertFalse(IS_INSTALLED_TEXT in response)
      self.assertTrue(IS_MISSING_TEXT in response)

   def test_ifapp_with_installed_app(self):
      template = self.get_ifapp_template(self.installed_app_name)
      response = template.render(Context({}))

      self.assertTrue(IS_INSTALLED_TEXT in response)
      self.assertFalse(IS_MISSING_TEXT in response)