import random
import sys
import os
import shutil
import xml.etree.ElementTree as ET

playlist = raw_input('Enter playlist destination: \n')
tree = ET.parse(playlist)
root = tree.getroot()

dest = raw_input('Enter files destination:\n')
for item in root.iter('{http://xspf.org/ns/0/}location'):
    srcf = item.text[7:]
    shutil.copy2(srcf, dest)
