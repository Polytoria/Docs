---
title: NetMessage
description: NetMessage is a data type used for transporting data between client and server.
icon: polytoria/NetMessage
---

# NetMessage

:polytoria-NetMessage: NetMessage is a data type used for transporting data between client and server when using {{ classLink("NetworkEvent") }}.

## Constructors

| Name                                                      | Description                         |
| --------------------------------------------------------- | ----------------------------------- |
| NetMessage.New()                                          | Creates a new NetMessage.           |
| NetMessage.AddString(`string` key, `string` value)        | Sets a key as a string.             |
| NetMessage.GetString(`string` key)                        | Gets the value of a string key.     |
| NetMessage.AddInt(`string` key, `int` int)                | Sets a key as an integer.           |
| NetMessage.GetInt(`string` key)                           | Gets the value of a integer key.    |
| NetMessage.AddNumber(`string` key, `float` number)        | Sets a key as a float.              |
| NetMessage.GetNumber(`string` key)                        | Gets the value of a float key.      |
| NetMessage.AddBool(`string` key, `boolean` bool)          | Sets a key as a boolean.            |
| NetMessage.GetBool(`string` key)                          | Gets the value of a boolean key.    |
| NetMessage.AddVector2(`string` key, `Vector2` Vector2)    | Sets a key as a Vector2.            |
| NetMessage.GetVector2(`string` key)                       | Gets the value of a Vector2 key.    |
| NetMessage.AddVector3(`string` key, `Vector3` Vector3)    | Sets a key as a Vector3.            |
| NetMessage.GetVector3(`string` key)                       | Gets the value of a Vector3 key.    |
| NetMessage.AddColor(`string` key, `Color` Color)          | Sets a key as a Color.              |
| NetMessage.GetColor(`string` key)                         | Gets the value of a Color key.      |
| NetMessage.AddInstance(`string` key, `Instance` Instance) | Sets a key as an Instance.          |
| NetMessage.GetInstance(`string` key)                      | CGets the value of an Instance key. |
