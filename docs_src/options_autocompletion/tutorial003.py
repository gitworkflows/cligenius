import cligenius

valid_names = ["Camila", "Carlos", "Sulaiman"]


def complete_name(incomplete: str):
    completion = []
    for name in valid_names:
        if name.startswith(incomplete):
            completion.append(name)
    return completion


app = cligenius.Cligenius()


@app.command()
def main(
    name: str = cligenius.Option(
        "World", help="The name to say hi to.", autocompletion=complete_name
    ),
):
    print(f"Hello {name}")


if __name__ == "__main__":
    app()
