import os

from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README')).read()
CHANGES = open(os.path.join(here, 'CHANGES')).read()

setup(name='weibopay',
      version='0.1',
      description='',
      long_description=README + '\n\n' +  CHANGES,
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Topic :: Internet :: WWW/HTTP",
        ],
      author='Filia Tao',
      author_email='Filia.Tao@gmail.com',
      url='',
      keywords='weibopay',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'Django',
#            'Django-Piston',
            #'django-email-confirmation',
            ],
      tests_require=[
            'Django',
#            'Django-Piston',
            #'django-email-confirmation',
            ],
      )

