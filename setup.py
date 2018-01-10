from setuptools import setup, find_packages

setup(
    name='pymodoro',
    version='1.1.4',
    packages=find_packages(),
    install_requires=['Click', 'tqdm'],
    py_modules=['pymodoro'],
    scripts=['pymodoro.py'],
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
