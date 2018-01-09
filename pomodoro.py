import click
from tqdm import tqdm
import time
import os

@click.command()
@click.argument('task', nargs=-1)
def cli(task):
    click.echo("Pomodoro for task: {}".format(" ".join(task)))
    for i in tqdm(range(25 * 60)):
        time.sleep(0.99999)
    os.system('terminal-notifier -title "Pomodoro Done" -message "'+task['text'] +'" -sound default')
