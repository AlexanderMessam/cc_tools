import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    with open(json_data, 'r') as f:
        data = json.load(f)

    # making Platform objects
    chipCallenge1Plat = test_data.Platform("Atari Lynx", "1989")
    chipCallenge2Plat = test_data.Platform("Atari Lynx", "1989")
    animalCrossingPlat = test_data.Platform("Game Cube", "2001")

    # making Game objects
    chipCallenge1 = test_data.Game("Chip's Challenge", chipCallenge1Plat, "1989")
    chipCallenge2 = test_data.Game("Chip's Challenge 2", chipCallenge2Plat, "2015")
    animalCrossing = test_data.Game("Animal Crossing", animalCrossingPlat, "2001")

    # adding game objects to Game Library
    game_library.add_game(chipCallenge1)
    game_library.add_game(chipCallenge2)
    game_library.add_game(animalCrossing)

    return game_library


#Part 2
input_json_file = "data/test_data.json"

gameLibrary = (make_game_library_from_json(input_json_file))
print(gameLibrary)
