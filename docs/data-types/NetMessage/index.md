# NetMessage

### Description

NetMessage is a data type used for transporting data between client and server.

### Constructors

| NetMessage.New()          |
| ------------------------- |
| Creates a new NetMessage. |

### Functions

| `void` NetMessage.AddString(`string` key, `string` value) |
| --------------------------------------------------------- |
| Sets a string value.                                      |

| `string` NetMessage.GetString(`string` key) |
| ------------------------------------------- |
| Gets a string value.                        |

| `void` NetMessage.AddInt(`string` key, `int` value) |
| --------------------------------------------------- |
| Sets an int value.                                  |

| `int` NetMessage.GetInt(`string` key) |
| ------------------------------------- |
| Gets an int value.                    |

| `void` NetMessage.AddNumber(`string` key, `number` value) |
| --------------------------------------------------------- |
| Sets a number value.                                      |

| `number` NetMessage.GetNumber(`string` key) |
| ------------------------------------------- |
| Gets a number value.                        |

| `void` NetMessage.AddBool(`string` key, `bool` value) |
| ----------------------------------------------------- |
| Sets a boolean value.                                 |

| `bool` NetMessage.GetBool(`string` key) |
| --------------------------------------- |
| Gets a boolean value.                   |

| `void` NetMessage.AddVector2(`string` key, `Vector2` value) |
| ----------------------------------------------------------- |
| Sets a Vector2 value.                                       |

| `Vector2` NetMessage.GetVector2(`string` key) |
| --------------------------------------------- |
| Gets a Vector2 value.                         |

| `void` NetMessage.AddVector3(`string` key, `Vector3` value) |
| ----------------------------------------------------------- |
| Sets a Vector3 value.                                       |

| `Vector3` NetMessage.GetVector3(`string` key) |
| --------------------------------------------- |
| Gets a Vector3 value.                         |

| `void` NetMessage.AddColor(`string` key, `Color` value) |
| ------------------------------------------------------- |
| Sets a Color value.                                     |

| `Color` NetMessage.GetColor(`string` key) |
| ----------------------------------------- |
| Gets a Color value.                       |

| `void` NetMessage.AddInstance(`string` key, `Instance` value) |
| ------------------------------------------------------------- |
| Sets an Instance value.                                       |

| `Instance` NetMessage.GetInstance(`string` key) |
| ----------------------------------------------- |
| Gets an Instance value.                         |
