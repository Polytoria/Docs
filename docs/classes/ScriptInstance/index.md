# ScriptInstance
ScriptInstances are Lua scripts that will be executed when the game starts. They can be parented to any instance.

You can get the currently executing script in a script using the `script` keyword.  

### Example
```lua
print(script.Parent.Name)
```

Inherited from [Instance](../Instance)