from setuptools import setup

setup(
    name='pomodoro',
    version='0.0.1',
    py_modules=['bujo'],
    install_requires=['Click', 'tqdm'],
    entry_points='''
        [console_scripts]
        pomodoro=pomodoro:cli
    '''
        )
