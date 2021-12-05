# Clicked
### Description
Gets triggered when this instance was clicked by a player.

Event of [Instance](/classes/Instance/)

#### Returns
`Player`

### Example
```lua
game["Environment"]["Part"].Clicked:Connect(function (player)
    print(player.Name .. " clicked on this part!")
end)
```

### Notes
- There must be an active collider on the instance for this event to trigger ([Part](/classes/Part), [Player](/classes/Player), etc.)