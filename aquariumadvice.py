class Fish:
    """
    Stores ideal conditions for a given species of fish.
    """
    def __init__(self, species, size, pH_range, temp_range, diet, aggressive, tank_size_minimum, info):
        """
        inputs the parameter of the fish's species name.
        """
        self._species = species
        self._size = size
        self._aggressive = aggressive
        self._pH_range = pH_range
        self._diet = diet
        self._temp_range = temp_range
        self._tank_size_minimum = tank_size_minimum
        self._info = info

    def get_species(self):
        """
        Returns species
        """
        return self._species

    def get_size(self):
        """
        Returns size
        """
        return self._size

    def get_pH_range(self):
        """
        Returns pH_range
        """
        return self._pH_range

    def get_temp_range(self):
        """
        Returns temp_range
        """
        return self._temp_range

    def get_diet(self):
        """
        Returns diet
        """
        return self._diet

    def get_aggressive(self):
        """
        Returns aggressive
        """
        return self._aggressive

    def get_tank_size_minimum(self):
        """
        Returns tank_size_minimum
        """
        return self._tank_size_minimum

    def get_info(self):
        """
        Returns information about the species
        """
        return self._info


def ideal_tank_setup(tank_size, list_of_species, list_of_quantities):
    """
    This is a function that was my first attempt for tank setup that I may revisit.
    """
    space_used = 0
    for fish_1 in list_of_species:
        for amount_1 in list_of_quantities:
            space_used += fish_1.get_size() * amount_1
    if tank_size > space_used:
        return 'You have too many fish in your tank.'
    else:
        for fish_variable in list_of_all_fish:
            if fish_variable.get_size <= space_used:
                amount_to_add = space_used//fish_variable.get_size
                return str(amount_to_add) + " " + fish_variable.get_species

# Data of fish species (will be added to)
harlequin_rasbora = Fish('Harlequin Rasbora', 1, [7, 8], [70, 80], 'N/A', False, 5, "The harlequin rasbora is a small fish in the family Cyprinidae. The species became an instant favorite among aquarists after its introduction in the early 1900s and is the best known and most widely kept species among the rasboras.")
betta_fish = Fish("Betta Fish", 3, [6.5, 8], [75, 80], 'N/A', True, 3, "The Siamese fighting fish, commonly known as the betta, is a freshwater fish native to Southeast Asia, namely Cambodia, Laos, Myanmar, Malaysia, Indonesia, Thailand, and Vietnam.")
species_list = [harlequin_rasbora, betta_fish]


# User enters tank info
print('What is the tank size in gallons?')
tank_size_1 = int(input())

# User enters fish info
user_not_done = "Yes"
while user_not_done == "Yes":
    print("What is the species name of one of your fish species?")
    species_1 = input()
    print('How many of these fish do you have?')
    quantity_1 = int(input())

    # Locates the fish mentioned
    for species in species_list:
        if species_1 == species.get_species():
            tank_size_1 -= species.get_size() * quantity_1
            print(species.get_info())

    # Sees if maximum is exceeded
    if int(tank_size_1) < 0:
        tank_size_2 = abs(int(tank_size_1))
        print("Maximum size exceeded by " + str(tank_size_2) + " gallons.")
        break

    # Asks if user wants to continue entering fish
    else:
        print("Would you like to enter another fish? (Yes or No)")
        user_not_done = input()



