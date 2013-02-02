Date: 2013-01-25
Title: HydroGadget Prototype Hardware Design
Tags: Hardware, Power Supply
Category: Design
Author: Eric McFall

Early on we decided that we wanted this project to be simple enough that a person relatively new to soldering could successfully assemble the board with pretty basic tools and supplies.  This ruled out using any surface mount component and using through hole exclusively.  We also wanted to limit the number of manufacturer specific or single source components we used to make it as easy as possible for people to find parts and avoid the hassle of discontinued components.  All but one of the components are “jellybeans”; meaning they are a generic part that can be sources from many different vendors and manufacturers.

The hardware concept is actually quite simple.  Power for the HydroGadget is taken from a 24VacRMS transformer that are standard for irrigation timers as the water valves are typically 24VacRMS.  The 24VacRMS passes through four diodes and a bypass capacitor produce a rectified signal.  This feeds a LM317 variable regulator configured to limit the output to about +34Vdc.  A tiny high efficiency dc to dc switching power regulator then  produces our +5Vdc system power.  I found that even though the transformers typically used all specify 24VacRMS, I found that with only a small load, the secondary voltage can be substantially beyond 24VacRMS.  Little RMS to peak math and found that a typical transformer can spit out as high as 41VacPeak.  The little dc to dc converter I found is great, but can only handle 36Vdc input.  Enter the ever flexible LM317.  With two resistors I can set the output voltage to 34Vdc, which the dc to dc converter can easily tolerate.  The LM317 has a useful little quirk that it is stable even when the input to output voltage difference is below the dropout voltage of about 2Vdc.  When the input voltage is below 36Vdc the output voltage is equal to the input voltage minus the dropout voltage.  So in essence, the LM317 is acting like a voltage limiter for the dc to dc converter.

The output board is not nearly as interesting.  A ribbon cable connecting the output board to the Raspberry Pi feeds the +5Vdc system power as well as the +3.3Vdc logic out signals from the Pi.  The logic out signals are run through a eight channel Darlington pair IC to minimize the load on the Raspberry Pis GPIO pins.  The Darlington pair IC drives four optocouplers with triac outputs.  These weak triacs then drive a much higher capacity triac which actually switches the 24VacRMS  on and off to the valves.  Besides the inherent safety advantage the optocouplers provide, it also adds flexibility to our design to switch different or higher voltages if someone wants to do that modification.  I’m very curious to see what people end up hacking HydroGadget to do.

-EM

Eric's OpenSouce Hardware Projects can be found on his blog: http://smokingcircuits.me/
