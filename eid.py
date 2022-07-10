import os
from time import sleep
def c():
    os.system("cls")
def s():
    sleep(0.01)

def color(msg, color):
    black=f'\033[30m{msg}\033[0;0m'
    red=f'\033[31m{msg}\033[0;0m'
    green=f'\033[32m{msg}\033[0;0m'
    orange=f'\033[33m{msg}\033[0;0m'
    blue=f'\033[34m{msg}\033[0;0m'
    purple=f'\033[35m{msg}\033[0;0m'
    cyan=f'\033[36m{msg}\033[0;0m'
    lightgrey=f'\033[37m{msg}\033[0;0m'
    darkgrey=f'\033[90m{msg}\033[0;0m'
    lightred=f'\033[91m{msg}\033[0;0m'
    lightgreen=f'\033[92m{msg}\033[0;0m'
    yellow=f'\033[93m{msg}\033[0;0m'
    lightblue=f'\033[94m{msg}\033[0;0m'
    pink=f'\033[95m{msg}\033[0;0m'
    lightcyan=f'\033[96m{msg}\033[0;0m'
    toReturn = {
        'black'      : black,
        'red'        : red,
        'green'      : green,
        'orange'     : orange,
        'blue'       : blue,
        'cyan'       : cyan,
        'purple'     : purple,
        'lightgrey'  : lightgrey,
        'darkgrey'   : darkgrey,
        'lightred'   : lightred,
        'lightgreen' : lightgreen,
        'yellow'     : yellow,
        'lightblue'  :lightblue,
        'pink'       :pink,
        'lightcyan'  :lightcyan}
    return toReturn[color]


e = """
┌──┐_________
|  |_________│
|  |
|  |_________
|  |_________│
|  |
|  |_________
|  |_________│
└──┘
"""

i = """
┌────────────┐
└────┬──┬────┘
     |  |
     |  |
     |  |
     |  |
     |  |
     |  |
     |  |
     |  |
┌────┴──┴────┐
└────────────┘
"""

d = """
┌──────────╮
|          **
|            ** 
|              **
|              **
|              **
|            **
|          ** 
└──────────┘
"""

eid = ''
for o in e:
    eid = eid + o
    s()
    c()
    print(eid)

for o in i:
    eid = eid + o
    s()
    c()
    print(eid)

for o in d:
    eid = eid + o
    s()
    c()
    print(eid)

EID = eid.split("\n")
eid = ''
for o in EID:
    eid = eid + o + '\n'
    s()
    c()
    print(color(eid, 'blue'))


mubarak = """
||        ||   |          |     bbbbbbbbbbb            AAA         RRRRRRRRRRR       |        /
||\\\    //||   |          |     bb         bb         A   A        R         RRR     |       /
|| \\\  // ||   |          |     bb         bbb       A     A       R           RRR   |      /
||  \\\//  ||   |          |     bbbbbbbbbbbbb       A       A      R          RRR    ┣━━━━━━
||        ||   |          |     bb         bbb     AAAAAAAAAAA     RRRRRRRRRRR       |      \\
||        ||   |          |     bb         bb     A           A    R          R      |       \\
||        ||   └──────────┘     bBBBBBBBBBB      A             A   R           R     |        \\
                                                                   R            R    
"""
print(color(mubarak, 'pink'))