"Comp110 exercise 3"
__author__: str = "730670964"


def invert(d: dict[str, str]) -> dict[str, str]:
    inverted = {}
    for key, value in d.items():
        if value in inverted:
            raise KeyError(f"Found a duplicate key when inverting: {value}")
        inverted[value] = key
    return inverted


def count(values: list[str]) -> dict[str, int]:
    result: dict[str, int] = {}
    for item in values:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    color_counts = count(list(favorites.values()))
    max_count = 0
    most_frequent = ""
    for color in favorites.values():
        if color_counts[color] > max_count:
            max_count = color_counts[color]
            most_frequent = color
    return most_frequent


def bin_len(words: list[str]) -> dict[int, set[str]]:
    result: dict[int, set[str]] = {}
    for word in words:
        length = len(word)
        if length in result:
            result[length].add(word)
        else:
            result[length] = {word}
    return result
