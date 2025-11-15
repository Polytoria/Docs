---
title: BaseScript
description: BaseScript is the base class of all script classes.

icon: polytoria/BaseScript
weight: 4
---

# BaseScript

{{ ambiguousMultiple([["ScriptInstance", "which runs your Lua scripts on the server."],["LocalScript", "which runs your Lua scripts on the client."],["ModuleScript", "which contains data accessible by any script."]]) }}

{{ abstract() }}

:polytoria-BaseScript: BaseScripts are the base class of all script types ({{ classLink("ScriptInstance") }}, {{ classLink("LocalScript") }}, {{ classLink("ModuleScript") }}). They can be parented to any instance.

{{ inherits("Instance") }}

## Methods

### Call(functionParameters) { method }

Calls a function on another script

**Example**

```lua
game["ScriptService"]["Script"]:Call("Foo", "Bar")
```

<div data-search-exclude markdown>
!!! warning "Scripts are naturally single-threaded, but can run multiple threads at once through Signals and :Call."
</div>

<div data-search-exclude markdown>
!!! failure "Local Functions cannot be ran using the Call function."
</div>