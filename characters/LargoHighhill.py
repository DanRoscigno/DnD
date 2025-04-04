"""This file describes the heroic adventurer Largo Highhill.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.10.2"

name = "Largo Highhill"
player_name = "Dan R"

# Be sure to list Primary class first
classes = ['Sorceror']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [2]  # ex: [10] or [3, 2]
subclasses = ["Draconic Bloodline"]  # ex: ['Necromacy'] or ['Thief', None]
background = "Guild Artisan"
race = "Lightfoot Halfling"
alignment = "Neutral good"

xp = 0
# HP is 1D6 + Con + 1 for Draconic Resilience
hp_max = 6 + 2 + 1 + 2 + 2 + 1
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 13
dexterity = 12 + 2 # +2 for Halfling
constitution = 15
intelligence = 11
wisdom = 11
charisma = 15 + 1 # +1 for Lightfoot Halfling

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('deception', 'intimidation', 'insight', 'persuasion')

# Any skills you have "expertise" (Bard/Rogue) in
skill_expertise = ()

# Named features / feats that aren't part of your classes, race, or background.
# Also include Eldritch Invocations and features you make multiple selection of
# (like Maneuvers for Fighter, Metamagic for Sorcerors, Trick Shots for
# Gunslinger, etc.)
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
languages = """Draconic, Elvish, Common, Halfling"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

# TODO: Put your equipped weapons and armor here
weapons = ["Dagger", "Light crossbow", "Quarterstaff"]  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "None"  # Eg "leather armor"
shield = "None"  # Eg "shield"

equipment = """- small bottle w/ dead sprite

- bag of holding

- component pouch

"""

attacks_and_spellcasting = """HP is 1D6 + Con + 1 for Draconic Resilience"""

ideals = """Davian: Best friend.  Has healing ability"""

# List of known spells
spells_prepared = ('mage hand', 'detect magic', 'chill touch', 'fire bolt', 'absorb elements', 'magic missile', 'frostbite')  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ()

# all spells known
spells = spells_prepared + __spells_unprepared

# Backstory
# Describe your backstory here
personality_traits = """Rosc: Barkeep at Sassy Christy.  Half Orc.  Does not like Elves."""

features_and_traits = """Vattar Kasari: Old friend / adventurer.  Campaigned with Cyris and myself.  I thought that Vattar had killed Malazar, but he just told me that Malazar is alive, missing an arm, and working with a necromancer from Thay and the Zhentarim (a black network of thieves, wizards, and spies)"""

bonds = """At 4th, 8th, 12th, 16th, & 19th level, increase one ability score of your choice by 2, or two ability scores by 1."""

flaws = """TODO: Describe your character's interesting flaws."""

