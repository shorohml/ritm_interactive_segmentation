from setuptools import setup, find_packages


setup(
    name='isegm',
    version='0.0.1',
    packages=find_packages(),
    long_description=open('README.md').read(),
    install_requires=open('requirements.txt').readlines(),
    package_data={
        "isegm": ["utils/cython/*.pyx*"],
    },
)
