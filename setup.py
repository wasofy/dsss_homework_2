from setuptools import setup, find_packages

setup(
    name='math-game',
    version='1.0.0',
    author='Mohamed Ibrahim',
    description='A Python math quiz game.',
    packages=find_packages(),
    install_requires=[
        'random'
    ],
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz:math_quiz',
        ],
    },
)
