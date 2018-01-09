# Pomodoro

It is a command line tool to assist you on applying the Pomodoro Techinique

## What's the Pomodoro Technique

Please, refer to the [official website](https://cirillocompany.de/pages/pomodoro-technique).

## Installation
```
pip3 install pymodoro
```
## How to use
```
Usage: pymodoro [OPTIONS] [TASK]...

  pymodoro is a Pomodoro Timer!

Options:
  --pomodoro-size INTEGER     Pomodoro size in MINUTES
  --short-break-size INTEGER  Break size in MINUTES
  --skip-break                When present, pymodoro will skip the break
  --auto-break                When present, pymodoro will not expect a
                              confirmation to start a break
  --help                      Show this message and exit.
```
### Examples
Starting 25 minutes long pomodoro on task 'write blog post': `pymodoro write blog post`

Starting 35 minutes long pomodoro on task 'call mum': `pymodoro --pomodoro-size 35 call mum`

## Contribution
