# PlayerRemoved
### Description
Gets triggered when a player quits the game.

Event of [Players](/classes/Players/)

#### Returns
Player `Player`

### Example
```lua
game["Players"].PlayerRemoved:Connect(function (player)
    print(player.Name .. " left the game!")
end)
```