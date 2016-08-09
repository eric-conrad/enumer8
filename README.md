# enumer8
User enumeration scripts for penetration testers

## enumer8-ssh.py:

Reads a list of potential usernames and tests an openssh server for the CVE-2016-6210 opensshd timing attack bug. Based on Eddie Harari's opensshd user enumeration POC.

Can append popular first initials to last names and loop accordingly. 

## pfi.pl (Popular First Initials):

Ranks first initials in order of popularity, per the 1990 US Census. Useful as an input to enumer8-ssh.py.
