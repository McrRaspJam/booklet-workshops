# Directories

## Where am I?

Once you've logged in, you should see a line that looks like this.

```bash
pi@raspberrypi:~$
```

This is your command prompt. Let's break up that line.

- The first part is the current user. We logged in as `pi`, so that appears here.
- Following the `@` is the hostname, or the name given to the computer. `raspberrypi` is the default hostname in Raspbian.
- Following the colon, your current director is shown. The tilde character `~` is a shortcut for your home folder.
- `$` is the current prompt. When this is the last thing printed, the terminal is ready to receive an instruction.

Let's confirm that the tilde is pointing at our home folder. To find the full address to our current directory, we can use the `pwd` command, which stands for 'print working directory'.

```bash
pi@raspberrypi:~$ pwd
/home/pi
```

## Moving Around

We're currently in our home directory, and there are two levels above us. to move to the root folder, we can use the `cd` command, which stands for 'change directory'.

```bash
pi@raspberrypi:~$ cd ..
pi@raspberrypi:/home $ cd ..
pi@raspberrypi:/ $ pwd
/
```
**..** causes us to move up a directory. to move into a directory, we can type its name.

```bash
pi@raspberrypi:/ $ cd usr
pi@raspberrypi:/usr $ pwd
/usr
```

We can type an absolute directory starting with `/`, the root folder.

```bash
pi@raspberrypi:/usr $ cd /media
pi@raspberrypi:/media $ pwd
/media
```

Using the cd command without a directory or `..` takes us to the home folder. We can string together directory changes using forward slashes.

```bash
pi@raspberrypi:/media $ cd
pi@raspberrypi:~ $ pwd
/home/pi
pi@raspberrypi:~ $ cd ../../usr
pi@raspberrypi:/usr $ pwd
/usr
```

Now have a go at finding at finding the location of the Python 3 binary executable. You can use the `whereis` command to find the location of a program.

```bash
$ whereis python3
```

The first part of the output will be the directory of the binary file.
