from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

REQUIREMENTS = {
    'base': [],
    'test': ['pytest==6.1.1']
}
setup(
    name='kcache',
    version='0.0.3',
    package_dir={'': 'src'},
    packages=['kcache'],
    url='https://github.com/krzysbaranski/kcache',
    license='GNU Lesser General Public License Version 3',
    author='Krzysztof Baranski',
    author_email='baranski5@gmail.com',
    description='Cache Library',
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQUIREMENTS['base'],
    tests_require=REQUIREMENTS['test'],
    extras_require={'test': REQUIREMENTS['test']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries",
        "Typing :: Typed"
    ],
    python_requires='>=3.7',
)
