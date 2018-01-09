from setuptools import setup

setup(
    name='pymodoro',
    version='1.1.1',
    py_modules=['bujo'],
    install_requires=['Click', 'tqdm'],
    entry_points='''
        [console_scripts]
        pymodoro=pymodoro:cli
    ''',
    author='Roger Almeida',
    author_email="roger.eduardo@gmail.com",
    description="It's a command line pomodoro timer",
    license="MIT",
    keywords="pomodoro technique timer application cli command line tool",
    url="https://github.com/rogeralmeida/pomodoro",
    project_urls={
        "Bug Tracker": "https://github.com/rogeralmeida/pomodoro/issues",
        "Documentation": "https://github.com/rogeralmeida/pomodoro",
        "Source Code": "https://github.com/rogeralmeida/pomodoro",
    }
)
