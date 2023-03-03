"""Class Item and class NPC for Project 2.

Class Item holds the methods and data associated with an Item object. Class NPC holds the
methods and data associated with and NPC object.

Author: Mars Bovee
Date: 02/15/2023"""

from typing import *


class Item:
    """
    The Item class sets up objects that the player will encounter.

    Attributes:
        name (str): The name of the item, cannot be blank.
        description (str): The description of the item, cannot be blank.
        num_calories (int): The number of calories an item has, must be between 0-1000.
        weight (int): How much an item weighs, must be between 0-500.
    """
    def __init__(self, name: str, description: str, num_calories: int, weight: int):
        """Initializes Item class with the corresponding values from the input parameters.

        Params:
            name (str): A string representing the name of this item.
            description (str): A string representing the description of this item.
            num_calories (int): an integer representing the number of calories this item has.
            weight (int): An integer representing the weight of this Item.

        Raises:
            ValueError: If any of the following occur:
                Name and description were blank.
                The num_calories parameter value wasn't between 0 - 1,000.
                The num_calories parameter value wasn't an integer.
                The weight parameter value wasn't an integer.
                The weight parameter value wasn't between 0 - 500.
            """
        if name == '' or description == '':
            raise ValueError('Name and description cannot be blank!')
        self.name = name
        self.description = description
        if num_calories not in range(0, 1001) or not isinstance(num_calories, int):
            raise ValueError('Calories must be an integer between 0-1000!')
        self.num_calories = num_calories
        if weight not in range(0, 501) or not isinstance(weight, int):
            raise ValueError('Weight must be an integer between 0-500!')
        self.weight = weight

    def __str__(self) -> str:
        """
        Returns:
            The Item name with the weight and the description.
        """
        return (f'{self.name} - {self.weight} lb - {self.description}')

    def get_weight(self) -> int:
        """Returns the integer representing the weight of this item."""
        return self.weight

    def get_name(self) -> str:
        """Returns the string representing the name of this item."""
        return self.name

    def get_calories(self) -> int:
        """Returns an integer representing the number of calories this item has"""
        return self.num_calories


class NPC:
    """
    The NPC class sets up and stores information about the characters the player will encounter.

    Attributes:
        name (str): The name of the NPC
        description (str): The description of the NPC
        message (list): A list of the messages an NPC can say
        message_num (int): The current message number the NPC is at.
        high_val (bool): A boolean representing if an NPC has a high value food item or not. This
            is what indicates if that NPC can be robbed or not.
        prize_food (Item): An Item object representing the high value food item that an NPC has.
    """
    def __init__(self, name: str, description: str, message: list, has_high_value_food: bool, prize_food: Item):
        """Initializes NPC class with the corresponding values from the input parameters.

        Params:
            name (str): A string representing the name of this NPC.
            description (str): A string representing the description of this NPC.
            message (list): A list of strings that represent what the NPC may say when spoken to.
            has_high_value_food (bool): A boolean representing if this NPC has a high value food or not.
            prize_food (Item): An Item object representing this npcs high value food item, if it has one."""
        self.name = name
        self.description = description
        self.message = message
        self.message_num = 0
        self.high_val = has_high_value_food
        self.prize_food = prize_food

    def get_name(self) -> str:
        """
        The getter for the name attribute.

        Returns:
            self.name
        """
        return self.name

    def set_name(self, name) -> None:
        """
        The setter for name.

        Parameters:
            name (str): The name we wish to use for the NPC.
        """
        self.name = name

    def get_description(self) -> str:
        """
        The getter for the attribute description.

        Returns:
             self.description
        """
        return self.description

    def set_description(self, description) -> None:
        """
        The setter for description.

        Parameters:
            The description we wish to use for the NPC.
        """
        self.description = description

    def get_message(self) -> str:
        """
        The getter for the message attribute.

        Returns:
            The message corresponding to the current message number.
        """
        if self.message_num == len(self.message):
            self.message_num = 0
        message = self.message[self.message_num]
        self.message_num += 1
        return message

    def __str__(self) -> str:
        """
        Returns:
            The npcs name as a string.
        """
        s = f'{self.name}'
        return s

    def has_prize_food(self) -> bool:
        """Returns the boolean representing if the NPC has a high value food or not."""
        return self.high_val

    def get_prize_food(self) -> Item:
        """Returns the prized food item of the NPC if the NPC has one."""
        self.high_val = False
        return self.prize_food
