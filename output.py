import csv
import rich
from rich.table import Table
from rich.console import Console
from pathlib import Path

def output_cli(leads):
    console = Console()

    table = Table(title="Leads")

    table.add_column("Name", style="cyan")
    table.add_column("Address", style="green")
    table.add_column("Phone")
    table.add_column("Website")
    table.add_column("Rating")
    table.add_column("Reviews")

    for lead in leads:
        table.add_row(
            lead.name,
            lead.address,
            str(lead.phone or ""),
            str(lead.website or ""),
            str(lead.rating or ""),
            str(lead.reviews or "")
        )

    console.print(table)

def output_csv(leads, filename="leads.csv"):

    export_dir = Path.home() / ".leadminer" / "exports"
    export_dir.mkdir(exist_ok=True)

    filepath = export_dir / filename

    with open(filepath, "w", newline="") as f:
        writer = csv.writer(f)

        writer.writerow([
            "name",
            "address",
            "phone",
            "website",
            "rating",
            "reviews"
        ])

        for lead in leads:
            writer.writerow([
                lead.name,
                lead.address,
                lead.phone,
                lead.website,
                lead.rating,
                lead.reviews
            ])
    print(f"Exported CSV to {filepath}")

def output(option: str, leads):
    if option == "csv":
        output_csv(leads)

    elif option == "cli":
        output_cli(leads)