# Only time will tell!
OSINT

## Challenge 

DESCRIPTION
This picture was taken sent to us! It seems like a bomb threat! Are you able to tell where and when this photo was taken? This will help the investigating officers to narrow down their search! All we can tell is that it's taken during the day!

If you think that it's 7.24pm in which the photo was taken. Please take the associated 2 hour block. This will be 1900-2100. If you think it is 10.11am, it will be 1000-1200.

Flag Example: govtech-csg{1.401146_103.927020_1990:12:30_2000-2200}
Use this calculator!
https://www.pgc.umn.edu/apps/convert/

Flag Format: govtech-csg{lat_long_date_[two hour block format]}

This challenge:
- Unlocks other challenge(s)
- Is eligible for Awesome Write-ups Award
- Prerequisite for Mastery Award - Intelligence Officer

Addendum:
- The amount of decimal places required is the same as shown in the example given.
- CLI tool to get something before you convert it with the calculator.

## Solution

Use exiftools

	GPS Latitude                    : 1 deg 17' 11.93" N
	GPS Longitude                   : 103 deg 50' 48.61" E
	GPS Position                    : 1 deg 17' 11.93" N, 103 deg 50' 48.61" 

The sun is in the west that's why the shadow is on the east, that means is somewhere from 1300-1700

## Flag

	govtech-csg{1.286647_103.846836_2020:10:25_1500-1700}
