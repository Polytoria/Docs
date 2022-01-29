# CreateExplosion
### Description
Creates a deadly explosion killing players and applying force to parts at the given position.

Function of [Environment](/classes/Environment/)

#### Parameters
Position `Vector3`
Radius `number, default = 10`
Force `number, default = 5000`
AffectAnchored `Boolean, default = True`
Callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
game["Environment"]:CreateExplosion(Vector3.New(0, 0, 0), 30, 5000, false)
```

### Notes
- When true, AffectAnchored will unanchor parts within the explosion radius.
- Callback gets called for each part within explosion radius.
