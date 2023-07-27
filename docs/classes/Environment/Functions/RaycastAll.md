# RaycastAll

### Description

Casts a ray from origin with a specified direction and returns a RayResult array for all hit objects.

Function of [Environment](/classes/Environment/)

#### Parameters

origin `Vector3`

direction `Vector3`

maxDistance `number, default = inf`

ignoreList `Instance[]`

#### Returns

`RayResult[]`

### Example

```lua
local hits = game["Environment"]:RaycastAll(Vector3.New(0, 10, 0), Vector3.New(0, -1, 0), 100)

for i, hit in pairs(hits) do
    print("Hit at " .. hit.Position .. "!")
end
```
