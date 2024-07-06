---
title: NetMessage
description: NetMessage is a data type used for transporting data between client and server.
icon: polytoria/NetMessage
---

# NetMessage

:polytoria-NetMessage: NetMessage is a data type used for transporting data between client and server when using {{ classLink("NetworkEvent") }}.

## Constructors

### NetMessage.New { method }

Creates a new NetMessage instance.

## Methods

### AddString(key;string,value;string) { method }

Sets a key as a string.

!!! warning "Limitations"
Adding a string longer than 65,535 characters will cause the message to be silently dropped during transmission, and the {{ classLink("NetworkEvent") }} will not be fired on the other side.

    If you need to send a large string, consider sending it in smaller chunks.

### GetString(key;string):string { method }

Gets the value of a string key.

### AddInt(key;string,int;int) { method }

Sets a key as an integer.

### GetInt(key;string):int { method }

Gets the value of an integer key.

### AddNumber(key;string,number;float) { method }

Sets a key as a float.

### GetNumber(key;string):float { method }

Gets the value of a float key.

### AddBool(key;string,bool;boolean) { method }

Sets a key as a boolean.

### GetBool(key;string):boolean { method }

Gets the value of a boolean key.

### AddVector2(key;string,vector2;Vector2) { method }

Sets a key as a Vector2.

### GetVector2(key;string):Vector2 { method }

Gets the value of a Vector2 key.

### AddVector3(key;string,vector3;Vector3) { method }

Sets a key as a Vector3.

### GetVector3(key;string):Vector3 { method }

Gets the value of a Vector3 key.

### AddColor(key;string,color;Color) { method }

Sets a key as a Color.

### GetColor(key;string):Color { method }

Gets the value of a Color key.

### AddInstance(key;string,instance;Instance) { method }

Sets a key as an Instance.

### GetInstance(key;string):Instance { method }

Gets the value of an Instance key.
