
with open("time.csv") as f:
	contents = f.readlines()

contents = contents[1:]

lines = len(contents)

payload = ""
prev_time = 8.28
for i in range(lines):
	line = contents[i]

	current_time = float(line.split(',')[0])
	timedelta = current_time - prev_time
	prev_time = current_time

	#if (1.6e-3 < timedelta < 1.7e-3):

	timedelta_msec = timedelta * 1000

	if (timedelta_msec < 0.1):
		# ignore modulation
		pass

	else:
		if (4.3 < timedelta_msec < 4.7):
			# burst start of
			payload += '-'
		elif (1.5 < timedelta_msec < 1.9):
			# high
			payload += '1'
		elif (0.35 < timedelta_msec < 0.65):
			# low
			payload += '0'
		elif (980 < timedelta_msec < 1100):
			# space
			payload += '\n'
		else:
			payload += '0\n'

		print("%.2f" % timedelta_msec)

print("payload", payload)

flag = b''
for line in payload.splitlines():
	ascii_numb = int(line[-16:], 2)

	if (ascii_numb):
		hex_str = hex(ascii_numb)[2:]
		byte_str = bytes.fromhex(hex_str)
		print(line[-16:], hex_str, byte_str)
		flag += byte_str

print(flag)
