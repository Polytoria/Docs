# KeyUp
### Description
Gets triggered when a key was released.

Event of [Input](/static-classes/Input/)

#### Returns
`string`

### Example
```lua
Input.KeyUp:Connect(function (key)
    print(key .. " was released!")

    if key == "P" then
        print("The 'P' key was released!")
    end
end)
```
