### Command Line

- aka the `Terminal`
- Faster & more powerful way to maneuver operating systems than using a GUI (graphical user interface), like Windows Explorer.

#### Let's Talk Structure

- Operating systems organize their finders in a hierarchy (tree)
- As in, there's "parents" and "children".
- Relative to a base ROOT directory.
- Files and directories have absolute paths based on the root, where each level down adds a "/".
- `~` represents Home. It's the default directory upon opening the terminal.

#### Onto the Commands

- `pwd`: prints working directory. Tells absolute path of where you're at.
- `cd`: change directory.
- `ls`: lists the contents of a directory.
  - `-a`: lists all files (including hidden ones)
  - `-l`: longer format
- `mkdir`: make directory.
- `touch`: creates the file.
  - When you use `touch` on a file that exists, it gently updates the date/time of the file.
- `mv`: move/rename, depending on the context.
  - source: (mv cat.text dog.txt)
  - destination (mv myphotos/puppy.jpg yourphotos)
- `rm`: remove.
  - GONE FORFEVER.
- `rmdir`: removes empty directories.
  - Not really used.
  - `-r`: recursive. Go through everything and delete everything.
  - `-f`: force, to prevent warnings.
  - Definitely need to use the r.
- `chmod`: change permissions.
  - `-w`: writing

#### Execute Python

- use `python3` in terminal.
- filenames end in `.py`

#### File Comments

- While JavaScript uses `//`, Python uses `#`.
