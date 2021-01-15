import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hylebot",
    version="0.0.1",
    author="Cuong Duong Tuan",
    author_email="cduongt@gmail.com",
    description="Twitch and Discord bot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/cduongt/hylebot-reborn",
    packages=setuptools.find_packages(where='hylebot'),
    package_dir={
    '': 'hylebot',
    },
    install_requires=[
          'irc',
          'redis',
          'requests'
          'python-dateutil'
      ],
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
)