## Updating
Make sure to update these templates when Darvas or Sylceran up-level
## Darvas
### Shortbow
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Shortbow}} {{Attack (roll+Dex+Pro)=[[1d20+4+2]]}} {{damage (roll+Dex)=[[1d6+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Magic Shortsword
- Attack roll: adding 4 for dexterity and 2 for proficiency and 1 for magic
- Damage roll: adding 4 for dexterity and 1 for magic
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Magic Shortsword}} {{Attack (roll+Dex+Pro+Magic)=[[1d20+4+2+1]]}} {{damage (roll+Dex+Magic)=[[1d6+4+1]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Rapier
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Rapier}} {{Attack (roll+Dex+Pro)=[[1d20+4+2]]}} {{damage (roll+Dex)=[[1d8+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Dagger (stab)
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Dagger (stab)}} {{Attack (roll+Dex+Pro)=[[1d20+4+2]]}} {{damage=[[1d4+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Dagger (thrown)
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: subtracting 1 for strength
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Dagger (thrown)}} {{Attack (roll+Str+Pro)=[[1d20-1+2]]}} {{damage=[[1d4-1]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```

## Sylceran

### Staff with Shillelagh
- Attack roll: adding 3 for wisdom and 2 for proficiency
- Damage roll: adding 3 for wisdom
```
&{template:default} {{name=Staff with Shillelagh Attack}} {{Attack (roll+Wis+Pro)=[[1d20+3+2]]}} {{damage (1 or 2 handed!)=[[1d8+3]]}}
```

### Cure Wounds
```
&{template:default} {{name=Cure Wounds}} {{healing=[[1d8+3]]}}
```

### Thunderwave
```
&{template:default} {{name=Thunderwave Attack}} {{damage=[[2d8]]}}  {{or w/ con save 1/2}}
```

### Staff without Shillelagh
- Attack roll: adding 1 for strength and 2 for proficiency
- Damage roll: adding 1 for strength
```
&{template:default} {{name=Staff w/o Shillelagh Attack}} {{Attack=[[1d20+1+2]]}} {{damage (2 handed)=[[1d8+1]]}} {{damage (1 handed)=[[1d6+1]]}}
```
