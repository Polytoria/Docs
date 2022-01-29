# Shared
### Description
An empty table you can use to hold metadata about anything on any object or player you want. Does not sync client <-> server.

Property of [Instance](/classes/Instance/)

#### Type
`Table`

### Example
```lua
-- Script 1
local players = game.Players.GetChildren()
local lucky = players[math.random(1, #players)]

lucky.Shared.IsZombie = true

-- Script 2
local killBrick = game.Environment["Kill Brick"]

killBrick.Touched:Connect(function(hit)
    if hit.IsA("Player") then
        if hit.Shared.IsZombie then
            print("YOU CAN'T KILL ME, I'M ALREADY DEAD!")
        else
            hit.Health = 0
        end
    end
end
```
