# RF Exploitation demo using RC Tanks

![tank banner](./images/banner.png)

This repo is meant to act as a demo and reference point when doing RF exploitation with GNURadio.  For the purpose of the demo we will be going over how to hack an RC toy, the [RC Fighting Battle Tanks by Liberty Imports](https://www.amazon.com/dp/B00GA97CUG).  At the time of this writing, these are available on Amazon for $25 for the pair.  These tanks are nice to practice and learn with, because they use a very simple AM On Off Keying modulation scheme to communicate.  

## Background

RF Exploitation is a fun field, I've been doing it almost my entire career, but it can be very hard to get into due to there not being many intro level tutorials for people who are RF and looking to use it from a hacking / pen testing standpoint.  Hopefully this guide will help fill that gap and leave you knowing more instead of less.  

## Materials Needed

### Hardware

* A computer able to run [GNURadio](https://github.com/gnuradio/gnuradio)
* [RC Fighting Battle Tanks by Liberty Imports](https://www.amazon.com/dp/B00GA97CUG)
  * Note this is only if you want to follow along directly and try these attacks on your own.  
* A Software Defined Radio capable of transmitting on 27 MHz and 40 MHz
  * The scripts and captures in this tutorial were all done using a [HackRF One](https://greatscottgadgets.com/hackrf/one/)
  * If you only have an [RTL-SDR](https://www.rtl-sdr.com/buy-rtl-sdr-dvb-t-dongles/) or other receive only SDRs, you can still record and decode your own captures but you will not be able to transmit.  

### Software

*  [GNURadio](https://github.com/gnuradio/gnuradio)
* [Inspectrum](https://github.com/miek/inspectrum)
* [Universal Radio Hacker](https://github.com/jopohl/urh)
* (Optional) Spectrum Analyzing software, Some examples are:
  * [QSpectrumAnalyzer](https://github.com/xmikos/qspectrumanalyzer)
  * [SDR#](https://airspy.com/download/)

## The Exploitation Process

Exploiting a system over RF involves three basic steps, Discovering and Identifying the signal, Analyzing said signal for vulnerabilities, and Transmitting your attack.  We're going to go over the following using the RC tank as an example target.  

### Discovery

Depending on what you are trying to exploit, you'll often start with one of two initial problems, either you are trying to figure out on what frequencies a device radiates, or you are noticing a signal in the wild and trying to identify what that device is.  By the nature of our work, we're often times targeting systems that are using non-standard or proprietary data links, and the more documentation and research you can discover about them, the easier your life will get when it comes time to analyze and exploit.  

Lets start with the first problem, since we have the toy tank and are trying to figure out what frequency it radiates on.  In this case the first thing you should do, if in the USA at least, is to look to see if there is an FCC ID somewhere on the device.  If there is, that means the device manufacturer has submitted paperwork to the FCC saying what frequency or frequencies they transmit on, as well as some other information about signal strength, components, etc...  Sites like [FCCID](https://fccid.io/) will let you search the FCC database by FCC ID and list the public documents that the FCC has on the device.  