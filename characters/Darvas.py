"""This file describes the heroic adventurer Darvas.

Modify this file as you level up and then re-generate 
the character sheet by running ``makesheets -F filename.py`` 
from the command line.

"""

dungeonsheets_version = "0.9.4"

name = "Darvas"
player_name = "Dan R"

# Be sure to list Primary class first
classes = ['Rogue']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [5]  # ex: [10] or [3, 2]
subclasses = ["Thief"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Criminal"
race = "Stout Halfling"
alignment = "Neutral"

xp = 0
# hit points are 1d8 + Constitution modifier at each level
hp_max = (8 + 3) + (5 + 3) + (4 + 3) + (4 + 3) + (5 + 3)
inspiration = 0  # integer inspiration value

# Ability Scores.  The Adventure League DM had me use this calculator:
# https://chicken-dinner.com/5e/5e-point-buy.html 
# It starts out with 8's for all of your abilities, and then you can
# allocate a total of 24 more points as you like.  Talk to Mark about
# what he suggests.  Note: The calculator linked above will automatically
# add points based on your chosen race and sub-race.

strength = 8
# Dex is +2 as a Halfling and another +2 as Level 4 Rogue
dexterity = 14 + 2 + 2
# Con is +1 as a Stout Halfling
constitution = 15 + 1
intelligence = 14
wisdom = 12
charisma = 8

# Select what skills you're proficient with
skill_proficiencies = ('acrobatics', 'investigation', 'perception', 'deception', 'sleight of hand', 'stealth')

skill_expertise = ('sleight of hand', 'stealth')

# Named features / feats that aren't part of your classes, 
# race, or background.
# Also include Eldritch Invocations and features you make 
# multiple selection of (like Maneuvers for Fighter, 
# Metamagic for Sorcerors, Trick Shots for Gunslinger, etc.)
# Example:
# features = ('Tavern Brawler',) # take the optional Feat from PHB
features = ()

# If selecting among multiple feature options: ex Fighting Style
# Example (Fighting Style):
# feature_choices = ('Archery',)
feature_choices = ()

# Weapons/other proficiencies not given by class/race/background
weapon_proficiencies = ()
_proficiencies_text = ("Dice set",)

# Proficiencies and languages
languages = """Common, Halfling"""

# Inventory
cp = 0
sp = 0
ep = 0
# rolled 4+3+3+1 for starting gold
# 15 for being a criminal
# 4 treasure points from Adventurer's League (1 point = 50gp) 
# - 10 to buy shield
# + 16 gold from Harbin Wester
# - 2 gold for two quivers of arrows
# - 40 to upgrade leather armor to studded leather (trade in leather)
# - 10 gold for rations
# - 100 gold to buy two healing potions
gp = (4 + 3 + 3 + 1) * 10 + 15 + (4 * 50) - 10 + 16 - 2 - 40  - 10 - 100
pp = 0

# See equipment packs on page 151 of PHB
# Page 129 of PHB: (Criminal) starting equip: 
# A crowbar, a set of dark common clothes
# including a hood, and a belt pouch containing 15 gp
#
# Also pg 96 (Rogue)
# You start with the following equipment, in addition
# to the equipment granted by your background:
# • (a) a rapier or (b) a shortsword
# • (a) a shortbow and quiver of 20 arrows or (b) a
# shortsword
# • (a) a burglar's pack, (b) a dungeoneer's pack, or (c) an
# explorer's pack
# • Leather armor, two daggers, and thieves' tools
# equipment = """A crowbar, a set of dark common clothes
# including a hood, and a belt pouch containing my coins"""
#
# Fom the above:
# Burglar's Pack: a backpack, a bag of 1,000 ball bearings, 
# 10 feet of string, a bell, 5 candles, a crowbar, a hammer, 
# 10 pitons, a hooded lantern, 2 flasks of oil, 5 days rations, 
# a tinderbox, and a waterskin. The pack also has 50 feet of 
# hempen rope strapped to the side of it.
#
# crowbar
# dark common clothes with hood
# 15 gp in belt pouch
# rapier
# shortbow and 40 arrows
# Leather armor
# two daggers
# thieves tools

weapons = ('rapier', 'shortsword', 'shortbow', 'dagger')
magic_items = ('cloak of druidane', 'BlueStingSword')  # Example: ('ring of protection',)
armor = "studded leather armor"
shield = "shield"
equipment = ( """

Shortbow and 40 arrows 

extra dagger

magic potion of unknown type

2 healing potions

thieves’ tools

backpack and pouch

800 ball bearings

10 feet of string
 
bell

5 candles + tinderbox

crowbar

hammer + 10 pitons

50 feet of hempen rope

hooded lantern + 2 flasks oil

5 days rations + waterskin

dark common clothes w/ hood""")

attacks_and_spellcasting = """--ATK Bonus=prof bonus + Dex

--Damage=roll + Dex on finesse & range weapon.

--Thrown dagger uses strength instead of dex.

--Armor Class is -2 without shield.

--Dagger range 20/60

--Shortbow range 80/320""" 

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
# Describe your backstory here
personality_traits = """Ranged: Attack (action)/move/Hide (bonus action)"""



ideals = """DODGE when attacked! (reaction)"""

bonds = """Dash, Hide, or Disengage as bonus action"""

flaws = """Stalk: Hide (bonus action)/move/Attack (action)"""

features_and_traits = """ STOUT RESILIENCE
Source: Race (Stout Halfling)
You have advantage on saving throws against
poison, and you have resistance against poison damage
(added here to avoid printing 3rd page!)"""

