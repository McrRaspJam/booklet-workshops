# Files

	Once you've picked a directory, you can use the `ls` command, which is short for 'list'.

```bash
 $ cd
~$ ls
Desktop Downloads Pictures python_games
```

Once we've found the file we're looking for, it's straightforward to edit it. For example, a text file could be opened using

```bash
~$ nano textfile.txt
```

If a file doesn't exist, most editor programs will create a new file with that name. Save this new file by pressing \textbf{Ctrl+O}, then quitting with \textbf{Ctrl+X}. Run ls again, and your file should now be present.

## Manipulating Files

Let's blitz through a few file operation commands.

To copy a file:

```bash
~$ cp textfile.txt anothertextfile.txt
```

To move a file:

```bash
~$ mv textfile.txt originaltextfile.txt
```

You'll note that both of these commands use the same parameters, the original file followed by the resulting file.

To remove a file:

```bash
~$ rm anothertextfile.txt
```

To make a directory:		

```bash
~$ mkdir textfile
```

We should be left with originaltextfile.txt and a directory. Try \textit{moving} the text file to within this new directory.

you can remove an empty directory with rmdir, but because ours has a file in it, we will delete it using the following command.

```bash
~$ rm -r textfile
```

-r is flag that tells rm to run recursively. There are lots of flags for most commands, for example try `ls -l`. you can view the flags of a program by viewing it's manual using the `man` command.

```bash
~$ man ls
```
