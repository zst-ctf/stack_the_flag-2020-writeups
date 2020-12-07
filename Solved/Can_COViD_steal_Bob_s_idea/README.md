# Can COViD steal Bob's idea?
Crypto

## Challenge

Bob wants Alice to help him design the stream cipher's keystream generator base on his rough idea. Can COViD steal Bob's "protected" idea?

## Solution

From the wireshark, you can extracted this conversation from the TCP payload

	p =   298161833288328455288826827978944092433
	g =   216590906870332474191827756801961881648
	g^a = 181553548982634226931709548695881171814
	g^b = 64889049934231151703132324484506000958

	Hi Alice, could you please help me to design a keystream generator according to the file I share in the file server so that I can use it to encrypt my 500-bytes secret message? Please make sure it run with maximum period without repeating the keystream. The password to protect the file is our shared Diffie-Hellman key in digits. Thanks.

Also from Wireshark, Follow TCP packets to extract the zip files

[tcp.zip](tcp.zip)

The attack is using Discrete Log to calculate the exponent. The Pohlig-Hellman algorithm for calculation must be used.

This is similar to some other CTF challenges. Relevant writeups:

- https://ctftime.org/writeup/12240
- https://github.com/asmitahajra/CTF/blob/master/SEC-T/Marty0ska1

There exists an online tool which makes it very convenient.

- https://www.alpertron.com.ar/DILOG.HTM

I get these results.

	a = 211631375588570729261040810141700746731
	b = 164628728413072046550711086534226032119

Here, I used python3 console to confirm the public keys g^a, g^b

	>>> p =   298161833288328455288826827978944092433
	>>> g =   216590906870332474191827756801961881648
	>>> a = 211631375588570729261040810141700746731
	>>> b = 164628728413072046550711086534226032119

	>>> pow(g,a,p)
	181553548982634226931709548695881171814

	>>> pow(g,b,p)
	64889049934231151703132324484506000958

And also calculate the shared key, g^(ab)

	>>> pow(g,a*b, p)
	246544130863363089867058587807471986686

Alternatively, I coded a script in Sage to solve it too.

	$ time sage test_discrete_log.sage 
	
	Private Key A: 211631375588570729261040810141700746731
	Private Key B: 164628728413072046550711086534226032119
	Shared Key: 246544130863363089867058587807471986686

	real	0m9.203s
	user	0m8.632s
	sys	0m0.557s

Now we can successfully extract the zip file

with the password `246544130863363089867058587807471986686`

## Flag

	govtech-csg{246544130863363089867058587807471986686}
