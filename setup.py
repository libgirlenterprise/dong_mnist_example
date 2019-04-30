# For easiness of sharing a dong project via pypi
# dong should make a setup.py template for its users

from setuptools import setup, find_packages

setup(name='tabemasu',
      version='0.1',
      description='none',
      license='apache2',
      install_requires=[
          'tensorflow',
      ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points = {
        'console_scripts': ['tabemasu=tabemasu:main'],
      },
    )
