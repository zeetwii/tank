# RF Exploitation demo using RC Tanks

![tank banner](./images/banner.png)

This repo is meant to act as a demo and reference point when doing RF exploitation with GNURadio.  For the purpose of the demo we will be going over how to hack an RC toy, the [RC Fighting Battle Tanks by Liberty Imports](https://www.amazon.com/dp/B00GA97CUG).  At the time of this writing, these are available on Amazon for $25 for the pair.  These tanks are nice to practice and learn with, because they use a very simple AM On Off Keying modulation scheme to communicate.  

## Background

RF Exploitation is a fun field, I've been doing it almost my entire career, but it can be very hard to get into due to there not being many intro level tutorials for people who are RF and looking to use it from a hacking / pen testing standpoint.  Hopefully this guide will help fill that gap and leave you knowing more instead of less.  

## Hardware Needed

* A computer able to run [GNURadio](https://github.com/gnuradio/gnuradio)
* [RC Fighting Battle Tanks by Liberty Imports](https://www.amazon.com/dp/B00GA97CUG)
  * Note this is only if you want to follow along directly and try these attacks on your own.  
* A Software Defined Radio capable of transmitting on 27 MHz and 40 MHz
  * The scripts and captures in this tutorial were all done using a [HackRF One](https://greatscottgadgets.com/hackrf/one/)
  * If you only have an [RTL-SDR](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) or other receive only SDRs, you can still record and decode your own captures but you will not be able to transmit.  


