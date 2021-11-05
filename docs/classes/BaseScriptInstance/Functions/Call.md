# Call
### Description
Calls 

Function of [Environment](/classes/Environment/)

#### Parameters
Position `Vector3`  
Radius `number`  
Force `number`  
AffectAnchored `bool`

### Example
```lua
game["Environment"]:CreateExplosion(Vector3.New(0, 0, 0), 30, 5000, false)
```

### Notes
- When true, AffectAnchored will unanchor parts within the explosion radius.