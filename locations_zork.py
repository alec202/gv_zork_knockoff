"""Class to hold the data and methods of the location class.

Author: Kyle Maitner
Date: 02/14/2023"""

from typing import *
from items_npc import Item
from items_npc import NPC


class Location:
    """
    The Location class holds the methods and data associated with a Location object.

    The class stores information about the location, the items at this location, and stores what npcs,
    are at this location. It also tells user of potential directions they can move in

    Attributes:
        name (str): The name of this location.
        description (str): The description of this location.
        visited (bool): Records if the player has been to this location before.
        directions (dict[str, Location): A dictionary that holds the nearby locations of this Location instance.
            The key is a string and the value is a Location object.
        npc (list[NPC]): Stores a list of NPC objects at this location instance.
        items (list[Item]): Stores a list of Item objects in this location instance.
    """
    def __init__(self, name: str, description: str):
        """Initializes class Location with the correct starting data.

        Params:
            name (str): A string representing the name of this Location instance.
            description (str): A string representing the description of this Location instance"""

        self.name = name
        self.description = description
        self.visited = False
        self.directions: dict[str, Location] = {}
        self.npc: List[NPC] = []
        self.items: List[Item] = []

    def get_locations(self) -> dict[str, 'Location']:
        """
        The getter for the attribute directions.

        Returns:
            directions (dict[str, Location]): A dictionary where the key is a string and the value is a
                Location object.
        """
        return self.directions

    def get_name(self) -> str:
        """
        The getter for the attribute name.

        Returns:
            name (str): A string representing the name of this location.
        """
        return self.name

    def get_description(self) -> str:
        """
        The getter for the attribute description.

        Returns:
            description (str): A string representing the description of this location.
        """
        return self.description

    def get_visited(self) -> bool:
        """
        The getter for the attribute Visited

        Returns:
            visited (bool): A boolean representing if this location has been visited or not.
        """
        return self.visited

    def set_visited(self) -> None:
        """
        The setter for the visited attribute.
        """
        self.visited = True

    def add_location(self, direction: str, location: 'Location') -> None:
        """
        The setter for location.

        Params:
            direction (str): A string representing which direction the location parameter is from this Location
                instance.
            location (Location): A Location object representing the location that is near this location instance.
        """
        if len(direction) == 0:
            raise ValueError('Direction and/or Location cannot be blank')
        if direction in self.directions:
            raise KeyError("key is already in use")
        directions = direction
        locations = location
        self.directions[directions] = locations

    def add_npc(self, npc: NPC) -> None:
        """
        Adds the npc parameter to the list of NPCs at this location instance.

        Params:
            npc (NPC): an NPC object.
        """
        add_npc = npc
        self.npc.append(add_npc)

    def get_npcs(self) -> list[NPC]:
        """
        The getter for the attribute npc.

        Returns:
            npc (list[NPC]): A list of NPC objects assigned to this location's instance.
        """
        return self.npc

    def add_item(self, item: Item) -> None:
        """
        Adds the item parameter to the items list attribute.

        Params:
            item (Item): an Item object.
        """
        add_item = item
        self.items.append(add_item)

    def remove_item(self, item: Item) -> None:
        """
        Removes the item parameter from this Location.

        Parameters:
            item (Item): An Item object.
        """
        remv_item = item
        self.items.remove(remv_item)

    def get_items(self) -> list[Item]:
        """
        The getter for the attribute items.

        Returns:
            items (Item): A list of Item objects at this location.
        """
        return self.items

    def __str__(self) -> str:
        """
        The getter for the attribute items.

        Returns:
            A string representing the name and description of this Location.
        """
        return f'{self.name} - {self.description}'
