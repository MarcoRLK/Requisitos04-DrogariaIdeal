from setuptools import find_packages, setup

setup(
    name='drogariaidealgcs',
    version='0.1',
    #packages=find_packages(exclude=("average",)),
    include_package_data=True,
    license='MIT License',  # example license
    description='Trabalho empacotado de gcs',
    long_description='Trabalho de GCS baseado no trabalho de Requisitos, Drogaria Ideal',
    url='https://github.com/MarcoRLK/Requisitos04-DrogariaIdeal',
    author='MarcoRLK',
    author_email='marco.antoniorl10@gmail.com',

    # Classifiers (see https://pypi.python.org/pypi?%3Aaction=list_classifiers)
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],

    # Packages and dependencies
    package_dir={'': 'DrogariaIdeal'},
    packages=find_packages('DrogariaIdeal'),

    install_requires=[
        'setuptools',
        #"django"
    ],

    extras_require={
        'dev': [
            #'pytest==3.2.3'
        ],
    },

    entry_points = {
       "console_scripts": ["average = average.__main__:main"]
    },
    # Other configurations
    zip_safe=False,
    platforms='any',
)
