import inquirer
import os
from rich.console import Console
from rich.table import Table

# Global list to store assets
assets = []


def add():
    # Additional prompt to gather asset information
    asset_questions = [
        inquirer.Text(
            'symbol', message="Please enter a ticker or asset name:"),
        inquirer.Text(
            'avg_price', message="What is your average price paid for this asset?")
    ]
    asset_answers = inquirer.prompt(asset_questions)
    if asset_answers:
        assets.append(asset_answers)  # Store the answers in the global list
        asset_name = asset_answers['symbol']
        asset_avg_price = asset_answers['avg_price']
        print(f"Adding asset: {asset_name} with an average price of {
              asset_avg_price}")


def view():
    table = Table(title="Assets")
    columns = ["Ticker/Asset Name", "Average Price Paid"]

    for column in columns:
        table.add_column(column)

    for asset in assets:
        table.add_row(asset['symbol'], asset['avg_price'],
                      style='bright_green')

    console = Console()
    console.print(table)


def main():
    # Prompt user questions
    prompt_question = [
        inquirer.List(
            "action",
            message="Which action would you like to perform in your vault?",
            choices=[
                "View Dashboard",
                "Add Asset",
                "Close Vault"
            ],
            carousel=True,
        )
    ]

    should_prompt_user = True
    while should_prompt_user:
        prompt_answers = inquirer.prompt(prompt_question)
        if prompt_answers:
            match prompt_answers["action"]:
                case "View Dashboard":
                    view()
                case "Add Asset":
                    add()
                case "Close Vault":
                    should_prompt_user = False


if __name__ == "__main__":
    main()
