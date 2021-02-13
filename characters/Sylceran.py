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
background = "Smuggler"
race = "Wood Elf"
alignment = "Lawful good"

xp = 0
# hit points are a D8 plus Constitution bonus
hp_max = 8 + 2
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
skill_proficiencies = ('perception', 'arcana', 'athletics', 'deception', 'nature')

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
_proficiencies_text = ("Herbalism kit", "water vehicle tools",)  # ex: ("thieves' tools",)

# Proficiencies and languages
languages = """Common, Elvish, Undercommon"""

# Inventory
# TODO: Get yourself some money
cp = 0
sp = 35
ep = 0
gp = 15
pp = 0

# TODO: Put your equipped weapons and armor here
#weapons = ["Scimitar", "Javelin", "Mace"]  # Example: ('shortsword', 'longsword')
weapons = ["Quarterstaff", "shortsword", "dagger", "club"]  # Example: ('shortsword', 'longsword')
#magic_items = ('healing potion', 'scroll (detect magic??)')  # Example: ('ring of protection',)
armor = "Hide Armor"  # Eg "leather armor"
shield = "Shield"  # Eg "shield"

equipment = ( """- bedroll

- healing potion

- scroll (detect magic?)

- Herbalism kit

- 2 pair leather boots

- backpack + pouch

- mess kit + 10 rations

- tinderbox + 10 torches

- waterskin

- 50 feet of hempen rope

- common clothes

- beatiful bottle w/ bit of Elverquiist""")


attacks_and_spellcasting = """Shillelagh and whack with staff. If there are multiple enemies, then Entangle and whack, unless they will be able to attack back with ranged weapons.  If that is not enough, then Thunderwave.  Entangle causes a strenth save against my spell save DC, Thunderwave is a constitution save."""

# List of known spells
# Example: spells_prepared = ('magic missile', 'mage armor')

# You can prepare this number of spells:
# Wisdom modifier + Druid level.  For example, with a Wisdom mod of +3 at level 2
# prepare 5 spells
spells_prepared = ('shillelagh', 'shape water', 'cure wounds', 'entangle', 'thunderwave', 'detect magic', 'detect poison and disease')  # Todo: Learn some spells

# Which spells have not been prepared
__spells_unprepared = ('Animal Friendship', 'Charm Person', 'Create or Destroy Water', 'Faerie Fire', 'Fog Cloud', 'Goodberry', 'Healing Word', 'jump', 'Longstrider', 'Purify Food and Drink', 'Speak with Animals') 
# all spells known
spells = spells_prepared + __spells_unprepared

# Wild shapes for Druid
wild_shapes = ()  # Ex: ('ape', 'wolf', 'ankylosaurus')

# Infusions for Artificer
infusions = () # Ex: ('repeating shot', 'replicate magic item')

# Backstory
# Describe your backstory here
personality_traits = """I become wistful when I see the sun rise over the ocean."""

ideals = """I will not cheat another smuggler or directly harm innocents."""

bonds = """Much of the treasure I claim will be used to enrich my community."""

flaws = """I struggle to trust the words of others."""

features_and_traits = """While rowing S-Cargo along the coast of Saltmarsh, stopping off once in a while to sell bottles of Elverquisst, which the locals enjoyed for its warming effects, I was caught in a sudden storm and struck by lightning.  When I awoke, I could feel the residual energy of the lightning coursing through my body.  The only real damage to the rowboat was to one oar, which seemed to take the brunt of the strike, and is now my staff.  I am naturally respectful of Nature, and have since been studying Nature's power."""
