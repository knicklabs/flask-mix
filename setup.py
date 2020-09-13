"""
Flask-Mix

Integrates Laravel Mix with Flask. Mix is an elegant wrapper around Webpack for the 80% use case.

See: https://laravel-mix.com
"""

from setuptools import setup

with open('README.md', 'r') as readme:
    long_description = readme.read()

setup(
    name='Flask-Mix',
    version='0.0.1',
    url='https://github.com/knicklabs/flask-mix',
    license='MIT',
    author='Nickolas Kenyeres',
    author_email='nickolas@knicklabs.com',
    description='Integrates Laravel Mix with Flask',
    long_description=long_description,
    long_description_content_type="text/markdown",
    py_modules=['flask_mix'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=['Flask'],
    keywords=['flask', 'webpack', 'assets', 'static', 'laravel', 'mix'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Flask',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    python_requires='>=3.6',
)
