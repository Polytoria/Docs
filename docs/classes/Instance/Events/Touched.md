# Touched
### Description
Gets triggered when this instance was touched by another instance.

Event of [Instance](/classes/Instance/)

#### Returns
`Instance`

### Example
```lua
game["Environment"]["Part"].Touched:Connect(function (other)
    print(other.Name .. " touched this part!")
end)
```

### Notes
- There must be an active collider on the instance for this event to trigger ([Part](/classes/Part), [Player](/classes/Player), etc.)
