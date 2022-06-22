from setuptools import setup, find_packages

with open('README.md', encoding='utf-8', mode='r') as readme:
    readme_Desc = readme.read()

setup(
    name="discord-build-info-py",
    version="0.0.4",
    author="KiyonoKara",
    # author_email="None",
    description="A module to get Discord clients' build information.",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    url="https://github.com/KiyonoKara/Discord-Build-Info-PY",
    packages=find_packages(exclude=['tests*']),
    keywords=['DISCORD', 'DISCORD LIBRARY', 'DISCORD BUILD', 'HTTP', 'URLLIB', 'REQUEST'],
    license='Apache 2.0',
    # classifiers=[
    #     "Programming Language :: Python :: 3",
    # ],
    python_requires='>=3.7',
)
