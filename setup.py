from setuptools import setup, find_packages

with open('README.md') as readme_file:
    README = readme_file.read()

with open('HISTORY.md') as history_file:
    HISTORY = history_file.read()

setup(
    name='oze_dataset',
    version='0.0.4',
    description='Downloads oze dataset and creates npz file.',
    long_description_content_type="text/markdown",
    long_description=README + '\n\n' + HISTORY,
    license='MIT',
    packages=find_packages(exclude=("tests",)),
    author='Daniel Kaminski de Souza',
    author_email='daniel@kryptonunite.com',
    keywords=['Dataset', 'Oze Dataset', 'Time Series'],
    url='https://github.com/krypton-unite/oze_dataset.git',
    download_url='https://pypi.org/project/oze-dataset/',
    install_requires = [
        'numpy',
        'pandas',
        'lxml',
        'requests',
        'tqdm'
    ],
    extras_require={
        'test': [
            'pytest',
            'python-dotenv',
            'pytest-cov'
        ],
        'dev': [
            'bumpversion',
            'twine',
            'wheel'
        ]
    }
)