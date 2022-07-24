# TouchEnded

### Description

Gets triggered when this instance is stopped being touched by another instance.

Event of [Instance](/classes/Instance/)

#### Returns

`Instance`

### Example

```lua
game["Environment"]["Part"].TouchEnded:Connect(function (other)
    print(other.Name .. " stopped touching this part!")
end)
```

### Notes

- There must be an active collider on the instance for this event to trigger ([Part](/classes/Part), [Player](/classes/Player), etc.)
