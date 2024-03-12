---
title: Http
description: Http is a static class used for HTTP communications and requests.
icon: polytoria/Http
---

# Http

{{ staticclass("Http")}}

:polytoria-Http: Http is a static class used for HTTP communications and requests.

{{ serverexclusive() }}

<div data-search-exclude markdown>
!!! warning "Each server has a rate limit of 15 requests per minute."

!!! note "The place ID is sent along with the request under the header named `PT-Game-ID`."

!!! note "When using the Http `:Post`, `:Put`, or `:Delete` methods, parameters are formatted in query form like this: `key1=value&key2=value`"

</div>

## Methods

### Get(url;string,callback;function,headers;array) { method }

Sends a GET request to the specified URL.

**Example**

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

### Post(url;string,parameters;string,callback;function) { method }

Sends a POST request to the specified URL.

**Example**

```lua
Http:Post("https://example.com/api/post", "id=1&name=Hello" , function (data, error, errmsg)
    if not error then
        script.Parent.Color = Color.New(1, 1, 1)
        script.Parent.Text = data
    else
        script.Parent.Color = Color.New(1, 0, 0)
        script.Parent.Text = errmsg
    end
end)
```

### Put(url;string,parameters;string,callback;function) { method }

Sends a PUT request to the specified URL.

**Example**

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

### Delete(url;string,parameters;string,callback;function) { method }

Sends a DELETE request to the specified url.

**Example**

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
