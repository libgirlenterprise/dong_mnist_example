# For easiness of sharing a dong project via pypi
# dong should make a setup.py template for its users

from setuptools import setup, find_packages

setup(name='dong_mnist_example',
      version='0.4',
      description='none',
      url='https://github.com/libgirlenterprise/dong_mnist_example',
      license='apache2',
      install_requires=[
          'tensorflow==2.5.1',
          'dong>=0.2',
      ],
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points = {
        'console_scripts': ['dong_mnist_example=dong_mnist_example:main'],
      },
    )
