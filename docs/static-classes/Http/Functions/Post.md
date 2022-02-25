# Post
### Description
Send a HTTP POST request to specific URL

Function of [Http](../../)

#### Parameters
url `String`
params `params`
callback `DynValue, default = nil`

#### Return type
`Void`

### Example
```lua
-- Post Discord Webhook
Http:Post("https://discord.com/api/webhooks/...", "content=Hello from Polytoria!" , function (data, error, errmsg)
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