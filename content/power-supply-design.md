Date: 2012-12-02
Title: Dear Wire Inductance..Go To Hell!
Tags: Hardware Startup, Power Supply, Hurt Feelings
Category: Design
Author: Brian Munroe


We got our first lesson in electical engineering 101 at last night's [SYN
Shop](https://synshop.org) meetup.


One of the requirements for the device is to use the existing irrigation
controller power supply.  To use this, we needed to convert the power from 24VAC to
5VDC.  Having never done this before and always up for the challenge, I fired up the internet and tried to determine
what components we needed to build our own power supply.


Ordering about $10 worth of parts (RF choke?  Whatever that is!) I tried my hand
at assembling the circuit following the data sheet from the DC-DC converter.


<img src="http://i.imgur.com/kbABb.jpg?sss" alt="" title="Hosted by imgur.com" />


After wiring it up, I was too tired and scared to plug it in to test it, so I
waited until the SYN Shop meetup to get a second set of eyes on my circuit.  At
the meetup, my good friend Josh looked over the converter datasheet and my wiring
job, gave me the thumbs up and I plugged it in.  Putting the volt meter on the
output leads....


** Zero volts **


Awe man, now what is wrong?


I started picking apart my circuit, looking for mistakes and trying to confirm
that I hadn't blown a part somewhere along the way.  After about 10 minutes of
doing that and finally throwing my hands up in the air, two SYN Shop regulars, Charley and Nathan came over and started looking at what I was doing.


Charley asked a few basic questions and finally said, "This circuit is way too
sensitive to inductance for you to be using that rat's nest of jumpers.  You need
to use perfboard and much shorter wire lengths".


Nathan confirmed Charley's assessment and retold a story about how he too had
been bitten by this same exact problem.  However, instead of telling me "good
luck!", Nathan went over to his box of components and pulled out an all in one
DC-DC converter, handed it to me and said "Here, just use this"

So now, instead of this wild mess of wires and various components (I did learn
what the RF choke does!  Thanks Charley!), the HydroGadget power circuit looks
like this:

<img src=http://i.imgur.com/lZaf4.jpg" title="Hosted by imgur.com" />


After a lot of back and forth, I decided that the even though it feels like
cheating using this [fancy-pants
converter](http://www.mouser.com/ProductDetail/Murata-Power-Solutions/OKI-78SR-5-15-W36-C/?qs=sGAEpiMZZMtwaiKVUtQsNemMZL4TplJBqOl7845nWHA%3d),
we will suck it up for now...probably :-)
