import os
from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    'check-manifest>=0.25',
    'coverage>=4.0',
    'invenio-app>=1.0.4',
    'invenio-mail>=1.0.0',
    'invenio-userprofiles>=1.0.0',
    'isort>=4.3.3',
    'mock>=2.0.0',
    'pydocstyle>=2.0.0',
    'pytest-cov>=2.5.1',
    'pytest-invenio>=1.1.0',
    'pytest-pep8>=1.0.6',
    'redis>=2.10.5',

]

extras_require = {
    'docs': [
        'Sphinx>=1.5.1',
    ],
    'mysql': [
        'invenio-db[mysql]>=1.0.0',
    ],
    'postgresql': [
        'invenio-db[postgresql]>=1.0.0',
    ],
     'sqlite': [
        'invenio-db>=1.0.0',
    ],
    'tests': tests_require,
}

extras_require['all'] = []

for name, reqs in extras_require.items():
    if name in ('mysql', 'postgresql', 'sqlite'):
        continue
    extras_require['all'].extend(reqs)
    
setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

# required dependencies that this package is using.
install_requires = [
    'Flask>=0.11.1',
    'Flask-Login>=0.3.2',
    'Flask-WTF>=0.13.1',
    'oauthlib>=1.1.2,!=2.0.3,!=2.0.4,!=2.0.5,<3.0.0',
    'python3-saml>=1.4.0',
    'requests-oauthlib>=0.6.2,<1.2.0',
    'uritools>=1.0.1',
    'python-slugify>=4.0.0',
]

packages = find_packages()

# Get the version string. Cannot be done with import!
g = {}

with open(os.path.join('invenio_saml', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='invenio-SAML',
    version=version,
    description='Module for invenio that provides authentication via Shibboleth.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mb-wali/invenio-SAML',
    license='MIT',
    author='TUGRAZ',
    author_email='mb_wali@hotmail.com',
    include_package_data=True,
    platforms='any',
    entry_points={
        'invenio_base.apps': [
            'invenio_saml = invenio_saml:InvenioSAML',
        ],
        'invenio_base.blueprints': [
            'invenio_saml = invenio_saml.views.client:blueprint',
        ],
        'invenio_config.module': [
            'invenio_saml = invenio_saml.config',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Development Status :: 5 - Production/Stable',
    ],


)
