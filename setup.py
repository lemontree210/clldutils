from setuptools import setup, find_packages

setup(
    name='clldutils',
    version='2.5.2',
    description='Utilities for clld apps',
    long_description=open("README.md").read(),
    long_description_content_type='text/markdown',
    author='Robert Forkel',
    author_email='forkel@shh.mpg.de',
    url='https://github.com/clld/clldutils',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    include_package_data=True,
    install_requires=[
        'six',
        'python-dateutil',
        'configparser>=3.5.0b2',
        'tabulate>=0.7.7',
        'colorlog',
        'attrs>=18.1.0',
        'pathlib2; python_version < "3.5"',
        'csvw>=1.0',
    ],
    extras_require={
        'dev': ['flake8', 'wheel', 'twine'],
        'test': [
            'mock',
            'pytest>=3.1',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
        ],
    },
    license="Apache 2.0",
    zip_safe=False,
    keywords='',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
