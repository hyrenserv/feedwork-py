from setuptools import setup, find_packages

setup(
    name='feedwork',
    version='1.0.0',
    description='python project common function.',
    author_email='miweicong@163.com',
    license='MIT Licence',
    packages=find_packages(exclude=["test_suite", "test.*"])
)
