# Glyphs Scripts
Python scripts for use with Glyphs.

# INSTALLATION

1. Put the scripts folder (or an alias) into the *Scripts* folder which appears when you choose *Script > Open Scripts Folder* (Cmd-Shift-Y): `~/Library/Application Support/Glyphs/Scripts/`
2. Then, hold down the Option (Alt) key, and choose *Script > Reload Scripts* (Cmd-Opt-Shift-Y). Now the scripts are visible in the *Script* menu

# Scripts

## Create varLib Designspace document

Creates a designspace document for use with interpolatable .ttfs and the varLib (fonttools) compiler.

```bash
$ fonttools varlib path/to/designspace
```

### Issues

*  Creates an empty file, designspace file doesn't exist. FIX: Run the script again.

