from setuptools import setup, find_packages
import os

version = '3.1.2.dev0'

tests_require = [
    'ftw.builder',
    'ftw.solr',
    'ftw.testbrowser',
    'ftw.subsite',
    'ftw.testing',
    'plone.app.testing',
    'plone.resource',
    'pyquery',
    'unittest2',
    ]

setup(name='plonetheme.onegov',
      version=version,
      description="Theme package for OneGov",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # https://pypi.org/pypi?:action=list_classifiers
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Framework :: Plone",
        "Framework :: Plone :: 4.1",
        "Framework :: Plone :: 4.2",
        "Framework :: Plone :: 4.3",
        "Framework :: Plone :: Theme",
        "Framework :: Zope2",
        "Framework :: Zope3",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='plone theme onegov',
      author='Julian Infanger',
      author_email='julian.infanger@4teamwork.ch',
      url='http://www.4teamwork.ch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['plonetheme'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'plone.app.theming',
        'Products.Archetypes',
        'Products.CMFCore',
        'collective.mtrsetup',
        'ftw.mobilenavigation>=1.2.3',
        'ftw.slider >= 2.1.1',
        'ftw.upgrade',
        'setuptools',
        'plone.batching',
        'PyScss',
        'plone.api',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
