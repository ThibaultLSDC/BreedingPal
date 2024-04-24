import json
import random as rd

from utils import Pal
from search import search_depth
from palInfo import loadPalData
from data import matrix_encoded, pal_to_int, passives_to_int
import time

with open("./resources/data/en-GB/passives.json", "r") as f:
    passiveData = json.load(f)

palData = loadPalData("./Level.sav")

pals = []
for k in range(len(palData["00000000-0000-0000-0000-000000000001"])):
    pal = Pal(name=palData['00000000-0000-0000-0000-000000000001'][k].GetName(), sex=0 if palData['00000000-0000-0000-0000-000000000001'][k].GetGender() == "Male ♂" else 1, passives=set([passiveData[skill]["Name"] for skill in palData['00000000-0000-0000-0000-000000000001'][k].GetSkills()]))
    pal = Pal(name=pal_to_int[pal.name], sex=pal.sex, passives=frozenset([passives_to_int[skill] for skill in pal.passives]))
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
