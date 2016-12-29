from chandra_aca import __version__

from setuptools import setup

setup(name='nb2to3',
      author='Thomas Kluyver, Fernando Perez, Tom Aldcroft',
      description='Run 2to3 on Jupyter notebook(s)',
      author_email='taldcroft@cfa.harvard.edu',
      url='https://gist.github.com/takluyver/c8839593c615bb2f6e80',
      entry_points={'console_scripts': ['nb2to3 = nb2to3:main']},
      version='0.1',
      zip_safe=False,
      packages=['nb2to3'],
      )
