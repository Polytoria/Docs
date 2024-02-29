---
title: UIButton
description: UIButton is a class used for having interactable buttons in your place's UI.
icon: polytoria/UIButton
weight: 100
---

# UIButton

:polytoria-UIButton: UIButton is a class used for having interactable buttons in your place's UI.

{{ inherits("UILabel") }}

## Events

### Clicked { event }

Fires when the UIButton is clicked

**Example**

```lua
script.Parent.Clicked:Connect(function ()
    print("The button was clicked!")
end)
```
