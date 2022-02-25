# Delete
### Description
Send a HTTP DELETE request to specific URL

Function of [Http](../../)

#### Parameters
url `String`
params `params`
callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
-- Delete your Discord Webhook message
Http:Delete("https://discord.com/api/webhooks/.../messages/...", "" , function (data, error, errmsg)
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
- Params are in query form, Example: key1=value&key2=value