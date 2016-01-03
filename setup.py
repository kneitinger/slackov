try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'A Slack bot that uses Markov chains to learn to\
        speak like a generic member of your team',
    'author': 'Kyle J. Kneitinger',
    'url': 'https://github.com/kneitinger/slackov',
    'author_email': 'kneit@pdx.edu',
    'version': '0.2.1',
    'install_requires': ['slackclient','markoff'],
    'scripts': ['bin/slackov'],
    'name': 'slackov',
    'packages': ['slackov'],
    'license' : 'BSD',
    'classifiers' : [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Communications :: Chat',
        'Topic :: Text Processing :: Linguistic'
    ]

}

setup(**config)
