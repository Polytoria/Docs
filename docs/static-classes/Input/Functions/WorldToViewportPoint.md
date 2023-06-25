# WorldToViewportPoint

### Description

Transforms `worldPosition` from world space into viewport space. <br />
Viewport space is normalized and relative to the camera. <br />
The bottom-left of the camera is (0,0); the top-right is (1,1). The z position is in world units from the camera.

Function of [Input](../../)

#### Parameters

worldPosition `Vector3`

#### Return type

`Vector3`

### Example

```lua
Input.WorldToViewportPoint(worldPosition)
```
