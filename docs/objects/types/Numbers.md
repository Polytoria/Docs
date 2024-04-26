---
title: Numbers
description: Numbers are a data type holding significant value to scripting.
icon: polytoria/NumberValue
---

# Numbers

Numbers are essential to scripting. This page will explain how numbers work and the difference between a float and an integer.

## Number operations

The basic number operations of addition, subtraction, multiplication, division, exponentation, root, modulo and logarithm are possible within Lua and thus within Polytoria.

### Addition

The addition operation may be done using `+`

```lua
local sum = summand1 + summand2
```

### Subtraction

The subtraction operation may be done using `-`

```lua
local difference = minuend - subtrahend
```

### Multiplication

The multiplication operation may be done using `*`

```lua
local product = factor1 * factor2
```

### Division

The division operation may be done using `/`

```lua
local quotient = dividend / divisor
```

### Exponentation

The exponentation operation may be done using `^` or `math.pow()`

```lua
local power = base^exponent
local power2 = math.pow(base^exponent)
```

### Root

The root operation may be done using `^` with an exponent higher than 0, but lower than 1. To perform a nth root you may use the exponent `(1/n)`.
For square roots you may use `math.sqrt()`

```lua
local squareRoot = 16^0.5
local squareRoot2 = math.sqrt(16)
local thirdRoot = 27^(1/3)
```

### Modulo

The modulo operation may be done using `%`.

```lua
local remainder = 14 % 5
```

### Logarithm

The logarithm operation may be done using `math.log()`

```lua
local logarithm = math.log(antilogarithm, base)
```

### See also

The [Lua 5.2 Reference](https://lua.org/manual/5.2/manual.html#6.6) for more operations possible with a number.

## Floats and Integers

You may have noticed that the documentation mentions `float` and `int`, but never `number`, when Lua only has the `number`data type.

Floats are decimal numbers, while integers are whole numbers. This distinction is important to let you know what kind of information you may give or receive.

Let's take player User IDs as an example: User IDs are whole numbers, but never numbers with a decimal component.
