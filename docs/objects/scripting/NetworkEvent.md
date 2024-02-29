---
title: NetworkEvent
description: NetworkEvents are events that can be called to communicate between server and client.

icon: polytoria/NetworkEvent
weight: 5
---

# NetworkEvent

:polytoria-NetworkEvent: NetworkEvents are events that can be called to communicate between server and client. {{ classLink("NetMessage") }} are the class used for sharing data between server and client when sending NetworkEvents.

{{ inherits("Instance") }}

## Events

### InvokedClient(sender;nil,netmsg;NetMessage) { event }

Fires when the client receives a message from the server.

**Example**

```lua
netEvent.InvokedClient:Connect(function (sender, message)
    local value = message:GetString("key")
end)
```

{{ clientexclusive() }}

### InvokedServer(sender;Player,netmsg;NetMessage) { event }

Fires when the server receives a message from the client.

**Example**

```lua
netEvent.InvokedServer:Connect(function (sender, message)
    local value = message:GetString("key")
end)
```

{{ serverexclusive() }}

## Methods

### InvokeClient(message;NetMessage,player;Player) { method }

Sends a network event to a specific player from the server.

**Example**

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClient(message, game["Players"]["willemsteller"])
```

{{ serverexclusive() }}

### InvokeClients(message;NetMessage) { method }

Sends a network event to all players from the server.

**Example**

```lua
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeClients(message)
```

{{ serverexclusive() }}

### InvokeServer(message;NetMessage) { method }

Sends a network event to the server from the client.

**Example**

```lua
-- netEvent defined somewhere else in the code
local message = NetMessage.New()
message.AddString("key", "value")
netEvent.InvokeServer(message)
```
