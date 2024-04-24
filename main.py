import json
import random as rd

from utils import Pal
from search import search_depth
from palInfo import loadPalData
from data import matrix_encoded, pal_to_int, passives_to_int
import time

with open("./resources/data/en-GB/passives.json", "r") as f:
    passiveData = json.load(f)

palData, palguidmanager = loadPalData("./Level.sav")

pals = []
for player, player_id in palguidmanager.GetPlayerslist().items():
    for pal in palData[player_id]:
        pal = Pal(name=pal_to_int[pal.GetName()], sex=0 if pal.GetGender() == "Male ♂" else 1, passives=frozenset([passives_to_int[passiveData[skill]["Name"]] for skill in pal.GetSkills()]), player=player)
        pals.append(pal)

if __name__ == '__main__':
    start = time.time()
    target_name = 'Anubis'
    target_skill = set(["Musclehead", "Ferocious", "Vanguard", "Hooligan"])

    target = Pal(name=pal_to_int[target_name], sex=0, passives=frozenset([passives_to_int[skill] for skill in target_skill]))
    result = search_depth(target, pals, matrix_encoded, 3)

    if result:
        print(result.get_ancestors())

    print(f"Time taken: {time.time() - start}s")
