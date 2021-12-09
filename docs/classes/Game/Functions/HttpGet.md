# HttpGet
### Description
Sends a HTTP GET request to the specified URL.

Function of [Game](/classes/Game/)

#### Parameters
url `String`
callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
game:HttpGet("https://api.polytoria.com/v1/asset/owner?userID=1&assetID=234", function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

### Notes
- HttpGet can only be called from server.
- The request sends the current game ID as a header
- There is a limit of 15 requests per minute
