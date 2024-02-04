from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in server_management/__init__.py
from server_management import __version__ as version

setup(
	name="server_management",
	version=version,
	description="server_management",
	author="server_management",
	author_email="hagermossad80@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
