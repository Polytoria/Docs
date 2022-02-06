# AmbientColor
### Description
Specifies the ambient light color of the world.

Property of [Lighting](/classes/Lighting/)

#### Type
`Color`

### Example
```lua
game["Lighting"].AmbientColor = Color.Random()
```

### Notes
- Only effective when [AmbientSource](/classes/Lighting/Properties/AmbientSource) is set to `AmbientColor`
