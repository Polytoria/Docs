---
title: Globals
description: Built-in globals.
weight: 1
---

Globals are automatically available in every script and do not need to be referenced from another object.

## Methods

This section documents built-in non-standard functions.

---

### spawn(callback;function) { method }

Executes a function asynchronously in a new thread.

**Example**

```lua
spawn(function()
    print("Hello, world!")
end)
```

### tick(void):number { method }

Returns how much time has passed in seconds since the Unix epoch.

### wait(seconds;number):number { method }

Yields the current thread for a duration.
Returns the time waited.

**Example**

```lua
print("foo")
wait(1)
print("bar")
```

<div data-search-exclude markdown>
!!! note "Calling wait(0) still yields execution."
</div>

## Properties

This section documents built-in non-standard properties.

---

### game:Game { property }

Privdes access to the root game instance.

### script:BaseScript { property }

A reference to the current script instance.

### \_VERSION:string { property }

The current MoonSharp version.

### \_MOONSHARP:table { property }

A table of MoonSarp information.
