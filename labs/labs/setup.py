try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup
    
config = {
    'description': 'prints prime numbers',
    'author': 'etwin',
    'url': 'URL to get it at',
    'download_url': 'Where to download it',
    'author_email': 'etwin@gmail.com',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['labs'],
    'scripts': [],
    'name': 'labs'
}

setup(**config)
