import cligenius

app = cligenius.Cligenius()


def complete(ctx, args, incomplete):
    cligenius.echo(f"info name is: {ctx.info_name}", err=True)
    cligenius.echo(f"args is: {args}", err=True)
    cligenius.echo(f"incomplete is: {incomplete}", err=True)
    return [
        ("Camila", "The reader of books."),
        ("Carlos", "The writer of scripts."),
        ("Sulaiman", "The type hints guy."),
    ]


@app.command()
def main(name: str = cligenius.Option("World", autocompletion=complete)):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
