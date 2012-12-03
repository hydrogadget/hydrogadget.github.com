Date: 2012-11-19
Title: Fire up Microsoft Project and find a PMP!
Tags: Hardware Startup, Raspberry Pi
Category: Design
Author: Brian Munroe


Ok, not really...but Charles, Mike and myself have been meeting on a regular basis for about a month
now and we've come up with a dumptruck load of design requirments.  We've pared
it down to a few that we think we can make for the Feb 2nd LV Mini Maker
Faire deadline:

### Phase One Reqirements ###

1.  Must be inexpensive to build.
2.  Must have a sensible and intuitive web / mobile interface.
3.  Must minimize waste - should act as a drop-in replacement for an existing residential
irrigation timer.
4.  THE BIG ONE:  Must be able to communicate with the water utility to determine
the water restriction schedule.


Most of these requirements are pretty straightforward, but #4 is the most exciting
to me.  Before starting this project, I googled around and found plenty of DIY
sprinkler controllers, but none of them had the ability to communicate with a
third party.  


Here in Southern Nevada (namely, Las Vegas), we have mandatory drought restriction
watering schedules.  These change on a quarterly basis and usually
customers are notifed via a postcard to adjust them.  People sometimes ignore the
notices, but most of the time, people just forget to change the schedules, even
with the reminder.


With the HydroGadget, we want to elimate this by allowing the system to
continually poll the water utility to determine the restriction schedule.  It then
would either adjust things automatically or at least send an email / SMS reminder 
that things need to be changed.


We think this will be something that the water utility would be really interested
in as well.  Eliminating water waste is easy once it is highly automated.


Additionally, we'd like to use the HydroGadget as a demostration platform for
showing how valuable public data APIs are.  Our phase one plans are to screen
scrape the water utility's website to determine the restriction schedule, but
eventually we'd like to work with them to develop a web API that the HydroGadget
and other devices could leverage.


### Choosing Hardware for the Controller ###

As far as choosing a platform, the HydroGadget team members have been playing around with the [Raspberry Pi](http://www.raspberrypi.org/) and we all think it will make an excellent controller for our project.


We originally started to take some inspiration from [Jeff
Keyzer's](http://mightyohm.com/blog/about/)[WiFi
Radio](http://mightyohm.com/blog/2008/10/building-a-wifi-radio-part-1-introduction/)
project.  Jeff did a really good job of documenting this fantastic project and we
could easily see how it could be adapted to fit our project.  However we decided that
if we wanted to make a production run of these things then using a Wifi router as
our platform would be too wasteful (we'd have to throw away the case and the
router power supply) and it would also be very time consuming to add the required
serial header to the router mainboard.


The Raspberry Pi is a very inexpensive (~$35US) and low power ARM based computer that runs Linux
and has enough general purpose Input-Output (GPIO) that we can control the
sprinkler valve solenoids without having to add a lot of extra components.

