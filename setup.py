from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in kastech_addon/__init__.py
from kastech_addon import __version__ as version

setup(
	name="kastech_addon",
	version=version,
	description="Kastech Addon Customization",
	author="InshaSiS Technologies",
	author_email="support@inshasis.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
