from setuptools import setup

setup(name='website_status',
      version='0.0.5',
      description='Check whether a website is up or down',
      long_description='Check whether a website is up or down with just one function call',
      keywords='website status website down website up',
      url='http://github.com/sahildua2305/website_status',
      author='Sahil Dua',
      author_email='sahildua2305@gmail.com',
      license='MIT',
      packages=['website_status'],
      install_requires=[
            'requests',
      ],
      zip_safe=False)