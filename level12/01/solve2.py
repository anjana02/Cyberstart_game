from pwn import remote
from timeit import default_timer


conn = remote("services.cyberprotection.agency", 9999)
t = default_timer()

l = list(map(lambda x: int(x), conn.recv(18).strip().split(b"\n")))
solution = int(l[0] * l[1] / l[2])
conn.sendline(str(solution))
t2 = default_timer() - t
print("Too slow by ", round(t2 - 0.1, 4), "seconds")
conn.recv(128, timeout=1)
