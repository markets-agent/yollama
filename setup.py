from setuptools import setup, find_packages

setup(
    name='yollama',
    version='1.0.4',
    packages=find_packages(),
    install_requires=[
        'langchain-core',
        'langchain-ollama',
    ],
    author='yactouat',
    author_email='yactouat@yactouat.com',
    description='helper functions for Ollama with Langchain',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/markets-agent/yollama',
    license='MIT',
)
