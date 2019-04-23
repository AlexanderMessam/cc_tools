import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    ### Begin Add Code Here ###
    #Loop through the json_data
    with open(json_data, 'r') as f:
        jsonData = json.load(f)

    # making Platform objects
    platformList = []
    for i in range(0,len(jsonData["Game Library"])):
        platformList.append(test_data.Platform(jsonData["Game Library"][i]["Platform"]["Platform Name"], jsonData["Game Library"][i]["Platform"]["Launch Year"]))

    # making Game objects
    gameList = []
    for i in range(0,len(jsonData["Game Library"])):
       gameList.append(test_data.Game(jsonData["Game Library"][i]["Title"], platformList[i], jsonData["Game Library"][i]["Year"]))

    # adding game objects to Game Library
    game_library.add_game(gameList[0])
    game_library.add_game(gameList[1])
    game_library.add_game(gameList[2])

    return game_library


#Part 2
input_json_file = "data/test_data.json"

gameLibrary = (make_game_library_from_json(input_json_file))
print(gameLibrary)
