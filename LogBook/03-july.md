E-Plat LogBook July 2017
=======================

July #1
-------
- **Mon Jul  3 08:28:00 WIB 2017**
	- Translate.
- **Tue Jul  4 08:28:00 WIB 2017**
	- STNK.
- **Wed Jul  5 08:28:00 WIB 2017**
	- Revising proposal.
	- Card Reader in raspi: Omnikey 5427 CK.
		- Possibly using CCID driver.
		- https://pcsclite.alioth.debian.org/ccid.html
		- https://pcsclite.alioth.debian.org/ccid/shouldwork.html#0x076B0x5427
		- https://pcsclite.alioth.debian.org/ccid/readers/HID_OMNIKEY_5427_CK.txt
		- http://smalltechproblems.blogspot.co.id/2013/04/raspberry-pi-checkin-devices.html
- **Thu Jul  6 08:24:22 WIB 2017**
	- Continue working on the smart card reader.
	- http://www.utilities-online.info/articles/GettingStarted-With-SmartCard-In-Linux/
	- Done. First run `pcscd` daemon as a background process. Then run this command:

			pcsc_scan

	- TODO: write a program to read the card automatically.
		- https://pyscard.sourceforge.io/
		- https://ludovicrousseau.blogspot.co.id/2010/04/pcsc-sample-in-python.html?m=1
		- https://pyscard.sourceforge.io/pyscard-framework.html#framework-samples
	- E-KTP data is protected, to read a key is necessary.
		- http://nisura.blogspot.co.id/2013/01/mencoba-tes-baca-chip-e-ktp-sim-dki-dan.html
	- https://play.google.com/store/apps/details?id=sybond.poc.ektpread
	- http://www.datascrip.com/read/product_file_1735577b45dac15ca.pdf
- **Fri Jul  6 10:55:02 WIB 2017**
	- Troubleshooting Mas Alam's PC.
	- Managing the ITS website.

July #2
-------
- **Mon Jul 10 08:58:09 WIB 2017**
	- Setting up Ubiquiti outoor (non 5GHz).
	- Working on the android smart traffic light communication.
		- Mobile apps parametrs now working.
		- Web app showing the mapp is now on progress: flask by default look the html in the templates page.
		- Maps template is now working.
- **Sel Jul 11 10:00:58 WIB 2017**
	- working on the maps.
		- https://developers.google.com/maps/documentation/javascript/examples/icon-complex
		- https://developers.google.com/maps/documentation/javascript/examples/marker-remove
	- Use `flask socketio` extension on flask to implement web socket.
		- https://flask-socketio.readthedocs.io/en/latest/
		- nice explanation: https://www.fullstackpython.com/websockets.html
		- The websocket worked but it seems to be unstable. It often encounters connection lost and needs to reconnect.
		- The client side javascript is done by using `socket.io` library.
	- The basic idea is everytime the raspberry server receives an update request from an eplat, the raspberry server pushes the data to the webclient.
	- TODO:
		- make sure `ASyncTask` instance is killed properly after running the http request.
		- make sure both eplat->server and server->webclient connection work properly.
	- For ITS web: https://inet.detik.com/cyberlife/d-3183119/menyambut-era-sistem-transportasi-cerdas-di-indonesia
- **Rab Jul 12 09:26:14 WIB 2017**
	- Searching about Google Maps in Android.
		- https://developers.google.com/maps/documentation/android-api/map-with-marker
- **Kam Jul 13 09:55:26 WIB 2017**
	- Start to write the patent draft. Some examples:
		- https://www.google.co.id/patents/US8253593?dq=traffic+light+system&hl=nl&sa=X&ved=0ahUKEwiJ04XqsIXVAhUEsY8KHU5jD6kQ6AEITzAF
		- https://www.google.co.id/patents/US7884738?dq=traffic+light+system&hl=nl&sa=X&ved=0ahUKEwiJ04XqsIXVAhUEsY8KHU5jD6kQ6AEIajAI
		- https://www.google.co.id/patents/US7821422?dq=traffic+light+system&hl=nl&sa=X&ved=0ahUKEwiJ04XqsIXVAhUEsY8KHU5jD6kQ6AEIczAJ
- **Jum Jul 14 10:15:15 WIB 2017**
	- Drafting patent.

July #3
-------
- **Sen Jul 17 09:16:17 WIB 2017**
	- Drafting Patent.
	- Meet Pak Selo.
- **Sel Jul 18 09:16:17 WIB 2017**
	- Drafting Patent.
	- What is currently not present in the patent draft:
		- Detailed block diagram, showing the relay, raspberry pi, ubiquiti access point, and stuff.
		- Time sequence diagram, presenting the communication between the vehicle and the traffic controller in a timely manner.
		- Flowchart of the system.
		- VANET communication scheme that bridges a traffic light to another using vehicles.
		- The corresponding description of those figures.
	- Start to write mid-term report.
	- Working on cabling.
	- Potential conference:
		- http://snti.untar.ac.id/index.php/call-for-paper/topik-seminar
		- http://semnastek.umj.ac.id/
		- http://sisfotek.org/
		- http://sinaptika.mercubuana.ac.id/news.php
	- Looking for some info about conference.
- **Rab Jul 19 09:27:12 WIB 2017**
	- Writing the mid-term report.
	- Deciding which conference to go for.
- **Kam Jul 20 09:51:33 WIB 2017**
	- Finalizing mid-term report.
- **Jum Jul 21 09:08:16 WIB 2017**
	- Finalizing mid-term report.

July #4
-------
- **Sen Jul 24 10:14:11 WIB 2017**
	- SKK Migas.
	- Got the practicals handbook for buku ajar.
- **Sel Jul 25 10:14:11 WIB 2017**
	- SKK Migas.
	- Away (Jakarta).
- **Rab Jul 26 10:14:11 WIB 2017**
	- Away (Jakarta).
- **Kam Jul 27 10:14:11 WIB 2017**
	- Start writing manuscript for seminar nasional.
