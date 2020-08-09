# CLGen-lib.py
# Cepheus Light character generator by Omer Golan-Joel
# v0.2 - August 9th, 2020
# This is open source code, feel free to use it for any purpose
# contact me at golan2072@gmail.com

# Import modules

import collections
import random
import stellagama

# Careers

careers = {
    'Agent': {"name": 'Agent', "qualification": 6, "qualification DM": "INT", 'survival': 6, "survival DM": "INT",
              "reenlistment": 6, "advancement": 7, "advancement DM": "EDU", "ranks": (
            "Agent", "Special Agent", "Sp. Agent in Charge", "Unit Chief", "Section Chief", "Assistant Director",
            "Director"),
              "rank skills": {0: "Investigation", 4: "Administration"},
              "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
              "muster materials": (
                  "Low Passage", "+1 INT", "Weapon", "Contact", "+1 SOC", "High Passage", "Low Passage"),
              "personal": ("+1 DEX", '+1 END', "+1 INT", "+1 EDU", "Athletics", "Carousing"),
              "service": ("Administration", "Computer", "Streetwise", "Investigation", "Leadership", "Stealth"),
              "specialist": ("Gun Combat", "Melee Combat", "Investigation", "Leadership", "Driving", "Recon"),
              "advanced education": ("Administration", "Computer", "Liaison", "Science", "Medicine", "Leadership")},
    'Army': {"name": 'Army', "qualification": 5, "qualification DM": "END", 'survival': 5, "survival DM": "END",
             "reenlistment": 5, "advancement": 8, "advancement DM": "EDU", "ranks": (
            "Private", "Lieutenant", "Captain", "Major", "Lt. Colonel", "Colonel",
            "General"),
             "rank skills": {0: "Gun Combat", 1: "Leadership", 6: "SOC +1"},
             "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
             "muster materials": ("Low Passage", "+1 INT", "Weapon", "Mid Passage", "Weapon", "High Passage", "+1 SOC"),
             "personal": ("+1 STR", '+1 DEX', "+1 END", "Athletics", "Melee Combat", "Carousing"),
             "service": ("Repair", "Gun Combat", "Gunnery", "Melee Combat", "Recon", "Driving"),
             "specialist": ("Computer", "Demolitions", "Gun Combat", "Melee Combat", "Survival", "Grav Vehicle"),
             "advanced education": (
                 "Administration", "Computer", "Jack-o-Trades", "Medicine", "Leadership", "Tactics")},
    "Belter": {"name": 'Belter', "qualification": 4, "qualification DM": "INT", 'survival': 7, "survival DM": "DEX",
               "reenlistment": 5, "advancement": 6, "advancement DM": "INT", "ranks": (
            "Miner", "Roughneck", "Tool Pusher", "Manager", "Director", "Vice-President",
            "Executive Officer"),
               "rank skills": {0: "Zero-G", 4: "Administration"},
               "muster cash": (1000, 5000, 5000, 10000, 50000, 100000, 250000),
               "muster materials": (
                   "Low Passage", "+1 INT", "Vacc Suit", "Mid Passage", "+1 EDU", "Prospector", "Explorer's Society"),
               "personal": ("+1 STR", '+1 DEX', "Athletics", "Jack-o-Trades", "Melee Combat", "Carousing"),
               "service": ("Repair", "Demolitions", "Piloting", "Computer", "Zero-G", "Repair"),
               "specialist": ("Engineering", "Computer", "Repair", "Science", "Zero-G", "Gunnery"),
               "advanced education": (
                   "Administration", "Medicine", "Science", "Engineering", "Grav Vehicle", "Liaison")},
    'Colonist': {"name": 'Colonist', "qualification": 5, "qualification DM": "END", 'survival': 5, "survival DM": "END",
                 "reenlistment": 5, "advancement": 8, "advancement DM": "EDU", "ranks": (
            "Citizen", "District Leader", "District Delegate", "Council Adviser", "Councillor", "Lieutenant Governor",
            "Governor"),
                 "rank skills": {0: "Survival", 3: "Liaison"},
                 "muster cash": (1000, 5000, 5000, 5000, 10000, 20000, 50000),
                 "muster materials": (
                     "Low Passage", "+1 INT", "Weapon", "Mid Passage", "Mid Passage", "High Passage", "+1 SOC"),
                 "personal": ("+1 STR", '+1 DEX', "+1 END", "+1 INT", "Athletics", "Carousing"),
                 "service": ("Repair", "Gun Combat", "Animals", "Melee Combat", "Survival", "Driving"),
                 "specialist": ("Recon", "Leadership", "Jack-o-Trades", "Watercraft", "Animals", "Grav Vehicle"),
                 "advanced education": ("Liaison", "Science", "Medicine", "Computer", "Administration", "Aircraft")},
    'Elite': {"name": 'Elite', "qualification": 0, "qualification DM": "SOC", 'survival': 5, "survival DM": "INT",
              "reenlistment": 6, "advancement": 8, "advancement DM": "INT", "ranks": (
            "Analyst", "Supervisor", "Manager", "Director", "Managing Director", "Vice President",
            "President"),
              "rank skills": {0: "Administration", 3: "Liaison"},
              "muster cash": (2000, 10000, 20000, 40000, 50000, 100000, 200000),
              "muster materials": (
                  "Contact", "+1 EDU", "+1 SOC", "High Passage", "+1 INT", "Explorer's Society", "Yacht"),
              "personal": ("+1 SOC", '+1 DEX', "+1 END", "Melee Combat", "Athletics", "Carousing"),
              "service": ("Administration", "Deception", "Carousing", "Computer", "Leadership", "Grav Vehicle"),
              "specialist": ("Recon", "Leadership", "Jack-o-Trades", "Watercraft", "Animals", "Grav Vehicle"),
              "advanced education": ("Administration", "Medicine", "Computer", "Liaison", "Carousing", "Science")},
    'Marine': {"name": 'Marine', "qualification": 6, "qualification DM": "INT", 'survival': 7, "survival DM": "END",
               "reenlistment": 6, "advancement": 6, "advancement DM": "SOC", "ranks": (
            "Trooper", "Lieutenant", "Captain", "Major", "Lt. Colonel", "Colonel",
            "Brigadier"),
               "rank skills": {0: "Gun Combat", 1: "Leadership", 3: "Tactics"},
               "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
               "muster materials": (
                   "+1 EDU", "Weapon", "Mid Passage", "+1 SOC", "High Passage", "Explorer's Society", "+1 EDU"),
               "personal": ("+1 STR", '+1 DEX', "+1 END", "+1 INT", "+1 EDU", "Carousing"),
               "service": ("Heavy Weapons", "Athletics", "Gun Combat", "Gunnery", "Melee Combat", "Zero-G"),
               "specialist": ("Repair", "Demolitions", "Leadership", "Survival", "Recon", "Grav Vehicle"),
               "advanced education": ("Administration", "Computer", "Piloting", "Medicine", "Science", "Tactics")},
    'Merchant': {"name": 'Merchant', "qualification": 6, "qualification DM": "INT", 'survival': 7, "survival DM": "END",
                 "reenlistment": 6, "advancement": 4, "advancement DM": "INT", "ranks": (
            "Crewmember", "Deck Cadet", "Fourth Officer", "Third Officer", "Second Officer", "First Officer",
            "Captain"),
                 "rank skills": {0: "Steward", 3: "Pilot"},
                 "muster cash": (1000, 5000, 10000, 20000, 20000, 50000, 100000),
                 "muster materials": (
                     "Low Passage", "+1 EDU", "Weapon", "Contact", "High Passage", "Explorer's Society", "Free Trader"),
                 "personal": ("+1 STR", '+1 DEX', "Athletics", "Zero-G", "Melee Combat", "Carousing"),
                 "service": ("Repair", "Liaison", "Gun Combat", "Admin", "Streetwise", "Steward"),
                 "specialist": ("Liaison", "Gunnery", "Jack-o-Trades", "Medicine", "Engineering", "Piloting"),
                 "advanced education": (
                     "Administration", "Engineering", "Medicine", "Computers", "Science", "Tactics")},
    'Navy': {"name": 'Navy', "qualification": 6, "qualification DM": "INT", 'survival': 6, "survival DM": "INT",
             "reenlistment": 5, "advancement": 7, "advancement DM": "EDU", "ranks": (
            "Starhand", "Ensign", "Lieutenant", "Lt. Commander", "Commander", "Captain",
            "Commodore"),
             "rank skills": {0: "Zero-G", 1: "Leadership", 3: "Tactics", 6: "+1 SOC"},
             "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
             "muster materials": (
                 "Low Passage", "+1 EDU", "Weapon", "Mid Passage", "+1 SOC", "High Passage", "Explorer's Society"),
             "personal": ("+1 STR", '+1 DEX', "Athletics", "+1 INT", "+1 EDU", "Carousing"),
             "service": ("Repair", "Engineering", "Gun Combat", "Gunnery", "Melee Combat", "Zero-G"),
             "specialist": ("Jack-o-Trades", "Repair", "Engineering", "Leadership", "Piloting", "Jack-o-Trades"),
             "advanced education": ("Administration", "Computer", "Engineering", "Medicine", "Science", "Tactics")},
    'Pirate': {"name": 'Pirate', "qualification": 5, "qualification DM": "DEX", 'survival': 7, "survival DM": "DEX",
               "reenlistment": 5, "advancement": 6, "advancement DM": "INT", "ranks": (
            "Crewmember", "Corporal", "Lieutenant", "Lt. Commander", "Commander", "Captain",
            "Dread Pirate"),
               "rank skills": {0: "Melee Combat", 2: "Piloting"},
               "muster cash": (1000, 5000, 10000, 20000, 50000, 100000, 250000),
               "muster materials": (
                   "+1 INT", "Weapon", "High Passage", "+1 SOC", "High Passage", "Corsair", "+1 INT"),
               "personal": ("+1 STR", '+1 DEX', "+1 END", "Melee Combat", "Stealth", "Recon"),
               "service": ("Streetwise", "Repair", "Gun Combat", "Melee Combat", "Stealth", "Recon"),
               "specialist": ("Zero-G", "Computer", "Engineering", "Gunnery", "Tactics", "Piloting"),
               "advanced education": (
                   "Computer", "Investigation", "Jack-o-Trades", "Medicine", "Administration", "Science")},
    'Rogue': {"name": 'Rogue', "qualification": 5, "qualification DM": "DEX", 'survival': 5, "survival DM": "DEX",
              "reenlistment": 4, "advancement": 8, "advancement DM": "INT", "ranks": (
            "Independent", "Associate", "Made Soldier", "Lieutenant", "Underboss", "Consigliere",
            "Boss"),
              "rank skills": {0: "Streetwise", 2: "Gun Combat"},
              "muster cash": (1000, 5000, 5000, 5000, 10000, 20000, 50000),
              "muster materials": (
                  "Low Passage", "+1 INT", "Weapon", "Contact", "Weapon", "Mid Passage", "+1 SOC"),
              "personal": ("+1 STR", '+1 DEX', "+1 END", "Athletics", "Melee Combat", "Carousing"),
              "service": ("Streetwise", "Repair", "Gun Combat", "Deception", "Stealth", "Recon"),
              "specialist": ("Computer", "Repair", "Carousing", "Admin", "Recon", "Deception"),
              "advanced education": (
                  "Survival", "Engineering", "Jack o' Trades", "Medicine", "Investigation", "Tactics")},
    'Scholar': {"name": 'Scholar', "qualification": 6, "qualification DM": "EDU", 'survival': 4, "survival DM": "INT",
                "reenlistment": 5, "advancement": 9, "advancement DM": "EDU", "ranks": (
            "Student", "Researcher", "Research Professor", "Assistant Professor", "Associate Professor", "Professor",
            "Distinguished Professor"),
                "rank skills": {0: "Admin", 3: "Liaison"},
                "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
                "muster materials": (
                    "Contact", "+1 EDU", "+1 INT", "Mid Passage", "+1 SOC", "High Passage", "Research Vessel"),
                "personal": ("+1 STR", '+1 DEX', "+1 END", "+1 INT", "+1 EDU", "Carousing"),
                "service": ("Admin", "Computer", "Medicine", "Liaison", "Investigation", "Science"),
                "specialist": ("Survival", "Admin", "Medicine", "Science", "Repair", "Carousing"),
                "advanced education": ("Piloting", "Computer", "Engineering", "Medicine", "Jack o' Trades", "Science")},
    'Scout': {"name": 'Scout', "qualification": 6, "qualification DM": "INT", 'survival': 7, "survival DM": "END",
                "reenlistment": 6, "advancement": 6, "advancement DM": "INT", "ranks": (
            "Scout", "", "", "Senior Scout", "", "", "Director",
            "Distinguished Professor"),
                "rank skills": {0: "Piloting", 3: "SCience"},
                "muster cash": (1000, 5000, 10000, 10000, 20000, 50000, 50000),
                "muster materials": (
                    "Low Passage", "+1 INT", "Weapon", "Mid Passage", "Vacc Suit", "Scout Ship", "Explorer's Society"),
                "personal": ("+1 STR", '+1 DEX', "Athletics", "Jack o' Trades", "+1 EDU", "Melee Combat"),
                "service": ("Repair", "Computer", "Gun Combat", "Piloting", "Recon", "Piloting"),
                "specialist": ("Engineering", "Gunnery", "Science", "Piloting", "Investigation", "Stealth"),
                "advanced education": ("Admin", "Computer", "Grav Vehicle", "Medicine", "Science", "Tactics")}
}

