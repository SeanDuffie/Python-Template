## @file cli_main.py
#  @author Sean Duffie
#  @brief CLI Interface

import typer
from project.logic import calculate_data

## @var app
# The object that contains the CLI interface
app = typer.Typer()


@app.command()
def compute(value: int):
    """CLI command to run a calculation."""
    result = calculate_data(value)
    print(f"The result is: {result}")
