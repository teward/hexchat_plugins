# ChanUserMatch

## What is this module?

This module is capable of doing matching upon ```user!ident@host#realname``` pattern matching against the open channel.

Output from this module are as follows:
 * A line saying how many users were matched.
 * If any users were matched, it outputs a list (```['nick', 'nick2', 'nick3', ...]```) of nicknames which match.
 
## Syntax

### Pattern Syntax

This plugin accepts a very specific syntax.  You must provide one of the following syntaxes.

If you do not have any need to run any realname matching the syntax for the pattern is this:  ```nick!ident@host```

If you wish to do any realname matching the syntax for the pattern is this: ```nick!ident@host#realname```.

Any portion (```nick```, ```ident```, ```host```, or ```realname```) of the pattern masks below can be replaced with an asterisk wildcard, but you cannot remove the ```!```, ```@```, or ```#``` from your entered pattern.

### Using the Command

To use the plugin, simply use this syntax: ```/chanusermatch pattern```
