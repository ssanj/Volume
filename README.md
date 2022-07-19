# Volume

A [Sublime Text](https://www.sublimetext.com/) Command to allow progressively running other commands supplied as a list of arguments.


## Installation

- Open the command palette with `CMD + SHIT + P`
- Select `Package Control: Add Repository`
- Enter https://github.com/ssanj/Voume for the repository
- Select `Package Control: Install Package`
- Choose Volume


## Functionality

### Volume Invocation

A volume invocation is a composite of a **key-combination** along with a **list of commands** to run.

An example Volume Invocation from the user key-bindings file:

```
    {
        "keys": ["f11"], //key-combo
        "command": "volume", //this command
        "args":
        {
          "commands":[ //list of commands you want run in order
              {
                "command": "set_layout", //run when index is 0 (first invocation)
                "args": {
                      "cols": [0.0, 1.0],
                      "rows": [0.0, 0.5, 1.0],
                      "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
                 },
              },
              {
                "command": "set_layout",  //run when index is 1  (second invocation)
                "args": {
                      "cols": [0.0, 1.0],
                      "rows": [0.0, 0.75, 1.0],
                      "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
                },
              },
              {
                "command": "set_layout",  //run when index is 2  (third invocation)
                "args": {
                      "cols": [0.0, 1.0],
                      "rows": [0.0, 0.95, 1.0],
                      "cells": [[0, 0, 1, 1], [0, 1, 1, 2]]
                },
              }
          ],
        }
    },
```

The above configuration changes the height of a horizontal split on each volume invocation (pressing the `F11` key). You can configure many such volume invocations. Another obvious one is to create a configuration for vertical split resizing. In the example below I've created both mappings, one for `F11` as above and another for `SHIFT` + `F11` which resizes vertically.

![Volume Example](volume-example.gif)

This command provides two capabilities:
1. It keeps track of the current index of a particular volume invocation. Each time the key-combo is used the index is increased. The index rotates by default (goes back to zero)
2. The command configured at that index is invoked. For the moment the command at the current index is invoked using `window.run_command`.


## Sample Arguments to a Volume Invocation

```
{
  "commands":[
      {
        "command": "command_name1",
        "args": {
          //command1 arguments
         },
      },
      {
        "command": "command_name2",
        "args": {
          //command2 arguments
         },
      },
      // other commands...
  ],
}
```


