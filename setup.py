from setuptools import setup, find_packages


setup(name='italian_vip_says',
	version='1.0.0',
	url='https://github.com/lotrekagency/italian-vip-says',
	license='MIT',
	author='Lotrek',
	author_email='dimmitutto@lotrek.it',
	description='Find out what some Italian VIPs really say',
	long_description=open('README.md').read(),
	install_requires=[],
	packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 3'
    ]
)
