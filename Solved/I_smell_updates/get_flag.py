#!/usr/bin/env python3

def magic4(param_1):
    local_c = 0;
    local_11 = param_1;
    while (local_c < 3):
        local_c = local_c + 1;
        local_11 = local_11 - 1;
    return 0xff & local_11


def sum(param_1,param_2):
    result = (0xff & param_1) - ((0xff & param_1) + param_2);
    return result & 0xff;

def magic3(param_1):
    bVar1 = magic4(0xff & param_1);
    cVar2 = sum(0xff & bVar1,1);
    return 0xff & (bVar1 - cVar2)


def mod(param_1):
    if param_1 == 0:
        return 0x42;
    else:
        return 1;

def magic2(param_1):
    bVar1 = magic3(0xff & param_1);
    cVar2 = mod(0xff & bVar1);
    return 0xff&(cVar2 + bVar1);


def min(param_1, param_2):
    if (param_2 < param_1):
        param_1 = param_1 - param_2;
    else:
        param_1 = (param_2 - (param_2 >> 0x1f) & 1) + (param_2 >> 0x1f) + 1;
    return param_1 & 0xff;

def magic(param_1):
    cVar1 = magic2(0xff & param_1);
    cVar2 = min(3,2);
    return 0xff & (cVar2 + cVar1);

input = [0] * 8

input[0] = magic(0x69 - 8)
input[1] = magic(0x27 ^ 0x69)
input[2] = magic(0x0b + 0x69)
input[3] = magic((input[1] & 0x7f) * 2 - 0x33)
input[4] = magic(0x42)
count = 5
input[5] = magic((count-1)*8 & 0xff | 1)

local_17 = ((input[4] + input[5] + input[3]) ^ input[3] + input[5] + 0x42) + 0x65;
input[6] = magic(local_17)

print(''.join(map(chr, input)))