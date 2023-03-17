#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2023 ZeeTwii.
#
# SPDX-License-Identifier: GPL-3.0-or-later
#

import numpy as np# needed for gnuradio
from gnuradio import gr # needed for gnuradio
import socket # needed for UDP socket

class spoofer(gr.sync_block):
    """
    docstring for block spoofer
    """
    def __init__(self, portNum):

        # create UDP socket
        self.recSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        
        # bind socket
        self.recSocket.bind((str('0.0.0.0'), int(portNum)))

        print(f"Binding Socket to: {str('0.0.0.0')} , {str(portNum)}")

        # set socket to nonblocking
        self.recSocket.setblocking(False)
        self.recSocket.settimeout(0)

        # variables for rc tank

        oversample = 1000

        # repeat counter
        self.repeat = 4
        
        # turning jamming on or off
        self.jamming = False 

        # used to store untransmitted parts of message between loops
        self.oldMsg = ''

        # both sides forward command
        self.bF = ''
        for char in '101110111010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010111011':
            self.bF += char * int(oversample)

        # both sides reverse
        self.bR = ''
        for char in '101110111010101010101010101010101010101010101010101010101010101010101010101010111011':
            self.bR += char * int(oversample)

        # fire cannon
        self.fC = ''
        for char in '101110111010101010101010101010101010101010101010101010111011':
            self.fC += char * int(oversample)

        # left forward
        self.lF = ''
        for char in '101110111010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010111011':
            self.lF += char * int(oversample)

        # left reverse
        self.lR = ''
        for char in '101110111010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010111011':
            self.lR += char * int(oversample)

        # right forward
        self.rF = ''
        for char in '101110111010101010101010101010101010101010101010101010101010101010101010101010101010101010111011':
            self.rF += char * int(oversample)

        # right reverse
        self.rR = ''
        for char in '101110111010101010101010101010111011':
            self.rR += char * int(oversample)

        # start and stop
        self.st = ''
        for char in '101110111010101010101010101010101010101010111011':
            self.st += char * int(oversample)

        gr.sync_block.__init__(self,
            name="spoofer",
            in_sig=None,
            out_sig=[np.float32])


    def work(self, input_items, output_items):
        out = output_items[0]
        
        # if jamming set everything to 1 otherwise set everything to zero
        if self.jamming:
            out[:] = float(1)
        else:
            out[:] = float(0)

        # empty message
        msg = ''

        # try to read the socket
        try:
            oriMsg =  self.recSocket.recv(4096).decode()

            userCommand = str(oriMsg)
            print(f"Got: {userCommand}")

            # clear out the old command
            self.oldMsg = ''

            if userCommand == 'j0':
                self.jamming = False
            elif userCommand == 'j1':
                self.jamming = True
            elif userCommand == 'bf': 
                msg = self.bF * self.repeat
            elif userCommand == 'br': 
                msg = self.bR * self.repeat
            elif userCommand == 'fc': 
                msg = self.fC * self.repeat
            elif userCommand == 'lf': 
                msg = self.lF * self.repeat
            elif userCommand == 'lr': 
                msg = self.lR * self.repeat
            elif userCommand == 'rf': 
                msg = self.rF * self.repeat
            elif userCommand == 'rr': 
                msg = self.rR * self.repeat
            elif userCommand == 'st': 
                msg = self.st * self.repeat
            else:
                print("warning, unknown command")
                msg = '000000000000'
    
        except socket.error: # gets called when socket timesout
            if len(self.oldMsg) > 0: # there is still data to send
                msg = self.oldMsg
                self.oldMsg = ''
            else:
                if self.jamming:
                    msg = '111111111' # blank message
                else:    
                    msg = '0000000000' # blank message
        
        
        # test if out or msg is shorter: only needed for startup
        if len(msg) > len(out):
            size = len(out)
            self.oldMsg = msg[size:] # save the untransmitted data for next cycle
            #print(f"message to big, max size {str(size)}")
        else:
            size = len(msg)
        
        for i in range(size):
            if msg[i] == '1':
                out[i] = float(1)
            else:
                out[i] = float(0)


        return len(output_items[0])
