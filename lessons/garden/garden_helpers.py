"""Some functions for my garden plan!"""

__author__ = "730477259"


def add_by_kind(by_kind: dict[str, list[str]], new_plant_kind: str, new_plant: str) -> None:
    """Group flowers by kind!"""
    if new_plant_kind in by_kind:
        by_kind[new_plant_kind].append(new_plant)
    else:
        by_kind[new_plant_kind] = []
        by_kind[new_plant_kind].append(new_plant)


def add_by_date(plants_by_date: dict[str, list[str]], month: str, plant: str) -> None:
    """Add plants by date!"""
    if month in plants_by_date:
        plants_by_date[month].append(plant)
    else:
        plants_by_date[month] = []
        plants_by_date[month].append(plant)


def lookup_by_kind_and_date(plants_by_kind: dict[str, list[str]], plants_by_date: dict[str, list[str]], kind: str, month: str) -> str:
    """Return string with list of plants of a specific kind to paltn in a specific month."""
    assert kind in plants_by_kind
    assert month in plants_by_date
    # Get a list of all plants of the specific kind input
    kind_list: list[str] = plants_by_kind[kind]
    # Get a list of all plants planted in a  specific month
    month_list: list[str] = plants_by_date[month]
    # Go through both lists and find emlements that appear in both
    # kind_list = ["marigold", "daisy"]
    # month_list = ["daisy", "rose"]
    combined_list: list[str] = []
    for plant in kind_list:
        for other_plant in month_list:
            if plant == other_plant:  # plant is in both kind_list and month_list
                combined_list.append(other_plant)
    #   "<kind>s to plant in <month>: <comnined_list>"
    if len(combined_list) > 0:
        return f"{kind}s to plant in {month}: {combined_list}"
    else:  # 'No <kind>s to plant in <month.'
        return f"No {kind}s to plant in {month}."