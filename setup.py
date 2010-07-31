from setuptools import setup, find_packages

version = '2.0.1'

setup(name='Products.EasyNewsletter',
      version=version,
      description="An easy to use but powerfull newsletter/mailing product for Plone",
      long_description=open("README.txt").read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Development Status :: 4 - Beta",
        ],
      keywords='Zope Plone Newsletter Mailing',
      author='Kai Diefenbach',
      author_email='kai.diefenbach@iqpp.de',
      url='http://plone.org/products/easynewsletter/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'Products.TemplateFields',
          'inqbus.plone.fastmemberproperties',
      ],
)