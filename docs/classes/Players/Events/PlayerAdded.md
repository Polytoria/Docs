# PlayerAdded

### Description

Gets triggered when a player joins the game.

Event of [Players](/classes/Players/)

#### Returns

Player `Player`

### Example

```lua
game["Players"].PlayerAdded:Connect(function (player)
    print(player.Name .. " joined the game!")
end)
```
