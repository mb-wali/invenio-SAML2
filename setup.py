import os
from setuptools import find_packages, setup

readme = open('README.rst').read()

tests_require = [
    # 'check-manifest>=0.25',

]

setup_requires = [
    'Babel>=1.3',
    'pytest-runner>=3.0.0,<5',
]

# required dependencies that this package is using.
install_requires = [
    'python3-saml>=1.8.0',
    'python-slugify>=3.0.6',
    'lxml>=3.5.0,<4.2.6',
    # 'xmlsec>=1.3.3',
]

# to add external data for example .txt or .dat or any other. not a python code.
# package_data = {
# }

packages = find_packages(exclude=['docs', 'tests*'])

# Get the version string. Cannot be done with import!
g = {}

with open(os.path.join('shibboleth_Authenticator', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ShibbolethAuthenticator',
    version=version,
    description='ShibbolethAuthenticator invenio',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/mb-wali/saml3.git',
    license='MIT',
    author='TUGRAZ',
    author_email='mb_wali@hotmail.com',
    keywords='SSO SAML2',
    # package_dir={'', 'shibboleth_Authenticator'},

    # packages=packages,
    # zip_safe=False,
    # include_package_data=True,
    # platforms='any',
    entry_points={
        'invenio_base.apps': [
            'shibboleth_Authenticator = shibboleth_Authenticator:ShibbolethAuthenticator',
        ],
        'invenio_base.blueprints': [
            'shibboleth_Authenticator = shibboleth_Authenticator.views.client:blueprint',
        ],
        'invenio_config.module': [
            'shibboleth_Authenticator = shibboleth_Authenticator.config',
        ],
    },
    # extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Development Status :: 5 - Production/Stable',
    ],
)
