from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='MIT',
    description='ESDA example eython package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/williamHlatshwayo/esda_eg_package.git',
    author='William X',
    author_email='74763532+williamHlatshwayo@users.noreply.github.com'
)