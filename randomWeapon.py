import random
weapons = ["mastiff", "kraber", "lstar", "devotion", "r99", "longbow", "peacekeeper", "hemlok", "prowler", "r301", "g7", "wingman",
           "spitfire", "havoc", "sentinel", "eva8", "flatline", "chargerifle", "re45", "tripletake", "alternator", "p2020", "mozambique"]
barrel_stabs = ["none", 1, 2, 3, 4]
light_mags = [1, 2, 3]
heavy_mags = [1, 2, 3]
sniper_mags = [1, 2, 3]
hop_ups = ["doubletap", "choke", "hammerpoint", "selectfire", "skullpiercer"]
stand_stocks = [1, 2, 3]
snipe_stocks = [1, 2, 3]
stocks = [stand_stocks, snipe_stocks]
mags = [light_mags, heavy_mags, sniper_mags]
bolts = ["none", 1, 2, 3]
rand_weapon = random.choice(weapons)
print(rand_weapon)
