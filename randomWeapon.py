import random
weapons = ["mastiff", "kraber", "lstar", "devotion", "r99", "longbow", "peacekeeper", "hemlok", "prowler", "r301", "g7", "wingman",
           "spitfire", "havoc", "sentinel", "eva8", "flatline", "chargerifle", "re45", "tripletake", "alternator", "p2020", "mozambique"]
barrel_stabs = [0, 1, 2, 3, 4]
#hop_ups = [{"ev8_g7": [0, "doubletap"]}, {"pk_tt": [0, "choke"]}, {"p20_moz": [0, "hammerpoint"]}, {"prow_hav": [0, "selectfire"]}, {"lb_wing": [0, "skullpiercer"]}]
hop_ups = [[0, "doubletap"], [0, "choke"], [
    0, "hammerpoint"], [0, "selectfire"], [0, "skullpiercer"]]
stocks = {"stand_stock": [0, 1, 2, 3], "snipe_stock": [0, 1, 2, 3]}
mags = [{"light_mag": [0, 1, 2, 3]}, {
    "heavy_mag": [0, 1, 2, 3]}, {"sniper_mag": [0, 1, 2, 3]}]
sg_bolts = [0, 1, 2, 3]
optics = [0, 1, 2, 3, 4, 5]
rand_weapon = random.choice(weapons)
# print(rand_weapon)
print(random.choice(stocks["snipe_stock"]))


def mastiff():
    bolt = random.choice(sg_bolts)
    optic = random.choice(optics)
    return (f"Mastiff: {bolt}, {optic}")


mastiff()
print(mastiff())
