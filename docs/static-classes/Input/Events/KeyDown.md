# KeyDown
### Description
Gets triggered when a key was pressed.

Event of [Input](/static-classes/Input/)

#### Returns
`string`

### Example
```lua
Input.KeyDown:Connect(function (key)
    print(key .. " was pressed!")

    if key == "P" then
        print("The 'P' key was pressed!")
    end
end)
```
