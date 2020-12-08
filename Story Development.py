# This is a casual route story:

input_gender = input("Enter your gender: ")
input_fname = input("Enter your first name: ")
input_lname = input("Enter your last name: ")
occupation_list = ['aristocrat', '']
gender = ""
player_name = input_fname
player_lname = input_lname

player_0 = [gender, player_name]
player_inventory = []
player_status = {}

options_chapter_1 = {
    "options_0": {"A": "Take the pathway nonchalantly.",
                  "B": '"Ooooo. is that a bird?"',
                  "C": "Search around for a bit.",
                  "D": "Take the pathway carefully.",
                  },
    "options_1": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_2": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_3": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_4": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_5": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_6": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_7": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_8": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_9": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_10": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_11": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_12": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_13": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_14": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_15": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_16": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_17": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_18": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_19": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
    "options_20": {"A": "",
                  "B": "",
                  "C": "",
                  "D": "",
                  },
}


class player:
    def __init__(self, health, defense, equipdura):
        self.health = health
        self.defense = defense
        self.equipdura = equipdura

class damage:
    def __init__(self, poison, blunt, slash, burning, freezing, drowning, magic, random):
        self.poison = poison
        self.blunt = blunt
        self.slash = slash
        self.burning = burning
        self.freezing = freezing
        self.drowning = drowning
        self.magic = magic
        self.random = random

CQC_Weapons = ['longsword', 'mace', 'shortsword', 'dagger', 'punches', 'kicks', 'kitchenknife', 'treebranch', 'pan',
               'stick', 'rock', 'staff', 'random',]

class CQCWeapons:
    def __init__(self, longsword, mace, shortsword, dagger, punches, kicks, kitchenknife, treebranch, pan, stick, rock,
                 staff, random):
        self.longsword = longsword
        self.mace = mace
        self.shortsword = shortsword
        self.dagger = dagger
        self.punches = punches
        self.kicks = kicks
        self.kitchenknife = kitchenknife
        self.treebranch = treebranch
        self.pan = pan
        self.stick = stick
        self.rock = rock
        self.staff =staff
        self.random = random

ranged_weapons = ['longbow', 'shortbow', 'crossbow', 'thrownrock', 'musket',]

class rangedweapons:
    def __init__(self, longbow, shortbow, crossbow, thrownrock, musket):
        self.longbow = longbow
        self.shortbow = shortbow
        self.crossbow = crossbow
        self.thrownrock = thrownrock
        self.musket = musket

print("\n___Introduction___")
print(f"\nYour name is {player_name.title()}, and your gender is {gender.title()}. You will begin your journey"
      f"in this new world. \nPlease make careful choices as it will affect the course of the story.")

print("\n\n___Chapter 1: Awakening___\nYou wake up inside of a tomb. You wake up confused not knowing what is going on."
      "\nYou get out of your coffin only to see a wooden door at the end of the room.")

tomb_event = True
while tomb_event:
    tomb_door = input("Do you open it? (yes/no) ")
    if tomb_door == 'yes':
        print(f"{player_name.title()} opens the wooden door and is introduced to the sunlight of the outside world.")
        break
    elif tomb_door == 'no':
        print(f"{player_name.title()} chose not to open the wooden door and stood still confused.")
        print(f"{player_name.title()} realizes that they need to open the wooden door.")
        continue
    else:
        print("Outside forces are working against you. Make the right decision.")
        print(tomb_door)


print("You walk outside to be greeted by a lush forest brimming with life. You hear the birds chirping and the "
      "radiant sunlight is warm. You look just ahead a find a pathway.")

