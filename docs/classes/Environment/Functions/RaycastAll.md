# RaycastAll
### Description
Casts a ray from origin with a specified direction and returns a RayResult array for all hit objects.

Function of [Environment](/classes/Environment/)

#### Parameters
Origin `Vector3`
Direction `Vector3`
MaxDistance `number, default = Infinity`

#### Return type
`RayResult[]`

### Example
```lua
local hits = game["Environment"]:RaycastAll(Vector3.New(0, 10, 0), Vector3.New(0, -1, 0), 100)

for i, hit in pairs(hits) do
    print("Hit at " .. hit.Position .. "!")
end
```
