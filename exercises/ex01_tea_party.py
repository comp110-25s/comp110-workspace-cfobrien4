"Ex1 Tea Party Planner"


__author__: str = "730670964"


def main_planner(guests: int) -> None:
    "Displays tea bag and treat count and cost for the amount of guests"
    print("A Cozy Tea Party for " + str(guests) + " People")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            (cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests)))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Returns a number of 2 tea bags for each person."""
    return 2 * people


def treats(people: int) -> int:
    """Returns 1.5 treats for every drink"""
    return int((tea_bags(people=people)) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Returns the cost of the tea party"""
    return tea_bags(people=tea_count) / 2 * 0.50 + treats(people=treat_count) / 3 * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))


age: int = 4
age = age + 1
age = 18
