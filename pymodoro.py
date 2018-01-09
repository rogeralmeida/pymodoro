import click
from tqdm import tqdm
import time
import os

SECONDS_PER_MINUTE=60

@click.command()
@click.option('--pomodoro-size', default=25, help="Pomodoro size in MINUTES")
@click.option('--short-break-size', default=5, help="Break size in MINUTES")
@click.option('--skip-break', is_flag=True)
@click.argument('task', nargs=-1)
def cli(pomodoro_size, short_break_size, skip_break, task):
    task_text = " ".join(task)
    click.secho("Pomodoro for task: {}".format(task_text), fg='blue')
    for i in tqdm(range(pomodoro_size * SECONDS_PER_MINUTE)):
        time.sleep(0.99999)
    os.system('terminal-notifier -title "Pomodoro Done" -message "'+" ".join(task_text)+'" -sound default')

    if skip_break == False:
        click.echo("Start a short break of {} minutes?[yn]".format(short_break_size))
        option = click.getchar()
        if option == 'y':
            click.secho("Pomodoro done! It is time for a break", fg='green')
            for i in tqdm(range(short_break_size * SECONDS_PER_MINUTE)):
                time.sleep(0.9099)
            os.system('terminal-notifier -title "Pomodoro Break Done" -message "Break done. Lets pomodoro another task" -sound default')
