# Delete

### Description

Sends a DELETE request to the specified url.

Function of [Http](../../)

#### Parameters

url `string`

params `params`

callback `function, default = nil`

#### Returns

`void`

### Example

```lua
Http:Delete("https://example.com/api/delete", "id=1" , function (data, error, errmsg)
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
