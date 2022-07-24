# Rendered

### Description

Rendered is an event that gets called after a frame is rendered.

Event of [Game](/classes/Game/)

#### Returns

DeltaTime `number`

### Example

```lua
game.Rendered:Connect(function(deltaTime)
    game["Environment"]["Part"].Position = game["Environment"]["Part"].Position + (Vector3.New(0, 1, 0) * deltaTime) -- Part will move upwards 1 stud per second.
end)
```

### Notes

- The server runs at a rate of 30 FPS or lower.
- DeltaTime is the amount of seconds passed between the current and last frame
