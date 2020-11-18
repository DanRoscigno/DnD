"""This file describes the heroic adventurer druidelf.

It's used primarily for saving characters from create-character,
where there will be many missing sections.

Modify this file as you level up and then re-generate the character
sheet by running ``makesheets`` from the command line.

"""

dungeonsheets_version = "0.10.2"

name = "Sylceran"
player_name = "Dan R"

# Be sure to list Primary class first
classes = ['Druid']  # ex: ['Wizard'] or ['Rogue', 'Fighter']
levels = [1]  # ex: [10] or [3, 2]
subclasses = ['']  # ex: ['Necromacy'] or ['Thief', None]
background = "GuildArtisan"
race = "Wood Elf"
alignment = "Lawful good"

xp = 0
hp_max = 8
inspiration = False  # boolean inspiration value

# Ability Scores
strength = 12
dexterity = 13 + 2
constitution = 14
intelligence = 10
wisdom = 15 + 1
charisma = 8

# Select what skills you're proficient with
# ex: skill_proficiencies = ('athletics', 'acrobatics', 'arcana')
skill_proficiencies = ('perception', 'arcana', 'insight', 'persuasion', 'nature')

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
_proficiencies_text = ("Distiller's tools",)  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Undercommon"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 0
ep = 0
gp = 15
pp = 0

# TODO: Put your equipped weapons and armor here
#weapons = ["Scimitar", "Javelin", "Mace"]  # Example: ('shortsword', 'longsword')
weapons = ["Scimitar"]  # Example: ('shortsword', 'longsword')
magic_items = ()  # Example: ('ring of protection',)
armor = "Hide Armor"  # Eg "leather armor"
shield = "Shield"  # Eg "shield"

equipment = ( """--bedroll

--distiller's’ tools

--backpack

--mess kit

--tinderbox

--10 torches

--10 days of rations

--waterskin

--50 feet of hempen rope

--letter of introduction from distillers' guild

--traveler's clothes

--pouch.""")


attacks_and_spellcasting = """TODO: Describe how your character usually attacks
or uses spells."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')
spells_prepared = ('druidcraft', 'thorn whip')  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ('entangle', 'faerie fire', 'healing word')

# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = () # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """TODO: Describe how your character behaves, interacts with others"""

ideals = """TODO: Describe what values your character believes in."""

bonds = """TODO: Describe your character's commitments or ongoing quests."""

flaws = """TODO: Describe your character's interesting flaws."""

features_and_traits = """TODO: Describe other features and abilities your
character has."""
