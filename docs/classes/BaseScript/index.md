# BaseScript

> This class cannot be created using the `Instance.New` function.

BaseScripts are the base classes of all scripts (Scripts, LocalScripts). They can be parented to any instance.

You can get the currently executing script in a script using the `script` keyword.

```lua
print(script.Parent.Name)
```

You can also get or set globals from other scripts if they're not local.

```lua
print(script1.variable)
script2.variable2 = true
```

Inherited from [Instance](../Instance)
