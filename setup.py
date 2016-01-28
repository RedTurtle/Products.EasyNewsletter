# -*- coding:utf-8 -*-

from setuptools import find_packages
from setuptools import setup

version = '3.0a3.dev3'
long_description = (
    open('README.rst').read() + '\n' +
    open('CHANGES.rst').read()
)

setup(
    name='Products.EasyNewsletter',
    version=version,
    description="Powerful newsletter/mailing addon for Plone",
    long_description=long_description,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    keywords='Zope Plone Newsletter Mailing',
    maintainer='Maik Derstappen, Timo Stollenwerk, Andreas Jung',
    author='Maik Derstappen',
    author_email='maik.derstappen@inqbus.de',
    url='http://plone.org/products/easynewsletter',
    license='GPL',
    packages=find_packages(exclude=['ez_setup']),
    namespace_packages=['Products'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'Products.CMFPlone',
        'Products.Archetypes',
        'Products.ATContentTypes',
        'BeautifulSoup',
        'jinja2',
        'nameparser',
        'plone.api',
        'Products.TemplateFields',
        'setuptools',
        'stoneagehtml',
    ],
    extras_require=dict(
        test=[
            'Pillow',
            'plone.app.testing',
            'plone.dexterity',
            'Products.SecureMailHost',
        ],
        fmp=['inqbus.plone.fastmemberproperties'],
        zamqp=[
            'collective.zamqp',
            'msgpack-python',
        ],
        all=[
            'collective.zamqp',
            'inqbus.plone.fastmemberproperties',
            'msgpack-python',
        ]
    ),
)
