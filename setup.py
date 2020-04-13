from setuptools import setup

setup(
    name='PyScraper',
    version='1.0',
    packages=['packages.PyScraper', 'packages.mechanize', 'packages.http.cookiejar', 'packages.bs4', 'packages.urllib3'],
    url='https://github.com/Gat123456/PyScraper',
    license='',
    platforms='any',
    requires=['mechanize', 'cookiejar', 'beautifulsoup4', 'urllib3'],
    install_requires=[
        'mechanize==0.4.5',
        'cookiejar==0.0.3',
        'beautifulsoup4==4.9.0',
        'urllib3==1.25.8'
    ],
    python_requires='>=3',
    author='Amr Samy',
    author_email='',
    description='PyScraper is a python class powered by known libraries to make it easier to scrape websites',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'Programming Language :: Python :: 3.2',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    ],
)
