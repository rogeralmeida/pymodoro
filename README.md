# Pymodoro

It is a command line pomodoro timer to assist you apply the Pomodoro Techinique

## What's the Pomodoro Technique

Please, refer to the [official Pomodoro Technique website](https://cirillocompany.de/pages/pomodoro-technique).

## Installation
```
pip3 install pymodoro
```
## How to use

The most basic format is `pymodoro <TASK>`. The `<TASK>` argument can be any sequence of words and space. You don't have to quote your task's title. The following is a valid example: `pymodoro write more documentation for pymodoro`. This command creates a default 25 minutes long pomodoro with the task "write more documentation for pymodoro". When the 25 minutes pomodoro finishes, pymodoro will prompt you to confirm if you want to start a 5 minutes break.

Of course pymodoro allows you to costumise its behaviour. You can change the pomodoro length, break length, you can skip the break, or skip the break prompt and start the break automatically.
For more details about how to use, refer to the `pymodoro --help` output bellow:

```
Usage: pymodoro [OPTIONS] [TASK]...

  pymodoro is a Pomodoro Timer!

  The basic usage is:

      pymodoro <TASK>

  Examples:

      Starting a default 25 minutes long pomodoro on task 'write blog post':
      `pymodoro write blog post`

      Starting a 35 minutes long pomodoro on task 'call mum': `pymodoro
      --pomodoro-size 35 call mum`

      Starting a default 25 long pomodoro task reading the task title from
      stdin: `echo "This is a test" | pymodoro -`

      Starting a default 25 minutes long pomodoro that will start a 5
      minutes break automatically when the pomodoro finishes: `pymodoro
      --auto-break some custom task`

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

Starting a default 25 long pomodoro task reading the task title from stdin: `echo "This is a test" | pymodoro -`

Starting a default 25 minutes long pomodoro that will start a 5 minutes break automatically when the pomodoro finishes: `pymodoro --auto-break some custom task`

## Contribution

Fork. Change. Pull Request.

## License

Please refer to LICENSE.txt

## Changelog

### 1.0.0

Creating pomodoro passing the task title as argument

### 1.1.0

Be able to receive the title task from stdin
