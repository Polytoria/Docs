# Raycast
### Description
Casts a ray from origin with a specified direction and returns a RayResult for the first hit object.

Function of [Environment](/classes/Environment/)

#### Parameters
Origin `Vector3`
Direction `Vector3`
MaxDistance `number, default = Infinity`

#### Return type
`RayResult`

### Example
```lua
local hit = game["Environment"]:Raycast(barrel.Position, barrel.Forward)

if hit and hit.Instance:IsA("Player") then
    hit.Instance.Health = 0
end
```