# Other data

melee_weapons = (
    "Axe", "Cudgel", "Dagger", "Spear", "Staff", "Sword", "Broadsword", "Great Axe", "Cutlass", "Machete", "Stun Prod",
    "Vibro-Blade")
guns = ("Bow", "Crossbow", "Revolver", "Shotgun", "Autopistol", "Carbine", "Rifle", "Submachinegun", "Assault Rifle",
        "Body Pistol", "Snub Revolver", "Accelerator Rifle", "Stunner")
skills = (
    "Administration", "Aircraft", "Animals", "Athletics", "Carousing", "Computer", "Deception", "Demolitions",
    "Driving",
    "Engineering", "Grav Vehicle", "Gun Combat", "Gunnery", "Heavy Weapons", "Investigation", "Jack-o-Trades",
    "Leadership",
    "Liaison", "Medicine", "Melee Combat", "Piloting", "Science", "Stealth", "Steward", "Steward", "Streetwise",
    "Survival",
    "Tactics", "Recon", "Repair", "Watercraft", "Zero-G")
homeworlds = {"High-Tech World": ("Computer", "Grav Vehicles", "Streetwise"),
              "Colony": ("Driving", "Watercraft", "Survival"), "Inhospitable Outpost": ("Repair", "Science", "Zero-G"),
              "Primitive Backwater": ("Animals", "Recon", "Survival")}


