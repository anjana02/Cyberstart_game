#!/usr/bin/env python3
import requests
import sys
import re
from tqdm import tqdm
import base64


def csrf():
    response = requests.get(
        "https://game.joincyberstart.com/base-headquarters",
        cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"},
    )
    matches = re.search(r'csrf=(.*?)"', response.text)
    csrf_base = matches.group(1)
    return csrf_base


session = requests.Session()


def run():
    challenge_url = f"https://game.joincyberstart.com/challenge?base=1&level=13&challenge=1&csrf={csrf()}"
    response = session.get(
        challenge_url, cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"}
    ).text
    reg = re.compile(r'<div class="line">([\s\S]*?)<\/div>')
    strings = re.findall(reg, response)
    with open("out32.txt", "ab") as f:
        for s in strings:
            # print(s)
            s = base64.b64decode(s).decode("utf-8")
            # print(s)
            match = re.search(r"[0-9a-fA-F]{10}", s)
            if match:
                session.post(
                    challenge_url,
                    cookies={"Cyber_Protection_Agency": "0vu34oap0bukiokhl5p4dr1orc"},
                    data={""},
                )


run()