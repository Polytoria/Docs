# KeyDown
### Description
Gets triggered when a key was pressed.

Event of [InputService](/static-classes/InputService/)

#### Returns
`string`

### Example
```lua
InputService.KeyDown:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```