# Functions

def name_gen(sex):
    name = ""
    if sex == "male":
        return stellagama.random_line("malenames.txt")
    elif sex == "female":
        return stellagama.random_line("femalenames.txt")
    else:
        return 'Tokay'


def add_possession(possessions, item):
    if item in possessions:
        possessions[item] += 1
    else:
        possessions[item] = 1
    return possessions


def skill_stringer(input_dict):
    return ', '.join('-'.join((k, str(v))) for k, v in sorted(input_dict.items()))


def possession_stringer(input_dict):
    return ', '.join(
        ' x'.join((k, str(v))) for k, v in sorted(input_dict.items()))


def upp_stringer(upp_dict):
    output_list = []
    for value in upp_dict.values():
        output_list.append(str(stellagama.pseudo_hex(value)))
    return ''.join(output_list)


def career_choice(upp_dict):
    if max(upp_dict, key=upp_dict.get) == "DEX":
        career = random.choice(["Pirate", "Rogue"])
    elif max(upp_dict, key=upp_dict.get) == "END":
        career = random.choice(["Army", "Colonist"])
    elif max(upp_dict, key=upp_dict.get) == "INT":
        career = random.choice(["Agent", "Belter", "Marine", "Merchant", "Navy", "Scout"])
    elif max(upp_dict, key=upp_dict.get) == "EDU":
        career = random.choice(["Navy", "Scholar"])
    elif max(upp_dict, key=upp_dict.get) == "SOC":
        career = "Elite"
    else:
        career = "Colonist"
    return career


