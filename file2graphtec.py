#!/usr/bin/env python3

#
# file2graphtec
#
# Send a file to a Graphtec vinyl cutter using libusb
#
# Copyright (c) 2013 Peter Monta <pmonta@gmail.com>
#

import sys
# import usb1
# import hid
import Graphtec

#
# open a graphtec vinyl cutter from a list of recognized devices
#

device_list = [
  (0x0b4d, 0x1121),     # Silhouette Cameo
  (0x0b4d, 0x1123),     # Silhouette Portrait
  (0x0b4d, 0x1132),      # Silhouette Portrait 2
  (0x0b4d, 0x1137)      # Silhouette Cameo 4

]

# def open_graphtec_device(ctx):
#   for (vendor_id,product_id) in device_list:
#     dev = ctx.openByVendorIDAndProductID(vendor_id, product_id)
#     if dev:
#       return dev
#   return None

#
# main program
#

dev = Graphtec.SilhouetteCameo()
dev.initialize()
dev.get_tool_setup()
dev.set_cutting_mat(1,279,216)

if len(sys.argv)==2:
  f = open(sys.argv[1], 'rb')
elif len(sys.argv)==1:
  f = sys.stdin
else:
  #print 'usage: file2graphtec [filename]'
  sys.exit(1)

# endpoint = 1
# ctx = usb1.USBContext()

# dev = open_graphtec_device(ctx)

# if not dev:
#   sys.stderr.write('no graphtec device found\n')
#   sys.exit(1)

# dev.claimInterface(0)
# print(hid.enumerate())
# dev = hid.Device(0x0b4d, 0x1137)

while True:
  data = f.read()
  if not data:
    break
  dev.safe_write(data)

f.close()
