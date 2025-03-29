from setuptools import setup, find_packages

with open('requirements.txt', 'r') as f :
    requirements = [line for line in f.read().split('\n')]

setup(
    name='summarize',
    version='0.0.1',
    summary='demonstration of summarize text using HuggingFace',
    home_page='https://github.com/MaksimNikolin/Text_summarization',
    author='Maksim Nikolin',
    entry_points={'console_scripts': ['summarize=main:main']},
    install_requires=requirements,
    packages=find_packages()
)
