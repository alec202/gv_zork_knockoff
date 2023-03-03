"""Class Game for Project 2

Class game holds the data and methods that enable the game to run.

Author: Alec Mirambeau
Date: 02/12/2023"""

import datetime
import random
from typing import *
from items_npc import Item, NPC
from locations import Location


class Game:
    """Class that will hold the game logic for the game.

    Attributes:
        locations (list): A list holding objects of the locations class.
        npc_dict (dict): A dictionary where a string representing the NPC name is the key, and
            the value is the object of that NPC.
        inventory (list): A list holding various food objects from the items class that the user
            currently has in their inventory.
        weight (int): An integer representing the weight of the player.
        calories_needed (int): An integer representing the number of calories needed before the game ends
        run_game (bool): A boolean representing if the game is still currently being played or not.
        commands (dict): A dictionary where the key is a string representing the command a user may enter.
            The value is the method that corresponds to that method.
        current_location (Location): A location object that represents where the player is currently within
            the game.
    """

    def __init__(self):
        """Initializes class game by creating each of the attributes and calling the create world function.

        The attributes get updated from these default values as the other methods are called.
        """
        self._locations = []
        self._npc_dict = {}
        self._inventory = []
        self._weight = 0
        self._calories_needed = 500
        self._run_game = True
        self.create_world()
        self._commands = self.setup_commands()
        self._current_location = self.random_location()

    def create_world(self) -> None:
        """Creates the world that this game takes place in.

        Sets up all the Locations through the Locations class, sets up all the items
        through the items class, and sets up all the NPCs through the NPC class,
        and puts the NPCs and Items in their correct locations."""
        # Set up code for the town.
        town = Location("Quiet Town", "A town full of buildings, but everyone seems to be inside.")
        # Creation and addition of the food items
        bottle = Item("pepsi", "A half drunken bottle of soda", 58, 1)
        town.add_item(bottle)

        # Setting up Lake Laogai
        lake_laogai = Location("Lake Laogai", "A beautiful lake that is a bright shade of blue.")
        # Creating the elf and adding him to Lake Laogai.
        elf_messages = ["Gwt me somrthkng fof this hangoger dude", "Uah, H-hey thefe...",
                        "Ugh, my head", "I don't feel so good"]
        elf_holder = Item("holder", "This is a holder for the elf", 10, 1)
        elf = NPC("elf", "A funny looking elf who could definitely use a bath.", elf_messages, False, elf_holder)
        lake_laogai.add_npc(elf)
        # Create and add the food to Lake Laogai
        sushi = Item("sushi roll", "A single California roll of sushi", 38, 1)
        lake_laogai.add_item(sushi)
        seaweed = Item("bundle of seaweed", "Green, mean, and lean they say", 50, 1)
        lake_laogai.add_item(seaweed)
        seashells = Item("sea shells", "Some pretty looking sea shells", 0, 2)
        lake_laogai.add_item(seashells)

        # Set up for the witch house
        witch_house = Location("Witch House", "A spooky scary house, what could be inside?")
        # creating the witch NPC and putting her in the house
        witch_messages = ["What do you need?",
                          "Hello stranger, I think your leg is all I need left for his next potion.",
                          "Have you seen my cat? She's a real cutie.",
                          "I'm getting impatient, give me your leg or leave me alone.",
                          "You're annoying me, I need to focus on my brew."]
        calorie_potion = Item("calorie potion", "This potion is sure to hold lots of calories", 190, 13)

        witch = NPC("Witch", "A short witch with an ugly mole on her nose.", witch_messages, True, calorie_potion)
        witch_house.add_npc(witch)
        # Creation and addition of food to the witch house
        no_calorie_potion = Item("zero calorie potion", "A blue potion which yields no calories.", 0, 3)
        witch_house.add_item(no_calorie_potion)
        frog_legs = Item("frog legs", "A plate of frog legs.", 90, 5)
        witch_house.add_item(frog_legs)
        chicken_head = Item("chicken head", "The head of a chicken. Looks fresh, but smells bad.", 115, 8)
        witch_house.add_item(chicken_head)

        # Set up the magic forest.
        magic_forest = Location("Magic Forest.", "A thick, green forest. Big enough for one to get lost in.")
        # Setting up the fairy NPC
        fairy_messages = ["Hello Wanderer, I hope you're not lost.",
                          "*sings*",
                          "I like your outfit!",
                          "I'll help in any way I can",
                          "I can't wait until the dragon finally leaves us all alone.",
                          "I can't fly freely with the dragon around. :("]
        magical_mushrooms = Item("magical mushrooms", "These mushrooms sure do have an interesting look to them.",
                                 185, 11)
        fairy = NPC("Fairy", "A small, sparkly, pretty fairy.", fairy_messages, True, magical_mushrooms)
        magic_forest.add_npc(fairy)
        # Creation and addtion of food to the magic forest.
        green_apple = Item("green apple", "A round, clean green apple hanging from a tree.", 50, 1)
        magic_forest.add_item(green_apple)
        pear = Item("pear", "A tasty green fruit, the elf is sure to love this.", 74, 1)
        magic_forest.add_item(pear)
        stick = Item("stick", "A long, skinny, stick. Doesn't look very tasty.", 0, 2)
        magic_forest.add_item(stick)

        # Set up for the cave
        cave = Location("Dark Cave", "A big, spooky, and dark cave.")
        # creation and addition of food in the cave
        magical_crystal = Item("magical crystal", "A shiny, reflective crystal, looks mysterious", 0, 3)
        cave.add_item(magical_crystal)
        old_burger = Item("15 day old burger",
                          "An old, moldy, dirt covered burger. Probably wouldn't taste good.", 0, 2)
        cave.add_item(old_burger)
        rock = Item("small rock", "Just a plain old rock.", 0, 2)
        cave.add_item(rock)

        # set up for tavern
        tavern = Location("Thorfin's Tavern", "The most famous tavern in this town. "
                                              "They serve all kinds of drinks and food.")
        # set up the Troll NPC
        troll_messages = ["OOGA BOOGA CHOOGA",
                          "*Burps in your face*",
                          "BUN DUN DITTY DUM",
                          "*Grunts with hints of annoyance*",
                          "*farts and then walks away from you*"]
        troll_holder = Item("holder for troll", "This is a holder", 10, 1)
        troll = NPC("Troll", "A troll who definitely isn't your average fellow. "
        
                                   "Who knows what goes on in his head", troll_messages, False, troll_holder)
        tavern.add_npc(troll)
        # set up the food in the tavern
        chair = Item("small chair", "A sturdy, wooden chair.", 0, 9)
        tavern.add_item(chair)
        root_beer = Item("root beer", "A tasty, fizzy drink.", 84, 4)
        tavern.add_item(root_beer)
        turkey_leg = Item("turkey leg", "A big piece of meat. Best food item sold at this tavern", 111, 12)
        tavern.add_item(turkey_leg)
        cow_heart = Item("cow heart", "A cow heart cooked to perfection.", 120, 13)
        tavern.add_item(cow_heart)

        # set up for the mountain area
        mountains = Location("Mountain area", "Lot's of high mountains all clumped together. better watch your step!")
        # set up the mountain food
        boulder = Item("boulder", "A really really big rock", 0, 25)
        mountains.add_item(boulder)
        rock2 = Item("small rock", "Just a plain old rock.", 0, 5)
        mountains.add_item(rock2)
        caterpillar = Item("caterpillar", "it's still moving and crawling around", 7, 1)
        mountains.add_item(caterpillar)
        cockroach = Item("cockroach", "A small, creepy looking cockroach", 11, 1)
        mountains.add_item(cockroach)

        # set up the castle
        castle = Location("A really big castle", "A creepy looking castle. It's the only building in these mountains")
        # set up gandalf
        gandalf_messages = ["You shall not pass any farther than this",
                            "The glock is for display purposes only",
                            "I hope you find your way back home safe"]
        gandalf_holder = Item("Gandalf Holder", "This is a holder for Gandalf", 10, 1)
        gandalf = NPC("Gandalf", "Really old, wise guy with a long beard. Seems pretty strong.", gandalf_messages,
                      False, gandalf_holder)
        castle.add_npc(gandalf)
        # set up the items in the castle
        glock = Item("glock", "A gun. Seems like an intimidating weapon.", 0, 8)
        castle.add_item(glock)
        blueberry_pie = Item("blueberry pie", "The best pie flavor out there.", 125, 10)
        castle.add_item(blueberry_pie)
        trail_mix = Item("trail mix bag", "A bag of assorted snacks", 83, 6)
        castle.add_item(trail_mix)
        smoothie = Item("strawberry smoothie", "A very tasty pink liquid.", 94, 9)
        castle.add_item(smoothie)

        # set up all the neighbor dictionaries
        # Making the town neighbor locations dictionary.
        town.add_location("east", tavern)
        town.add_location("west", lake_laogai)
        town.add_location("south", mountains)
        # making the lake laogai neighbor locations dictionary.
        lake_laogai.add_location("east", town)
        lake_laogai.add_location("north", witch_house)
        # making witch neighbor locations dictionary
        witch_house.add_location("east", magic_forest)
        witch_house.add_location("south", lake_laogai)
        # setting up the magic forest neighbors dictionary
        magic_forest.add_location("east", cave)
        magic_forest.add_location("south", tavern)
        magic_forest.add_location("west", witch_house)
        # make the cave neighbors dictionary.
        cave.add_location("west", magic_forest)
        # creating the tavern neighbors dictionary
        tavern.add_location("north", magic_forest)
        tavern.add_location("west", town)
        # set up the mountains neighbor dictionary.
        mountains.add_location("south", castle)
        mountains.add_location("north", town)
        # set up the neighbors dictionary
        castle.add_location("north", mountains)

        self._locations = [town, lake_laogai, witch_house, magic_forest, cave, tavern, mountains, castle]
        self._npc_dict = {"elf": elf,
                          "witch": witch,
                          "fairy": fairy,
                          "troll": troll,
                          "gandalf": gandalf}

    def setup_commands(self) -> Dict[str, 'function']:
        """Method to set up the commands dictionary

        Returns:
            commands (dict[str, Callable]): A dictionary where the key is a string representing
                the method name and the value is the callable method."""
        commands = {"?": self.show_help,
                          "help": self.show_help,
                          "talk": self.talk,
                          "meet": self.meet,
                          "take": self.take,
                          "give": self.give,
                          "go": self.go,
                          "items": self.show_items,
                          "look": self.look,
                          "quit": self.quit,
                          "q": self.quit,
                          "rob": self.rob,
                          "teleport": self.teleport}
        return commands

    def random_location(self) -> Location:
        """Returns a random location from the locations list."""
        random_index = random.randint(0, len(self._locations) - 1)
        return self._locations[random_index]

    def play(self) -> None:
        """Method That is the core loop used to run the game."""
        print("\nWelcome to the magical world of Ireland! A once lively and joyful area, "
              "has now become\nvery grim and depressing. Why you may ask? Well unfortunately, the dragon Alduin\n"
              "has taken over the area. He flies around and eats people who are happy. What makes matters worse\n"
              "is that our hero elf is too drunk to do anything about the dragon. Please hero, feed the elf\n"
              "some food to help sober him up. Please save us from this dragon.\n")
        self.show_help()

        # begin game loop
        while self._run_game:

            # Get the input as lower case letters and make the list of tokens
            tokens = input("\nWhat is your command? (Type 'help' for instructions) ").lower().split()
            # Separate the command from the target
            command = tokens.pop(0)
            target = " ".join(tokens)
            # make sure the user entered a valid command and keep asking the user for a command
            # until a valid command is entered
            if command not in self._commands:
                print("Invalid command! Try again")
                continue
            self._commands[command](target)

            # check if the elf has enough calories.
            if self._calories_needed <= 0:
                break

        if self._calories_needed <= 0:
            print("Congratulations hero! You gave the elf enough food to cure his hangover"
                  " and he slayed the dragon! "
                  "We are very grateful for what you've done.")

    def show_help(self, arg: str = "") -> None:
        """Method to show the current time and all the possible commands a user can execute.

        Params:
            arg (str): An empty string."""
        time_obj = datetime.datetime.now()
        print(f"It is currently {time_obj.hour}:{time_obj.minute}:{time_obj.second}")
        print("Valid commands are:\n"
              "\n- help"
              "\n- ?"
              "\n- talk (put the npc name you want to talk to after this word. Ex: talk elf)"
              "\n- meet (put the npc name you want to talk to after this word. Ex: meet elf)"
              "\n- take (put the item name you want to take after this word. Ex: take pepsi)"
              "\n- give (put the item name you want to give/drop after this word. Ex: give pepsi)"
              "\n- go (put the direction you want to go after this word. Ex: go North)"
              "\n- items (lists the items you currently are holding)"
              "\n- look (allows you to see what is around you)"
              "\n- quit"
              "\n - q"
              "\n- rob"
              "\n- teleport")

    def talk(self, target: str) -> None:
        """Method to talk with an NPC as long as it's in the same area as the user.

        Params:
            target (str): A string representing the NPC the user wishes to talk to. """
        if target in self._npc_dict:
            if self._npc_dict[target] in self._current_location.get_npcs():
                print(self._npc_dict[target].get_message())
            else:
                print("There's no one in this room")
        else:
            print("That creature doesn't exist.")

    def meet(self, target: str) -> None:
        """Method to meet an NPC as long as it's in the same area as the user.

        Params:
            target (str): A string representing the NPC that the player wishes to meet."""
        if target in self._npc_dict:
            if self._npc_dict[target] in self._current_location.get_npcs():
                print(self._npc_dict[target].get_description())
            else:
                print("There's no one in this room")
        else:
            print("That creature doesn't exist")

    def take(self, target: str) -> None:
        """Method to add an item to the user's inventory.

        This method removes the target item from the location that the player is in and then adds
        that item to the player's inventory. The player's weight is increased by the item's weight.

        Params:
            target (str): A string representing the item the user wishes to add to their inventory."""
        for item in self._current_location.get_items():
            if item.get_name() == target:
                self._current_location.remove_item(item)
                self._inventory.append(item)
                self._weight += item.get_weight()
                print(f"You took the {item}")
                return
        print("That item doesn't exist.")

    def give(self, target: str) -> None:
        """Method to drop/give an item in an area or to the elf

        Params:
            target (str): A string representing the item that the user wants to drop."""

        # Loop through all the items in the inventory
        for item in self._inventory:
            # Item matches the item the user wants to drop execute the following
            if item.get_name() == target:
                # Check if the player is in the same location as the elf
                if self._current_location == self._locations[1]:
                    # Checks if the item was edible or not and execute the corresponding outcome
                    if item.get_calories() > 0:
                        self._calories_needed -= item.get_calories()
                        self._inventory.remove(item)
                        self._weight -= item.get_weight()
                        if self._calories_needed > 0:
                            print(f"\nYummy food, more please. How about you bring me "
                                  f"{self._calories_needed} more calories worth in food.")
                        return
                    else:
                        self._inventory.remove(item)
                        self._weight -= item.get_weight()
                        print("\nTHAT TASTED HORRIBLE, BE GONE FROM MY SIGHT!")
                        print("\nThe elf didn't like that item.")
                        self._current_location = self.random_location()
                        print(f"The elf teleported you to a new location: "
                              f"{self._current_location.get_name().capitalize()}")
                        return
                # If the player isn't near the elf then just add the dropped item to this location.
                else:
                    print(f"\nYou dropped {item}")
                    self._current_location.add_item(item)
                    self._weight -= item.get_weight()
                    self._inventory.remove(item)
                    return
        if len(self._inventory) > 0:
            print("\nThat item is not in your inventory")
        else:
            print("\nYour inventory is empty.")

    def go(self, target: str) -> None:
        """Method to change the current location to a new one as long as the direction exists.

        Params:
            target (str): A string representing the direction a player wants to go.
        """
        self._current_location.set_visited()
        if self._weight > 30:
            print(f"You're carrying too much stuff. You currently weigh {self._weight} pounds."
                  f"You need to drop some items to get below 30 pounds to move")
            return

        if target in self._current_location.get_locations():
            self._current_location = self._current_location.get_locations()[target]
            print(f"\nYou are in {self._current_location}")
        else:
            print("\nYou can't go that direction.")

    def show_items(self, args: str = "") -> None:
        """Method to print the weight of player and print their inventory.

        Params:
            args (str): An empty string."""
        print(f"\nYour weight in pounds is: {self._weight}.\n"
              f"The items in your inventory are:")
        if len(self._inventory) == 0:
            print("\nYou are not carrying any items.")
        for item in self._inventory:
            print(f"\n- {item}")

    def look(self, args: str = "") -> None:
        """Method for user to see what objects and NPCs are near them.

        If there are no NPCs or items, this method prints a message to the user informing them.

        Params:
            args (str): An empty string.
        """
        # Print what is in the room
        print(f"\nYou are located in: {self._current_location}")
        print("\nYou see:")

        # print what items are in the room
        if not self._current_location.get_items():
            print("No items here of use.")
        for item in self._current_location.get_items():
            print(f"- {item}")

        print("\nand")

        # print the npcs in the room.
        if not self._current_location.get_npcs():
            print("You are alone.")
        for character in self._current_location.get_npcs():
            print(f"{character.get_name()}")

        # Print the possible directions someone can go from here
        print(f'\nFrom here you may go:')
        for dir in self._current_location.get_locations():
            if self._current_location.get_locations()[dir].get_visited():
                print(f"- {dir} - {self._current_location.get_locations()[dir]}")
            else:
                print(f"- {dir}")

    def quit(self, args: str = "") -> None:
        """Method to print that the player failed.

        Params:
            args (str): An empty string"""
        print("You failed to save Ireland. :(")
        self._run_game = False

    def rob(self, args: str = "") -> None:
        """Method so a player can rob an NPC.

        An NPC can only be robbed if it has a prized food. Else, it is not possible
        for it to be robbed.

        Params:
            args (str): An empty string. """
        has_glock = False
        for npc in self._current_location.get_npcs():
            current_npc = npc
            chance = random.randint(0, 100)
            # check if the npc can be robbed (if it has a prize food item)
            for item in self._inventory:
                if item.get_name() == "glock":
                    has_glock = True
            if current_npc.has_prize_food():
                # Check if glock is in the user's inventory
                if has_glock:
                    # If glock is in inventory then these are the odds of success
                    if chance < 87:
                        print(f"You successfully robbed {current_npc}")
                        print(f"You acquired {current_npc.get_prize_food()}")
                        self._inventory.append(current_npc.get_prize_food())
                        self._weight += current_npc.get_prize_food().get_weight()
                        return
                    else:
                        print(f"You weren't successful in robbing {current_npc}.")
                        return
                # If glock is not in the user's inventory then these are the odds of success
                else:
                    if chance < 47:
                        print(f"You successfully robbed {current_npc}")
                        print(f"You acquired {current_npc.get_prize_food()}")
                        self._inventory.append(current_npc.get_prize_food())
                        self._weight += current_npc.get_prize_food().get_weight()
                        return
                    else:
                        print(f"You weren't successful in robbing {current_npc}")
                        return
            # Print's nps is unrobbable if it has no prize food
            else:
                print(f"It is not possible to rob {current_npc}")
                return
        print("You can't rob the air.")

    def teleport(self, args: str = "") -> None:
        """Method that is called when player's command is teleport.

        Changes the player's current location to a random location in the game and tells the player
        where they teleported to. If they teleported to the same location that they're currently in
        then we print a message telling the player that they failed to teleport. Else, this method
        tells the player where they teleported to.
        Params:
            args (str): An empty string."""
        old_location = self._current_location
        self._current_location = self.random_location()
        if old_location != self._current_location:
            print(f"\nYou are now in {self._current_location}")
            return
        print(f"\nYour teleport was unsuccessful.\nYou are still located in: {self._current_location}.")



def main():
    """Function that is the main method of our program.

    This function will run the game created by the three separate classes."""
    rp = Game()
    rp.play()


if __name__ == "__main__":
    main()
