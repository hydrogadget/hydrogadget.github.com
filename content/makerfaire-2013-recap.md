Date: 2013-02-03
Title: Mini-Makerfaire LV: The aftermath
Tags: Design, Mini Makerfaire LV
Category: Design
Author: Brian Munroe <brian.e.munroe@gmail.com>

I think it is safe to say that plenty of people were very excited to see
HydroGadget in a form other then a) a mess of wires and blown up components
and b) more then just hot air about a non existent project.

<img src="http://smokingcircuits.files.wordpress.com/2013/02/img_0752.jpg?w=250&h=187" alt="" title="Hosted by imgur.com" />

A HUGE thanks to [Eric](http://smokingcircuits.me/) for taking over the
electronics.  That power supply was a tricky little guy.  Luckily for us, Eric
worked through a lunch break and produced something that didn't constantly let out
the blue smoke and / or simultaneously destroy the Raspberry Pi.

In summary, people were genuinely excited about it.  I explained the reason why I
wanted to scratch this itch and I found that people were actively agreeing with me to the
point of wanting to buy the prototype as is.

I'm not 100% sure it is clear from the previous blog posts as to why we decided
to do this.  So I'll recap a little:

* Build A Better Interface - Now I'm no Jacob Nielson, but I knew I could build a better interface then the existing one.  HydroGadget was born out of frustration trying to use a bizzaro UI that not even my landscaper could figure out (seriously).  I followed the natural progression of things and decided it should be a web app for sure. At the final hour I added a smartphone / mobile UI too.  All it does is allow you to turn valves on or off remotely, but it is super helpful for troubleshooting sprinkler head repairs.  You no longer have to run around to the front of the house to turn on the valve and then run back to where you were working.  Just fire up your phone.

* Water Conservation - In Southern Nevada, we have drought restriction schedules that must be followed, otherwise you run the risk of being fined or shamed into compliance by your neighbors.  The schedules change about every quarter and I know that a lot of people usually forget.  Since the device is connected to the internet already, it would be rather trivial to make it location aware.  By doing so, it could then query the local water utility and automatically adjust your watering days accordingly (or at least pester you via email / sms / twitter / facebook / irc / jabber / [Twilio](http://www.twilio.com/) / etc until you do so :-)

* Practice What I Preach - As one of the founders of [SYN Shop](http://synshop.org), I constantly speak to people about making and failure and learning and collaboration all the time.  I figure I better put up or shut up, lest I be considered a poseur.

I also got very re-invigorated about this project after reading Chris Anderson's
book [Makers: The Next Industrial
Revolution](http://www.amazon.com/Makers-The-New-Industrial-Revolution/dp/0307720950).
The crazy thing is, the book starts off talking about irrigation timers and how he
collaborated with Ray (sorry Ray, I don't know your last name) to build
[OpenSprinkler](http://www.opensprinkler.com/).  I met Ray at the 2012 Makerfaire
San Mateo and he and I talked a little bit about my requirements.  He is a very nice guy and actually taught me about bridge rectifers while I was explaining my first approach, pre Raspberry Pi.  I suppose I could have borrowed from his design, but HydroGadget was supposed to be a learning exercise, at least initially.

I think we have a great team and MMF LV was a huge eye opening experience for us.
Tons of suggestions, feature requests, collaborations.  I figured one or two
people would be interested, but the design points really struck a chord with
makerfaire attendees, much to my surpise.  We are taking a little breather, but
definitely going to regroup and figure out what our next step is very quickly here.

If you are interested in keeping informed about the progress of HydroGadget, [please take this little survey](http://hydrogadget.org/info/) and we'll be in touch soon.
