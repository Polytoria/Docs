---
title: ScriptInstance
description: A ScriptInstance is a script that only runs on the server.

icon: polytoria/ScriptInstance
weight: 1
---

:polytoria-ScriptInstance: ScriptInstances run Lua code on the server. Any code that should be kept on the server (such as Datastores) should be kept in a ScriptInstance.

Some classes and functions are only callable through a ScriptInstance. You may find a server-exclusive warning with them in the Documentation.

{{ inherits("BaseScript") }}