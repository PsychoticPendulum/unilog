# unilog

unilog is a simple logging library that prints to the screen and can also write the logs to a file with timestamps.
Current version is 1.3.7

## Usage
`from unilog import *`

You should set where the logfiles are written

`LOG.path = "/path/to/dir/"`

`LOG.file = "<filename>.log"`

You can also disable writing to file with

`LOG.writeToFile = False`


There are 3 levels

**INFO** A green box saying [ OK ] before the log.

**WARN** A yellow box saying [WARN] and also pausing the execution of the program until any key is pressed

**FAIL** A red box saing [FAIL] that exits out of the program.

## Examples

`Log(LVL.INFO, "This is some information")`

`Log(LVL.WARN, "This is a warning")`

`Log(LVL.FAIL, "Something went wrong")`
