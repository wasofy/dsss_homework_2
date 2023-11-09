from setuptools import setup, find_packages

setup(
    name='math-game',
    version='1.0.0',
    author='Mohamed Ibrahim',
    description='A Python math game.',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'math-quiz = math_quiz:math_quiz',
        ],
    },
)
