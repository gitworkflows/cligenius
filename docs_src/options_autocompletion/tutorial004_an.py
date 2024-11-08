import cligenius
from typing_extensions import Annotated

valid_completion_items = [
    ("Camila", "The reader of books."),
    ("Carlos", "The writer of scripts."),
    ("Sulaiman", "The type hints guy."),
]


def complete_name(incomplete: str):
    completion = []
    for name, help_text in valid_completion_items:
        if name.startswith(incomplete):
            completion_item = (name, help_text)
            completion.append(completion_item)
    return completion


app = cligenius.Cligenius()


@app.command()
def main(
    name: Annotated[
        str,
        cligenius.Option(help="The name to say hi to.", autocompletion=complete_name),
    ] = "World",
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
