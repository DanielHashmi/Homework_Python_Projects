magicians: list[str] = ['Daniel', 'Aysha', 'Oz',
                        'KungFuPanda', 'HarryPotter', 'Dambaldore']


def show_magicians(array: list[str]) -> None:
    for magician in array:
        print(magician)


def make_great(array: list[str]) -> list[str]:
    new_magicians: list[str] = []
    for magician in array:
        new_magicians.append(magician.replace(
            magician, f'The Great {magician}'))

    return new_magicians


print(make_great(magicians))
show_magicians(magicians)
