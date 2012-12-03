Date: 2012-11-19
Title: Fire up Microsoft Project and find a PMP!
Tags: Hardware Startup, Raspberry Pi
Category: Design, Project Management
Author: Brian Munroe


Ok, not really...but Charles, Mike and myself have been meeting on a regular basis for about a month
now and we've come up with a dumptruck load of design requirments.  We've pared
it down to a few that we think we can make for the Feb 2nd LV Mini Maker
Faire deadline:


1.  Must be inexpensive to build.
2.  Must connect to the internet.
3.  Must have a sensible and inuitive (web) interface.
4.  Must minimize waste - be a drop-in replacement for an existing residential
irrigation timer.

5.  THE BIG ONE:  Be able to communicate with the water district to determine 


All of the HydroGadget team members have been playing around with the Raspberry Pi
platform and we all think it will make an excellent controller for our project.
We originally started to take some inspiration from [Jeff
Keyzer's](http://mightyohm.com/blog/about/) [WiFi
Radio](http://mightyohm.com/blog/2008/10/building-a-wifi-radio-part-1-introduction/)
project.  Jeff did a really good job of documenting this fantastic project and we
could easily see how we could adapt it to fit our needs.  However we decided that
if we wanted to make a production run of these things then using a Wifi router as
our platform would be too wasteful (we'd have to throw away the case and the
router power supply) and it would also be very time consuming to add the required
serial header to the router mainboard.