# outside tomb decision making.
# something is not working here.
outside_tomb = True
while outside_tomb:
    print(options_chapter_1['options_0'])
    out_tomb = input(f"Now that you're outside of that tomb; what do you do?\n(A/B/C/D) ")
    if out_tomb.lower() == "a" or out_tomb.upper() == "A":
            print(f"You walk down the pathway without a care in the world as you just woke up from a tomb. "
                  f"\n You're chilling but your lack of care has alerted a wild boar on the overgrown path.")
            after_choiceA = input(f"\nDo you chose to fight? (yes/no) ")
            if after_choiceA == "yes":
                print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                      f" runs away.")
                print("--The Boar Fled--")
                break
            elif after_choiceA == "no":
                print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                      f" evade the boar, but the rustling of the bushes spooked the boar.")
                print("--The Boar Fled--")
                break
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    elif out_tomb.lower() == "b" or out_tomb.upper() == "B":
            print(f"You're super chilling. You look at the trees and sky outside and get distracted by a bird. "
                  f"\n Life is great.")
            after_choiceB = input("Do you want to look around or take the path? (A/C)")
            if after_choiceB.lower == "a" or after_choiceB.upper() == "A":
                print(f"You look around the tomb for a good while. You managed to find and pickup a rusty shortsword"
                      f"\n hidden away in the overgrown grass.")
                player_inventory.append('shortsword')
                print(f"Your Inventory: {player_inventory}")
            elif after_choiceB.lower == "c" or after_choiceB.upper() == "C":
                print(
                    f"You take the pathway carefully and you managed to spot a wild boar in the middle of the road grazing."
                    f"\n It seems to be relatively strong.")
                bboar_fight = input(f"Do you want to fight the boar? (yes/no) ")
                if bboar_fight == 'yes':
                    print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                          f" runs away.")
                    print("--The Boar Fled--")
                    break
                elif bboar_fight == 'no':
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    elif out_tomb.lower() == "c" or out_tomb.upper() == "C":
            print(f"You look around the tomb for a good while. You managed to find and pickup a rusty shortsword"
                  f"\n hidden away in the overgrown grass.")
            player_inventory.append('shortsword')
            print(f"Your Inventory: {player_inventory}")
            after_choiceC = input(f"There is nothing to do here now. Will you leave the tomb area? (yes/no) ")
            if after_choiceC == "yes":
                print(f"You take the pathway carefully and you managed to spot a wild boar in the middle of "
                      f"the road grazing.\n It seems to be relatively strong.")
                cfight_boar = input(f"Do you want to fight the boar? (yes/no) ")
                if cfight_boar == "yes":
                    print("You wield your rusty shortsword and lunge straight at the boar catching it off guard. "
                          "\nYour shortsword manages to pierce to skull of the boar.")
                    print(f"--Player {player_name.title()} has recieved 35 exp. (experience points)--")
                    print(f"--Player {player_name.title()} has gained 2x boar hide.--")
                    player_inventory.append("2x boar hide")
                    player_status['level'] = 1
                    player_status['experience'] = 35
                    print(player_status)
                    print(player_inventory)
                    break
                elif cfight_boar == "no":
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
            elif after_choiceC == "no":
                print("You decide to hang around a little more. There is nothing to do so you decide to go down the"
                      " overgrown path.")
                print(f"You take the pathway carefully and you managed to spot a wild boar in the middle of "
                      f"the road grazing.\n It seems to be relatively strong.")
                cfight_boar = input(f"Do you want to fight the boar? (yes/no) ")
                if cfight_boar == "yes":
                    print("You wield your rusty shortsword and lunge straight at the boar catching it off guard. "
                          "\nYour shortsword manages to pierce to skull of the boar.")
                    print(f"--Player {player_name.title()} has recieved 35 exp. (experience points)--")
                    print(f"--Player {player_name.title()} has gained 2x boar hide.--")
                    player_inventory.append("2x boar hide")
                    player_status['level'] = 1
                    player_status['experience'] = 35
                    print(player_status)
                    print(player_inventory)
                    break
                elif cfight_boar == "no":
                    print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                          f" evade the boar, but the rustling of the bushes spooked the boar.")
                    print("--The Boar Fled--")
                    break
                else:
                    print("Outside forces are working against you. Make the right decision.")
                    continue
    elif out_tomb.lower() == "d" or out_tomb.upper() == "D":
            print(f"You take the pathway carefully and you managed to spot a wild boar in the middle of the road grazing."
                  f"\n It seems to be relatively strong.")
            after_choiceD = input(f"Do you want to fight the boar? (yes/no) ")
            if after_choiceD == "yes":
                print(f"You lunge at the boar at a sprinting speed. The boar gets scared at your sudden aggression and"
                      f" runs away.")
                print("--The Boar Fled--")
                break
            elif after_choiceD == "no":
                print(f"You decided to sneak around the boar. Your sneak skill isn't high enough to completely"
                      f" evade the boar, but the rustling of the bushes spooked the boar.")
                print("--The Boar Fled--")
                break
            else:
                print("Outside forces are working against you. Make the right decision.")
                continue
    else:
            print("Outside forces are working against you. Make the right decision.")
            continue

print("You continue down the overgrown path that is hidden away by dense brush. "
      "\nYou tear through the dense brush to be introduced to a well maintained road paved in brick.")
print("You are given the choice to get left or right.")
tomb_street = input('Left or Right? (L/R) ')

