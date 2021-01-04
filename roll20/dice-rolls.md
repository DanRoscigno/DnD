## Updating
Make sure to update these templates when Darvas or Sylceran up-level
## Darvas
### Shortbow
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Shortbow}} {{Attack (+Dex + Proficiency)=[[1d20+4+2]]}} {{damage (+ Dex)=[[1d6+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Shortsword
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Shortbow}} {{Attack=[[1d20+4+2]]}} {{damage=[[1d6+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Dagger (stab)
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: adding 4 for dexterity
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Dagger (stab)}} {{Attack=[[1d20+4+2]]}} {{damage=[[1d6+4]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```
### Dagger (thrown)
- Attack roll: adding 4 for dexterity and 2 for proficiency
- Damage roll: subtracting 1 for strength
- Sneak attack: 2d6 at 4th level
```
&{template:default} {{name=Dagger (thrown)}} {{Attack=[[1d20-1+2]]}} {{damage=[[1d6-1]]}} {{Sneak attack (if applicable)=[[2d6]]}}
```

## Sylceran

### Staff with Shillelagh
- Attack roll: adding 3 for wisdom and 2 for proficiency
- Damage roll: adding 3 for wisdom
```
/me &{template:default} {{name=Staff with Shillelagh Attack}} {{Attack=[[1d20+3]]}} {{damage=[[1d8+3+3]]}}
```
