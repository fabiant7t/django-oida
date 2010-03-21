from setuptools import setup, find_packages


setup(
    name='django-oida',
    version='0.1',
    description='A set of tools to execute parts of your code only if a '\
        'specified application is installed.',
    long_description=open('README').read(),
    author='Fabian Topfstedt',
    author_email='topfstedt@schneevonmorgen.com',
    url='http://github.com/fabiant7t/django-oida/tree/master',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    package_data = {
        'oida': [
            'templatetags/*',
        ]
    },
    zip_safe=False,
)

