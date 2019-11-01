### Simple GUI to display Air Sensor Data

#### Requirements:
* Tkinter ```sudo apt-get install python3-tk```
* PIL ```sudo pip install pillow```

#### Other
* Turn off screen saver ```sudo apt-get install xscreensaver``` [Turn off screensaver](https://www.geeks3d.com/hacklab/20160108/how-to-disable-the-blank-screen-on-raspberry-pi-raspbian/)

```bash
$ sudo xset s off
$ sudo xset -dpms
$ sudo xset s noblank
```
* ```xset q``` and turn off _dpms_ ```xset dpms```

#### Troubleshooting
* If You're using 3.5 Display like me it's could be necessary to run ```export DISPLAY=:0```

#### To Do:
* Change to using Canvas