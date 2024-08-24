---
title: Insert
description: Insert is a class used for inserting user-generated models into your game via scripts.
icon: polytoria/Unknown
---

:polytoria-Unknown: Insert is a class used for inserting user-generated models into your game via scripts.

## Methods

### Model(modelID;int, callback;func=nil) { method }

Inserts the specified model ID into your game, with an optional callback for when the model successfully loads.

**Example:**
```lua
-- Loads the tree model associated with that ID
Insert:Model(739)
```