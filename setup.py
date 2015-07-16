from setuptools import setup

setup(name='website_status',
      version='0.0.1',
      description='Check whether a website is up or down with just one function call',
      url='http://github.com/sahildua2305/website_status',
      author='Sahil Dua',
      author_email='sahildua2305@gmail.com',
      license='MIT',
      packages=['website_status'],
      install_requires=[
            'requests',
      ],
      zip_safe=False)