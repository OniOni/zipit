import sys
sys.path.insert(1, f'{sys.path[0]}/deps')

import click


@click.command()
def hello():
    click.echo("Hello, World!")


if __name__ == '__main__':
    hello()
