from setuptools import setup

setup(
    name="gitignore",
    version="0.0.1",
    description="fetch gitignore files from github",
    author="czheo",
    license="MIT",
    keywords="git github gitignore",
    scripts=[
        'bin/gg'
    ],
    packages=[
        'gitignore'
    ],
    install_requires=[
        'requests',
        'requests_cache',
    ],
)
