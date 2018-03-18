# The Ultimate Command of Destruction

The Linux command line places a lot of trust in you. As far as it's aware, you're somebody who knows what your doing. If you don't know what you're doing, be careful.

We're going to have a look at some useful features of the command line, and see what happens when you combine them incorrectly.

### -f

`-f` stands for force, and on a command like `rm` skips any warning messages that would usually be created.

if we were trying to delete 1000 files which were set as read-only, we would usually have to answer a yes/no check on every single file. `-f` will stop that from happening, so the command would finish instantly.

```bash
$ rm -f readonlyfile
```

### sudo

`sudo` stands for superuser do. Any time we want to complete a command that requires a high level of authority, such as modifying the read-only files mentioned above, we run that command as a superuser using `sudo`.

```bash
$ sudo rm protectedfile
```

This command effectively means "I know what I'm doing", so make sure you do!

### Wildcards

In the CLI, the asterisk character `*` is used as a wildcard. If we wanted to delete all the .txt files from a directory filled with thousands of different files, we could find each one and manually type in

```bash
$ rm file23of9000.txt
$ rm file72of9000.txt
$ rm file73of9000.txt
$ rm file79of9000.txt
...
```

```bash
$ rm *.txt
```

would delete all of the files ending in `.txt`, just like we wanted. Likewise, to delete all the files beginning with the word 'January', we could do:
```bash
$ rm january*
```

But what if you tried a command such as `rm *`? By default it would stop within the current folder, and possibly the sub folders, but what if we accidentally told it not to?

## Making the wrong combination

The truly scary thing about the ultimate command of destruction is how inconspicuous it looks.

```bash
$ sudo rm -rf /
```
Let's break the command down.

`rm` is our standard remove file function. To it, we have supplied the flags `-rf`. `-f` means we know what we're doing, and `-r` means it will start at one point and work through every subdirectory it finds.

This is fine if we're trying to delete a Java Project folder, or a collection of cat pictures, but what directory have we supplied?

`/` is the root directory, the directory under which every single file on our computer is contained.

The Operating system would have stopped you, but we've ran it under `sudo`, so the computer's convinced we done this intentionally.

And now (if you're happy to wipe whatever SD card you're running on) you can try it on your Raspberry Pi.

A feature of modern Linux distributions, at this point the program throws one last warning at you to try and stop you.
If you're really *really* happy to lose all of your files, just add the flag it tells you to, and it will finally run your command.
I'd recommend adding the flag `-v` for dramatic effect, which will display the files as they're being deleted.

```bash
$ sudo rm -rfv /
```

#

Whilst it certainly is for your Raspberry Pi (until you reinstall NOOBS, that is), I thought I'd leave you with one story about accidental misuse of rm.

This story about a quite famous film company is available as a video at https://youtu.be/8dhp_20j0Ys, and a text article is available at http://bit.ly/2jgR3nC.
