---
title: Chat
description: Chat is a static class used for various actions regarding the chat.
icon: polytoria/Chat
---

# Chat

{{ staticclass("Chat")}}

:polytoria-Chat: Chat is a static class used for various actions regarding the chat.

## Methods

### BroadcastMessage(message;string) { method }

Sends a chat message to all users.

**Example**

```lua
Chat:BroadcastMessage("Hello, world!")
```

### UnicastMessage(message;string,player;Player) { method }

Sends a chat message to a specific user.

**Example**

```lua
Chat:UnicastMessage("Hello, world!", game["Players"]["willemsteller"])
```
