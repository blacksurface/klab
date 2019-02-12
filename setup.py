from setuptools import setup

setup(
	name="src",
	packages=["src"],
	
	entry_points = {
		"console_scripts": ["pserv = src.klab:main",] 
			}
	)
