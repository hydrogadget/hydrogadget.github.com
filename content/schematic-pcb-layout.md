Date: 2013-03-31
Title: HydroGadget Rev 0.F Schematic & PCB Layout
Tags: Hardware 
Category: Design
Author: Eric McFall

I really meant to get this finished and published a month ago, but life got in the way.  Put in a whole lot of extra hours producing a special one time Cirque du Soleil production in our showroom to benefit “One Drop“, a world water access charity.  The event was a huge success bringing awareness and financial support for One Drop, but it was a lot of work to get it there.

I tweaked a couple of things on the design schematic to make testing the performance of the circuits a bit easier.  I have a handful of header and shunt sets along the power paths to allow me to interrupt the trace and measure current passing from one component to the next.  I’m becoming less and less fond of my power supply design, so don’t be surprised if you see something completely different on the next revision.  I also split up the main filtering capacitor into three separate smaller capacitors.  Something smells fishy about my ripple calculations and this allow me to easily add filter capacitance in stages and see how my circuit responds.  If I do end up using this basic power supply design I want to know how close I am to the margins.  There is also an additional LED that is going to indicate the health of the programs running on the Raspberry Pi.  If everything is healthy it should blink briefly every 5 seconds or so.  If the LED is stuck on or doesn’t blink, we know something has crashed on the Pi and an investigation is in order.

One issue that we are trying to tackle is how do we initially configure the HydroGadget network settings and how would adjust those settings if we changed the name or password of the wireless network it attaches to.  We decided that a network settings reset switch would be needed to put the HydroGadget into an ad hoc wireless mode to allow a computer or phone to connect directly to the HydroGadget.  Once the HydroGadget is told what network to attach to and what password to use it would then go back to a client mode and connect to the wireless network like any other device would.  One of these classic chicken and egg problems.  A simple tactile push button and some resistors and we now have a magic reset switch.  At the request of one of our programmers, I added a simple serial in/out port to allow for debugging code.

The layout is definitely a work in progress.  I’m pretty sure the design of the output side is fairly solid, so I spent a fair bit of time getting that section of the layout nice and clean.  As I said earlier, the power supply concept might very well change completely, so that side of the layout isn’t nearly as polished.  I had to back mount the filter capacitors to try to keep the profile reasonably tight so designing a case for this wouldn’t be a complete disaster.  Since I had the space for the LM317 to mount to the board, I poured a large ground plan on both sides to act as a little heatsink and riddled the section directly under the LM317 with vias to help transfer heat to the back plane.

I fully expect there to be at least one big mistake on this board revision that will require all types of fun hacking.  I’ll be sure to post pictures of my butchering.  From talking with seasoned professionals, you never get it right on the first spin.  I sent in my gerber set tonight to my friends at OSHPark so I should have three boards show up in my mailbox in about 14 days.  I have included all my source files in the link below.  Stay tuned for the next update.

[Download: HydroGadget-Rev-0.F](https://www.box.com/s/bhgditxoie52h2e5ruh8)

<center>
![Front Side](http://i.imgur.com/GPdDpeml.jpg)

![Back Side](http://i.imgur.com/fcOoYRvl.jpg)
</center>

Eric's OpenSouce Hardware Projects can be found on his blog: [SmokingCircuits.me](http://smokingcircuits.me/)
