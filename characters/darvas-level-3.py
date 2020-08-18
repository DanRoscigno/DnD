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
levels = [3]  # ex: [10] or [3, 2]
subclasses = ["Thief"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Criminal"
race = "Stout Halfling"
alignment = "Neutral"

xp = 0
hp_max = 11 + 5 + 4
inspiration = 0  # integer inspiration value

# Ability Scores
strength = 8
dexterity = 16
constitution = 16
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
weapon_proficiencies = ('dagger', 'shortbow', 'rapier')
_proficiencies_text = ("thieves' tools", "Dice set")

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
gp = (4 + 3 + 3 + 1) * 10 + 15 + (4 * 50) - 10
pp = 0

weapons = ('rapier', 'dagger', 'shortbow')
magic_items = ()  # Example: ('ring of protection',)
armor = "leather armor"
shield = "shield"

# See equipment packs on page 151 of PHB
# Page 129 of PHB: Criminal starting equip: 
# A crowbar, a set of dark common clothes
# including a hood, and a belt pouch containing 15 gp
equipment = """A crowbar, a set of dark common clothes
including a hood, and a belt pouch containing my coins"""

attacks_and_spellcasting = """ATK Bonus=prof bonus + Dex
                              Damage=roll + Dex on
                              finesse & range weapon.
                              Thrown dagger uses strength
                              instead of dex.
                              Armor Class is -2 without shield.

                              Dagger range 20/60

                              Shortbow range 80/320
"""

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
personality_traits = """The first thing I do in a new place is
note the locations of everything valuable—or where such things
could be hidden."""

ideals = """I'm loyal to my friends, not to any ideals, and
everyone else can take a trip down the Styx for all I
care. (Neutral)"""

bonds = """I'm trying to pay off an old debt I owe to a generous
benefactor."""

flaws = """I have a "tell" that reveals when I'm lying.
"""

features_and_traits = """TODO: Describe other features
                         and abilities your
                         character has."""
