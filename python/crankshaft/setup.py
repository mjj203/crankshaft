
"""
CartoDB Spatial Analysis Python Library
See:
https://github.com/CartoDB/crankshaft
"""

from setuptools import setup, find_packages

setup(
    name='crankshaft',

    version='0.0.01',

    description='CartoDB Spatial Analysis Python Library',

    url='https://github.com/CartoDB/crankshaft',

    author='Data Services Team - CartoDB',
    author_email='dataservices@cartodb.com',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Mapping comunity',
        'Topic :: Maps :: Mapping Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='maps mapping tools spatial analysis geostatistics',

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    extras_require={
        'dev': ['unittest'],
        'test': ['unittest', 'nose', 'mock'],
    },

    # The choice of component versions is dictated by what's
    # provisioned in the production servers.
    install_requires=['pysal==1.11.0', 'numpy==1.10.4', 'scipy==0.17.0', 'pandas==0.17.1', 'scikit-learn==0.17.0', 'statsmodels==0.6.1', 'keras==0.3.2', 'shapely==1.5.3', 'osgeo==2.0.2','scikit-image==0.12.3'],

    requires=['pysal', 'numpy', 'scipy', 'pandas', 'scikit-learn', 'statsmodels', 'keras', 'shapely', 'osgeo','skimage'],

    test_suite='test'
)
