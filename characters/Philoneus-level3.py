"""This file describes the heroic adventurer Philoneus.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets -F Philoneus-level3.py`` from the 
command line.
"""

dungeonsheets_version = "0.9.4"

name = "Philoneus"
player_name = "Mark M."

classes = ['Monk']
levels = [3]

# I just chose Human at random, pg 17 in Player's
# Handbook:
race = "Human"

# This is an example for Philoneus' background, change it to
# your choice.  See Player's Handbook pg 121:
background = "Charlatan"

# Based on your attacks at the end of our last session
# I set the subclass (Monastic Tradition) to Way of the Drunken Master:
subclasses = ["Way of the Drunken Master"] 

# I don't know what is "normal" for Monks, set it as you wish:
alignment = "Lawful good"

# I don't think we use xp any more, Mark will tell you if
# he uses xp or the new leveling system:
xp = 0

# Max hit points: At Level 1 you get 8 plus Constitution modifier  
# (because this is dependent on your Constitution modifier
# you will have to roll/calculate your ability scores first).
# At further levels you use 1d8 + Constitution modifier.
# Below are samples, change to yours: 
hp_max = 9 + 5 + 4

inspiration = 0  # integer inspiration value

# Ability Scores.  The Adventure League DM had me use this calculator:
# https://chicken-dinner.com/5e/5e-point-buy.html 
# It starts out with 8's for all of your abilities, and then you can
# allocate a total of 24 more points as you like.  Talk to Mark about
# what he suggests.  Note: The calculator linked above will automatically
# add points based on your chosen race and sub-race.
strength = 8
dexterity = 16
constitution = 13
intelligence = 14
wisdom = 14
charisma = 10

# Select what skills you're proficient with. Choose two from
# this list as a Monk:
#     acrobatics, athletics, history, insight, religion, stealth

# Your background will also give you profiency, also add those.
#
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'deception', 'sleight of hand')
skill_proficiencies = ('athletics', 'stealth', 'deception', 'sleight of hand')

# Any skills you have "expertise" in
skill_expertise = ()

# Named features / feats that aren't part of your classes, 
# race, or background.
# Also include Eldritch Invocations and features you make 
# multiple selection of (like Maneuvers for Fighter, Metamagic 
# for Sorcerors, Trick Shots for Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()  # ex: ('shortsword', 'quarterstaff')
_proficiencies_text = ()  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Gnomish"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 0
pp = 0

# TODO: Put your equipped weapons and armor here

# You start with the following equipment, in addition to 
# the equipment granted by your background:
#  • (a) a shortsword or (b) any simple weapon
#  • (a) a dungeoneer's pack or (b) an explorer's pack - 10 darts
weapons = ('shortsword')  # Example: ('shortsword')
magic_items = ()  # Example: ('ring of protection',)
armor = ""  # Leave blank, right?
shield = ""  # Leave blank, right?

equipment = """TODO: list the equipment and magic items your character carries"""

attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ()  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Backstory
# Describe your backstory here, see Player's Handbook pg 121:
personality_traits = """TODO: How does your character behave? See the PHB for
examples of all the sections below"""

ideals = """TODO: What does your character believe in?"""

bonds = """TODO: Describe what debts your character has to pay,
and other commitments or ongoing quests they have."""

flaws = """TODO: Describe your characters interesting flaws.
"""

features_and_traits = """TODO: Describe other features and abilities your
character has."""
