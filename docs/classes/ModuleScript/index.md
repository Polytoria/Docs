# ModuleScript
ModuleScript is a class that inherits from [BaseScript](../BaseScript) and can be used to share things between scripts. They are synced across the server and client, and can be used with the `require` function to load them. Beware that ModuleScripts may not be loaded when other scripts are running, so you should add a `wait` at the beginning of your script to ensure that it is loaded before you use it.

Currently, functions are not supported in ModuleScripts.

Inherited from [BaseScript](../BaseScript)
