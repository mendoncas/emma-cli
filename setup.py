from setuptools import setup
setup(
    name='emma',
    version='0.1.0',
    packages=['emma'],
    entry_points={
        'console_scripts': [
            'emma = emma.__main__:main'
        ]
    })
