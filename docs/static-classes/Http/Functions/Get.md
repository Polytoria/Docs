# Get
### Description
Sends a GET request to the specified url.

Function of [Http](../../)

#### Parameters
url `String`
callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
Http:Get("https://api.polytoria.com/v1/asset/owner?userID=1&assetID=234", function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end,{})
```
