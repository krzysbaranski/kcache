from setuptools import setup


REQUIREMENTS = {
    'base': [],
    'test': []
}
setup(
    name='kcache',
    version='0.0.2',
    package_dir={'': 'src'},
    packages=['kcache'],
    url='https://github.com/krzysbaranski/kcache',
    license='GNU Lesser General Public License Version 3',
    author='Krzysztof Baranski',
    author_email='baranski5@gmail.com',
    description='Cache',
    install_requires=REQUIREMENTS['base'],
    tests_require=REQUIREMENTS['test']
)
