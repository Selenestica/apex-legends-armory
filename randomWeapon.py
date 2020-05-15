import random as r

barrel_stabs = ["none", "1", "2", "3", "4"]
hop_ups = [["none", "doubletap"], ["none", "choke"], [
    "none", "hammerpoint"], ["none", "selectfire"], ["none", "skullpiercer"]]
mags_bolts_stocks = ["none", "1", "2", "3"]
optics = {"sniper": ["none", "1xholo", "classic", "1x2xvar", "bruiser", "6x", "ranger", "2x4xaog", "4x8x", "digi"], "lmg_ar": [
    "none", "1xholo", "classic", "1x2xvar", "bruiser", "ranger", "2x4xaog"], "sg_smg_pist": ["none", "1xholo", "classic", "1x2xvar", "bruiser", "digi"]}


def mastiff():
    sg_bolt = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    return("Mastiff\n    Bolt: " + sg_bolt + '\n    Optics: ' + optic)


def kraber():
    return("Kraber")


def lstar():
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("L-Star\n    Stock: " + stock + '\n    Optics: ' + optic)


def devotion():
    return("Devotion")


def r99():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    stock = r.choice(mags_bolts_stocks)
    return("R-99\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def longbow():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sniper"])
    stock = r.choice(mags_bolts_stocks)
    hop_up = r.choice(hop_ups[4])
    return("Longbow\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock + "\n    Hop-up: " + hop_up)


def peacekeeper():
    return("Peacekeeper")


def hemlok():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("Hemlok\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def prowler():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    stock = r.choice(mags_bolts_stocks)
    hop_up = r.choice(hop_ups[3])
    return("Prowler\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock + "\n    Hop-up: " + hop_up)


def r301():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("R-301\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def g7():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    hop_up = r.choice(hop_ups[0])
    return("G7\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock + "\n    Hop-up: " + hop_up)


def wingman():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    hop_up = r.choice(hop_ups[4])
    return("Wingman\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Hop-up: " + hop_up)


def spitfire():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("Spitfire\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def havoc():
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("Havoc\n    Stock: " + stock + '\n    Optics: ' + optic)


def sentinel():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sniper"])
    stock = r.choice(mags_bolts_stocks)
    return("Sentinel\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def eva8():
    sg_bolt = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    hop_up = r.choice(hop_ups[0])
    return("EVA-8\n    Bolt: " + sg_bolt + '\n    Optics: ' +
           optic + "\n    Hop-up: " + hop_up)


def flatline():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["lmg_ar"])
    stock = r.choice(mags_bolts_stocks)
    return("Flatline\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def chargerifle():
    optic = r.choice(optics["sniper"])
    stock = r.choice(mags_bolts_stocks)
    return("Charge Rifle\n    Optics: " + optic + "\n    Stock: " + stock)


def re45():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    return("RE-45\n    Barrel: " + barrel +
           '\n    Mag: ' + mag + "\n    Optics: " + optic)


def tripletake():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sniper"])
    stock = r.choice(mags_bolts_stocks)
    hop_up = r.choice(hop_ups[1])
    return("Triple Take\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock + "\n    Hop-up: " + hop_up)


def alternator():
    barrel = r.choice(barrel_stabs)
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    stock = r.choice(mags_bolts_stocks)
    return("Alternator\n    Barrel: " + barrel + "\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Stock: " + stock)


def p2020():
    mag = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    hop_up = r.choice(hop_ups[2])
    return("P2020\n    Mag: " + mag +
           "\n    Optics: " + optic + "\n    Hop-up: " + hop_up)


def mozambique():
    sg_bolt = r.choice(mags_bolts_stocks)
    optic = r.choice(optics["sg_smg_pist"])
    hop_up = r.choice(hop_ups[2])
    return("Mozambique\n    Bolt: " + sg_bolt +
           '\n    Optics: ' + optic + "\n    Hop-up: " + hop_up)


weapons = [mastiff, kraber, lstar, devotion, r99, longbow, peacekeeper, hemlok, prowler, r301, g7, wingman,
           spitfire, havoc, sentinel, eva8, flatline, chargerifle, re45, tripletake, alternator, p2020, mozambique]

rand_weapon1 = r.choice(weapons)
rand_weapon2 = r.choice(weapons)
rand_weapon3 = r.choice(weapons)
rand_weapon4 = r.choice(weapons)

print("\n============Player 1============\n" +
      rand_weapon1() + "\n" + rand_weapon2() + "\n")
print("\n============Player 2============\n" +
      rand_weapon3() + "\n" + rand_weapon4() + "\n")

