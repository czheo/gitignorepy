from setuptools import setup

setup(
    name="gitignorepy",
    version="0.3.0",
    description="fetch gitignore files from github",
    url='https://github.com/czheo/gitignorepy/',
    author="czheo",
    license="MIT",
    keywords="git github gitignore",
    scripts=[
        'bin/gg'
    ],
    install_requires=[
        'requests',
        'requests_cache',
    ],
)
