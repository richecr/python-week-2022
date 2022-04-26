import typer
from typing import Optional
from rich.table import Table
from rich.console import Console

from beerlog import core


main = typer.Typer(help="Beer Management Application")

console = Console()

@main.command("add")
def add(
    name: str,
    style: str,
    flavor: int = typer.Option(...),
    image: int = typer.Option(...),
    cost: int = typer.Option(...),
):
    """Adds a new beer to database."""
    if core.add_beer_to_database(name, style, flavor, image, cost):
        print(":beer_mug: Beer added to database")


@main.command("list")
def list(style: Optional[str] = None):
    """Lists beers in database."""
    beers = core.get_beers_from_database()
    table = Table(title="Beerlog :beer_mug:")
    headers = ['id', 'name', 'style', 'rate', 'date']
    for header in headers:
        table.add_column(header, style="magenta")
    for beer in beers:
        values = [str(getattr(beer, header)) for header in headers]
        table.add_row(*values)
    console.print(table)
    
