from setuptools import setup, find_packages

setup(
    name='gtfobins-scan',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        # Add any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'gtfobins-scan=gtfobins_scan:main',
        ],
    },
)
