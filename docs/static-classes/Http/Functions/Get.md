# Get

### Description

Sends a GET request to the specified url.

Function of [Http](../../)

#### Parameters

url `string`

callback `function, default = nil`

header `Table`

#### Returns

`void`

### Example

```lua
Http:Get("https://api.polytoria.com/v1/store/25272", function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end,{})
```
