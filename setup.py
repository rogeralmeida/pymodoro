from setuptools import setup

setup(
    name='pymodoro',
    version='1.0.0',
    py_modules=['bujo'],
    install_requires=['Click', 'tqdm'],
    entry_points='''
        [console_scripts]
        pomodoro=pomodoro:cli
    ''',
    author='Roger Almeida',
    author_email="roger.eduardo@gmail.com",
    description="Pomodoro timer",
    license="MIT",
    keywords="pomodoro technique timer application cli command line tool",
    url="https://github.com/rogeralmeida/pomodoro",
    project_urls={
        "Bug Tracker": "https://github.com/rogeralmeida/pomodoro/issues",
        "Documentation": "https://github.com/rogeralmeida/pomodoro",
        "Source Code": "https://github.com/rogeralmeida/pomodoro",
    }
)
