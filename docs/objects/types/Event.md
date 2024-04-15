---
title: Event
description: Event is the data type that represents listenable events.
icon: polytoria/Event
---

# Event

Event is a data type that represents listenable events.

You aren't able to create your own listenable events using this data type.

Events are present on many different objects and are marked with :polytoria-Event: on the Documentation.

## Methods

### Connect(function) { method }

Connect the specified function to the event. When the event is fired, the function will be ran. The event parameters may be passed to the function, if there are any.

**Example**

The function may be specified in 2 different ways:

```lua
function hitListener(hit)
    print(hit.Name .. "touched the Part!")
end

game["Environment"]["Part"].Touched:Connect(hitListener)
```

and

```lua
game["Environment"]["Part"].Touched:Connect(function(hit)
    print(hit.Name .. "touched the Part!")
end)
```

**Note: Defining a function within the Connect method will cause the function to be non-removable from the event.**

### Disconnect(function) { method }

Disconnect the specified function from the event.

**Example**

```lua
function hitListener(hit)
    print(hit.Name .. "touched the Part!")
end

game["Environment"]["Part"].Touched:Connect(hitListener)
wait(5)
-- hitListener(hit) will no longer run when the event is fired after the following line
game["Environment"]["Part"].Touched:Disconnect(hitListener)
```