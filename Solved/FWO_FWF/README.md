# FWO FWF
Misc

## Challenge 

As part of forensic investigations into servers operated by COViD, an investigator found this web server containing a hidden secret. Help us find the contents of this secret.

Web Server

## Solution

There are 3 classes in the html. `.a, .b, .c` and in the embedded CSS, only .c is being shown, the others are hidden.

Modify it and we can see some texts...

Show a, hide b and c to see this text
	
	The flag is hidden in a file

Show b, hide a and c to see this text

	CSG.TXT

Visit the webpage

- http://yhi8bpzolrog3yw17fe0wlwrnwllnhic.alttablabs.sg:40731/CSG.TXT

We get this

	Rmo0Y19HdTNfZkdsWTNfaTFmMW8xWTFHbAo=

Base64 decode

	Fj4c_Gu3_fGlY3_i1f1o1Y1Gl

ROT Ceaser Cipher (Use this online tool: https://planetcalc.com/1434/)

	ROT13	Sw4p_Th3_sTyL3_v1s1b1L1Ty

## Flag

	govtech-csg{Sw4p_Th3_sTyL3_v1s1b1L1Ty}
