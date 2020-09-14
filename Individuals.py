import pandas as pd

class Individual():
    def __init__(self,animal_type, scenario):
        self.type = animal_type 
        self.scenario = scenario #to split up different species and pops
        self.corresponding_data = None

        # Mapping that defines the scenario to the correct CSV file
        self.scenarioLink = {
            "study1": "data_1.csv",
            "study2": "data_2.csv",
            "study3": "data_3.csv"
        }

    def retrieve_data(self):
        """ Dynamically read in the data based on the corresponding mapping defined """
        print("Currently loading in data frame for " + self.scenario + " corresponding to " + self.scenarioLink[self.scenario])

        if self.corresponding_data == None:
            self.corresponding_data = pd.read_csv(self.scenarioLink[self.scenario], delimiter = ',', names = ['id', 'first_name', 'last_name', 'animal_type'], skiprows=1)
            return self.corresponding_data
        return self.corresponding_data

"""
This is an example with a bunch of "Individual" class instantiations
"""

# Animal_Type, Scenario, Corresponding File Name
individual1 = Individual("lizard", "study1")
individual2 = Individual("bear", "study2")
individual3 = Individual("cat", "study3")

# Putting all the individuals into a list to iterate over
individuals = [individual1, individual2, individual3]

for individual in individuals:
    print("--------\n")
    loaded_df = individual.retrieve_data();
    for name_index in range(len(loaded_df['first_name'])):
        print("First name is: " + loaded_df['first_name'][name_index])