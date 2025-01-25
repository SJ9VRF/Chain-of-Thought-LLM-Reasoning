from setuptools import setup, find_packages

setup(
    name='chain-of-thought',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'logging',
    ],
    description='Chain-of-Thought Reasoning Framework',
)
