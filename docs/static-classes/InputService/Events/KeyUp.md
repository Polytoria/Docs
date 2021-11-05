# Touched
### Description
Gets triggered when a key was released.

Event of [InputService](/static-classes/InputService/)

#### Returns
`string`

### Example
```lua
InputService.KeyUp:Connect(function (key)
    print(key .. " was released!")

    if key == "P" then
        print("The 'P' key was released!")
    end
end)
```