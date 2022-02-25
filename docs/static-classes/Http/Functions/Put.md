# Put
### Description
Sends a PUT request to the specified URL

Function of [Http](../../)

#### Parameters
url `String`
params `params`
callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
Http:Put("https://example.com", "id=1&content=Hello" , function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

#### Note
- Params are in query form (key1=value&key2=value)