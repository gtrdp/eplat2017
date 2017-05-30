E-Plat LogBook May 2017
=======================

May #3
------
- **Mon May 15 10:07:12 WIB 2017**
	- Kick off meeting.
- **Tue May 16 10:07:12 WIB 2017**
	- Beginning the real work.
	- Installing UniFi router (need ethernet cable).
	- Setting up Raspi (need keyboard).
	- Setting up the desktop computer: resetting password etc.
- **Rab Mei 17 12:06:07 WIB 2017**
 - Installing Raspbian (cancelled).
- **Kam Mei 18 10:02:04 WIB 2017**
	- Met Rudi P.
- **Jum Mei 19 09:21:42 WIB 2017**
	- Setting up unifi.
		- AP cannot be detected.

May #4
------
- **Sen Mei 22 10:11:18 WIB 2017**
	- UniFi AP is now discoverable (solution: the router needs upgrade).
	- Raspberrypi default password is `raspberry`.
	- Running web server using Python in raspberry pi
		- https://www.raspberrypi.org/learning/python-web-server-with-flask/worksheet/
	- Return `json` output in Flask
		- http://stackoverflow.com/questions/13081532/return-json-response-from-flask-view
- **Sel Mei 23 08:50:25 WIB 2017**
	- SKK Migas.
- **Rab Mei 24 08:50:25 WIB 2017**
	- Progress report DSSDI.
- **Kam Mei 25 08:50:25 WIB 2017**
	- Ascension Day.
- **Jum Mei 26 08:50:25 WIB 2017**
	- Installing flask.
	- https://stackoverflow.com/questions/32550487/how-to-print-from-flask-app-route-to-python-console
	- Setting up remote media mounting (SSHFS)
	- Setting up PyCharm and Android Studio

May #5
------
- **Sen Mei 29 08:41:17 WIB 2017**
	- Resizing hard drive.
- **Sel Mei 30 10:08:47 WIB 2017**
	- Setting up the reserver (raspi) to read JSON input.
	- JSON test data:
		```
		{"id": 12345, "lat":-7.797068, "long":-7.797068, 110.370529, "direction": "S"}
		```
	- The server now can read JSON input from HTTP POST request.
	- Map View in Android https://gist.github.com/joshdholtz/4522551
	- Get location on tap https://stackoverflow.com/questions/15362281/how-do-i-get-the-coordinates-of-a-map-on-tap-with-mapfragment-not-mapview
