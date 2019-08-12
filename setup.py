# -*- coding: utf-8 -*-
from os.path import join, dirname
from setuptools import setup, find_packages


version = __import__('model_report').__version__


LONG_DESCRIPTION = """
django-model-report
===================

django reports integrated with highcharts

"""


def long_description():
    try:
        return open(join(dirname(__file__), 'README.md')).read()
    except IOError:
        return LONG_DESCRIPTION


setup(name='django-reports-python3',
      version=version,
      author='tanishqandmac',
      author_email='tanishqandmac@gmail.com',
      description='Django reports integrated with highcharts.',
      license='MIT',
      keywords='django, model, report, reports, highcharts, chart, charts',
      url='https://github.com/tanishqandmac/django-reports-python-3',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      long_description=long_description(),
      install_requires=[
        'reportlab',
        'html5lib',
        'xhtml2pdf',
        'xlwt',
      ],
      classifiers=['Framework :: Django',
                   'Development Status :: 1 - Beta',
                   'Topic :: Internet',
                   'Intended Audience :: Developers',
                   'Environment :: Web Environment',
                   'Programming Language :: Python :: 3.6'])
