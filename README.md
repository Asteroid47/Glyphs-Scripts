# Glyphs Scripts
Python scripts for use with Glyphs.

# INSTALLATION

1. Put the scripts folder (or an alias) into the *Scripts* folder which appears when you choose *Script > Open Scripts Folder* (Cmd-Shift-Y): `~/Library/Application Support/Glyphs/Scripts/`
2. Then, hold down the Option (Alt) key, and choose *Script > Reload Scripts* (Cmd-Opt-Shift-Y). Now the scripts are visible in the *Script* menu

# Scripts

## Designspace

### Create varLib Designspace document

Creates a designspace document for use with interpolatable .ttfs and the varLib (fonttools) compiler.

*Requires a customParameter "isDefault" in a master for the default axis vaules to be set.*

Use:
```bash
$ fonttools varLib path/to/designspace+interpolatableTTFs
```
to compile a Variable TTF.



# Contact
Drop me an e-mail: theo@tderewnicki.co.uk