def upp_dms(upp_dict):
    characteristic_dm = (-2, -2, -2, -1, -1, -1, 0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4)
    dms = {"STR": characteristic_dm[upp_dict["STR"]], "DEX": characteristic_dm[upp_dict["DEX"]],
           "END": characteristic_dm[upp_dict["END"]], "INT": characteristic_dm[upp_dict["INT"]],
           "EDU": characteristic_dm[upp_dict["EDU"]], "SOC": characteristic_dm[upp_dict["SOC"]]}
    return dms


def benefit_choice(rank, benefit_list):
    roll = stellagama.dice(1, 6)
    if rank >= 5:
        roll += 1
    return benefit_list[roll - 1]


# Classes


class Character:
    def __init__(self):
        self.upp = {"STR": stellagama.dice(2, 6), "DEX": stellagama.dice(2, 6), "END": stellagama.dice(2, 6),
                    "INT": stellagama.dice(2, 6), "EDU": stellagama.dice(2, 6), "SOC": stellagama.dice(2, 6)}
        self.upp_dms = upp_dms(self.upp)
        self.history = []
        self.skills = []
        self.possessions = []
        self.rank = 0
        self.terms = 0
        self.cash = 0
        self.title = ""
        self.status = ""
        self.sex = random.choice(["male", "female"])
        self.name = name_gen(self.sex)
        self.surname = stellagama.random_line("surnames.txt")
        self.career = career_choice(self.upp)
        self.age = 18
        self.homeworld = random.choice(["High-Tech World", "Colony", "Inhospitable Outpost", "Primitive Backwater"])
        self.skills.append(random.choice(homeworlds[self.homeworld]))
        # Enlistment
        enlistment = stellagama.dice(2, 6)
        enlistment += self.upp_dms[careers[self.career]["qualification DM"]]
        if enlistment >= careers[self.career]["qualification"]:
            self.career = self.career
            self.history.append(f"Successfully enlisted into the {self.career}")
        else:
            self.career = random.choice(["Colonist", "Rogue", "Marine", "Merchant", "Navy", "Scout"])
            self.history.append(f"Drafted into the {self.career}")
        # Career generation loop
        in_career = True
        while in_career:
            self.terms += 1
        # Survival
            survival = stellagama.dice(2,6)
            survival += self.upp_dms[careers[self.career]["survival DM"]]
            if survival >= careers[self.career]["survival"]:
                self.age += 4
            else:
                self.status = "DECEASED"
                in_career = False
        # Skills
            if self.terms == 1:
                for i in range (0, 2):
                    skill_table = random.choice(("personal", "service", "specialist", "advanced education"))
                    self.skills.append(random.choice(careers[self.career][skill_table]))
            else:
                skill_table = random.choice(("personal", "service", "specialist", "advanced education"))
                self.skills.append(random.choice(careers[self.career][skill_table]))
            if self.rank in careers[self.career]["rank skills"]:
                    self.skills.append(careers[self.career]["rank skills"][self.rank])
        # Advancement
            if self.rank < 6:
                advancement = stellagama.dice(2,6)
                advancement += self.upp_dms[careers[self.career]["advancement DM"]]
                if advancement >= careers[self.career]["advancement"]:
                    self.rank += 1
                    skill_table = random.choice(("personal", "service", "specialist", "advanced education"))
                    self.skills.append(random.choice(careers[self.career][skill_table]))
                else:
                    pass
            else:
                pass


# Test Area
