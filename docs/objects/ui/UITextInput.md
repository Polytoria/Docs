---
title: UITextInput
description: UITextInput is a class that allows the user to enter text.
icon: polytoria/UITextInput
weight: 100
---

# UITextInput

:polytoria-UITextInput: UITextInput is a class that allows the user to enter text.

{{ inherits("UIView") }}

## Events

### Changed { event }

An event that is fired when the value of the text input changes.

**Example**

```lua
element.Changed:Connect(function()
    print(element.Text)
end)
```

### Submitted { event }

The event that is triggered when the user submits the text in a text input.

**Example**

```lua
element.Submitted:Connect(function()
    print(element.Text)
end)
```

## Properties

### AutoSize:bool { property }

Whether the text should be automatically sized to fit the label's size.

**Example**

```lua
element.AutoSize = true
```

### Font:TextFontPreset { property }

The font of the label.

**Example**

```lua
element.Font = TextFontPreset.Montserrat
```

### FontSize:float { property }

The font size of the label.

**Example**

```lua
element.FontSize = 20
```

### IsMultiline:bool { property }

Set if the text input can be multiline.

**Example**

```lua
element.IsMultiline = true
```

### IsReadOnly:bool { property }

Set if the text input can be edited or not.

**Example**

```lua
element.IsReadOnly = true
```

### JustifyText:TextJustify { property }

Determines how the text is justified.

**Example**

```lua
element.JustifyText = TextJustify.Center
```

### MaxFontSize:float { property }

The maximum font size of the UI element if AutoSize is set to true.

**Example**

```lua
element.MaxFontSize = 16
```

### Placeholder:string { property }

The placeholder of the text input.

**Example**

```lua
element.Placeholder = "Type here..."
```

### PlaceholderColor:Color { property }

The color of the placeholder text.

**Example**

```lua
element.PlaceholderColor = Color.New(0, 0, 0, 0.5)
```

### Text:string { property }

The text of the label.

**Example**

```lua
element.Text = "Hello, World!"
```

### TextColor:Color { property }

The color of the text.

**Example**

```lua
element.TextColor = Color.New(0, 0, 0, 1)
```

### VerticalAlign:TextVerticalAlign { property }

The vertical alignment of the text.

**Example**

```lua
element.VerticalAlign = TextVerticalAlign.Middle
```
