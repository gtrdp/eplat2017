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
