# Contributing

Thanks for waiting to contribute to the new unofficial Polytoria documentation! If you can't contribute at this time please notify one of our contributors and tell them the change that should be made and they can do it for you. Otherwise, you can open a pull request and we'll either accept it or request changes depending on what the pull request is about.

## Dependencies

| Name                       | Version |
| -------------------------- | ------- |
| mkdocs                     | 1.5.3   |
| mkdocs-macros-plugin       | 1.0.5   |
| mkdocs-material            | 9.5.7   |
| mkdocs-material-extensions | 1.3.1   |
| mkdocs-nav-weight          | 0.2.0   |
| pymdown-extensions         | 10.7    |
| ghp-import                 | 2.1.0   |

## Notes

1. When creating a page make sure if it is a class it should have the corresponding icon at the start of the description
2. When creating a page it is recommended that if it is an abstract object (one that can't be created using `Instance.New()` and is only used a base/inheriting class for other parts) there is no description
3. When creating a note, make sure that it is encased in a `<div data-search-exclude markdown>` element to make sure that the note doesn't show up while searching the documentation

## Page Order

Pages should be ordered like this:

1. Events
2. Methods
3. Properties

## How-To Write

### How-To: Write Events

**Example:** `EventName(ParameterName;ParameterType=ParameterValue) { method }`

`EventName` is the name of the event

```
How-To: Write Parameters

Parameters for events exist to better show what information the event provides when fired. All parameters must be encased in () and parameters entirely are COMPLETELY OPTIONAL
ParameterName is the name of the parameter
ParameterType is the type of the value which this property expects
ParameterValue is the default value of the parameter (OPTIONAL)

The last part is a macro, that STAYS THE SAME for all events to make sure the code knows it's a event
```

### How-To: Write Methods

**Example:** `MethodName(ParameterName;ParameterType=ParameterValue):Type { method }`

`MethodName` is the name of the method

`Type` is the type that is returned when using this method (if it returns nothing/void then don't put any return type or colon; it's automatically added)

```
How-To: Write Parameters

Parameters for methods exist to better show what the method wants/needs when called. All parameters must be encased in () and parameters entirely are COMPLETELY OPTIONAL
ParameterName is the name of the parameter
ParameterType is the type of the value which this property expects
ParameterValue is the default value of the parameter (OPTIONAL)

The last part is a macro, that STAYS THE SAME for all methods to make sure the code knows it's a method
```

### How-To: Write Properties

**Example:** `PropertyName:Type=Value { property }`

`PropertyName` is the name of the property

`Type` is the type that is returned when reading the property and that the property is set to when set

`Value` is the default value of the property (OPTIONAL)

The last part is a macro, that **STAYS THE SAME** for all properties to make sure the code knows it's a property

### How-To: Write Macros

**Example:** `{{ service() }}` - returns a "this object is a service" notice when the site is live

To write macros, encase a function like `service()` (or another macro listed in the macro list below) in double curly brackets, also make sure to put `()` after the macro name like it's a function

## Lists

### Macros List

Macros are short commands you can put in documentation pages that will be replaced with notes. Macros that are not listed here but are found in the code are most likely macros used on hidden pages or for internal usage.

| Name                                      | Text                                                                                                                                                                                                                                             |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `{{ inherits(className) }}`               | **Text:** "Inherits className". "?" if no classLink exists under that className                                                                                                                                                                  |
| `{{ ambiguous(className, description) }}` | **Note:** "Not to be confused with className, description"                                                                                                                                                                                       |
| `{{ ambiguousMultiple(classes) }}`        | **Note:** "Not to be confused with [classes]"                                                                                                                                                                                                    |
| `{{ notnewable() }}`                      | **Note (warning):** "This object cannot be created by scripts using `Instance.New()`"                                                                                                                                                            |
| `{{ abstract() }}`                        | **Note (danger):** "This object exists only to serve as a foundation for other objects. It cannot be accessed directly, but its properties are documented below. Additionally, it cannot be created in the creator menu or with `Instance.New()" |
| `{{ service() }}`                         | **Note (example):** "This object is automatically created by Polytoria. Additionally, scripts cannot change its parent."                                                                                                                         |
| `{{ staticclass(className) }}`            | **Note (tip):** "This object is a static class. It can be accessed by using it's name as a keyword like this `className`. Additionally, it cannot be created in the creator menu or with `Instance.New()`"                                       |
| `{{ serverexclusive() }}`                 | **Note (warning):** "This is only available to the server. It can only be accessed within server scripts."                                                                                                                                       |
| `{{ clientexclusive() }}`                 | **Note (warning):** "This is only available to the client. It can only be accessed within local scripts."                                                                                                                                        |
| `{{ nosync() }}`                          | **Note (failure):** "This object does not sync across the server and client. It is recommended to avoid changing its properties from Scripts, as the changes will not be visible to players."                                                    |
| `{{ readonly() }}`                        | **Note (warning):** "This property is read-only and cannot be modified."                                                                                                                                                                         |
| ~~`{{ comingsoon() }}`~~                  | NOT CURRENTLY USED ANYWHERE                                                                                                                                                                                                                      |
| `{{ classlink(className) }}`              | **Returns:** The class specified as a link with the corresponding icon next to it. "?" if no classLink exists under that className                                                                                                               |
