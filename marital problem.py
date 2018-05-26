m = [
    {
        "mname": "A",
        "station": True,
        "g": "m",
        "p": ["P", "R", "T", "S", " "],
        "en": "",
        "pro": [],
    },
    {
        "mname": "B",
        "station": True,
        "g": "m",
        "p": ["Q", "R", "P", "T", "S"],
        "en": "",
        "pro": [],
    },
    {
        "mname": "C",
        "station": True,
        "g": "m",
        "p": ["P", "R", "S", "Q", " "],
        "en": "",
        "pro": [],
    },
    {
        "mname": "D",
        "station": True,
        "g": "m",
        "p": ["Q", "T", "R", "S", "P"],
        "en": "",
        "pro": [],
    },
    {
        "mname": "E",
        "station": True,
        "g": "m",
        "p": ["P", "Q", "S", "T", " "],
        "en": "",
        "pro": [],
    }
]           # man's data store

f = [
    {
        "mname": "P",
        "station": True,
        "g": "f",
        "p": ["C", "A", "D", "E", "B"],
        "en": "",
        "pro": [],
    },
    {
        "mname": "Q",
        "station": True,
        "g": "f",
        "p": ["B", "C", "E", "D", " "],
        "en": "",
        "pro": [],
    },
    {
        "mname": "R",
        "station": True,
        "g": "f",
        "p": ["B", "E", "D", "A", "C"],
        "en": "",
        "pro": [],
    },
    {
        "mname": "S",
        "station": True,
        "g": "f",
        "p": ["C", "D", "A", "E", " "],
        "en": "",
        "pro": [],
    },
    {
        "mname": "T",
        "station": True,
        "g": "f",
        "p": ["B", "A", "D", "C", "E"],
        "en": "",
        "pro": [],
    }
]       #female's data store


def breakEngagement(p):# judgement whether it is break or engagement
    breakingWith = engagedto(p)
    for i in m:
        if i["mname"] == p:
            if i["en"] != "":
                i["en"] = ""
                i["station"] = True
                print("{} is break with {}.".format(p, breakingWith))

    for j in f:
        if j["mname"] == p:
            if j["en"] != "":
                j["en"] = ""
                j["station"] = True
                print("{} is break with {}.".format(p, breakingWith))


def engagedto(p):# engaged relationship
    for i in m:
        if i["mname"] == p:
            return i["en"]

    for j in f:
        if j["mname"] == p:
            return j["en"]

    return False


def engaged(p):# engaged relationship
    for i in m:
        if i["mname"] == p:
            if i["en"] != "":
                return True

    for j in f:
        if j["mname"] == p:
            if j["en"] != "":
                return True

    return False


def loveMore(p, c1, c2):# rebuild the relationship
    for i in m:
        if i["mname"] == p:
            for x in range(0, len(m)):
                if c1 == i["p"][x]:
                    return c1
                if c2 == i["p"][x]:
                    return c2

    for j in f:
        if j["mname"] == p:
            for x in range(0, len(m)):
                if c1 == j["p"][x]:
                    return c1
                if c2 == j["p"][x]:
                    return c2


def engage(dK, dQ):
    for i in m:
        if i["mname"] == dK:
            i["en"] = dQ
            i["station"] = False

    for j in f:
        if j["mname"] == dQ:
            j["en"] = dK
            j["station"] = False


def GetName(dK, rk):
    for i in m:
        if i["mname"] == dK:
            return i["p"][rk]


def main():
    while (True):
        numberOfPairs = len(m)
        good = 1
        for i in m:
            dramaMan = i["mname"]
            if (i["station"] == False) and (len(i["pro"]) != numberOfPairs):
                good += 1
                if good == numberOfPairs:
                    print("Success engaged!")
                    return

            for x in range(0, numberOfPairs):
                if not engaged(dramaMan):
                    if x not in i["pro"]:
                        i["pro"].append(x)

                        woman = GetName(dramaMan, x)

                        if engaged(woman):
                            CurrentManOfEngaged = engagedto(woman)

                            BetterLover = loveMore(
                                woman, CurrentManOfEngaged, dramaMan)

                            engage(BetterLover, woman)

                            if BetterLover != CurrentManOfEngaged:
                                breakEngagement(CurrentManOfEngaged)
                        else:
                            engage(dramaMan, woman)


def end():#display outcome
    for i in m:
        dramaKing = i["mname"]
        dramaQueen = i["en"]

        print("{} ------ {}".format(dramaKing, dramaQueen))


main()
end()

#reference: https://gist.github.com/joyrexus/9967709
#reference: https://en.wikipedia.org/wiki/Stable_marriage_problem