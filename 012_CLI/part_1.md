# Starting at the Deep End

The Linux command line is usually accessed through one of two ways:

1. By opening a terminal window from the desktop.
2. By running the operating system in the command line mode.

When we use the latter method, the desktop environment won't start at all. We'll set our Pi's into this mode now, so we won't feel tempted to stray outside of the command line for this workshop.

## Enable boot to Console

Open a terminal window and type the following


```bash
$ sudo raspi-config
```

a bright blue menu should appear. Navigate to the following options using the arrow keys and enter.

- 3 Boot Options
- B1 Desktop/CLI
- B1 Console

Then navigate to Finish. You will be then asked if you wish to restart. Select Yes.

## Login

If you joined the Raspberry Pi community recently, you'll have always had the Raspberry Pi boot to desktop automatically.

We've now disabled this behaviour, and when we reboot our Pi, you'll be greeted with a login screen. The default Raspbian login credentials are as follows:

- **username:** pi
- **password:** raspberry

Take care when typing your password, it won't appear on screen as you type it, not even as asterisks or dots.
