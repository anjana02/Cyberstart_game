```
~/ctf/cyberstart/level11/11 [master|✚ 8…9] $ nmap services.cyberprotection.agency -p 14000-15000 -sV -Pn
Starting Nmap 7.80 ( https://nmap.org ) at 2021-03-11 17:54 EST
Stats: 0:00:57 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 27.97% done; ETC: 17:58 (0:02:27 remaining)
Stats: 0:00:59 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 28.97% done; ETC: 17:58 (0:02:25 remaining)
Stats: 0:02:02 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 60.44% done; ETC: 17:58 (0:01:20 remaining)
Nmap scan report for services.cyberprotection.agency (3.249.74.244)
Host is up (0.13s latency).
rDNS record for 3.249.74.244: ec2-3-249-74-244.eu-west-1.compute.amazonaws.com
Not shown: 1000 filtered ports
PORT      STATE SERVICE VERSION
14444/tcp open  unknown
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port14444-TCP:V=7.80%I=7%D=3/11%Time=604AA049%P=x86_64-pc-linux-gnu%r(N
SF:ULL,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S\n")%r(HTTPOptions,1E,"\nFLAG:
SF:\x20Dc4GChlyxd3jkTmapRcQ0S\n")%r(RPCCheck,1E,"\nFLAG:\x20Dc4GChlyxd3jkT
SF:mapRcQ0S\n")%r(Kerberos,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S\n")%r(Fou
SF:rOhFourRequest,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S\n")%r(LDAPSearchRe
SF:q,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S\n")%r(WMSRequest,1E,"\nFLAG:\x2
SF:0Dc4GChlyxd3jkTmapRcQ0S\n")%r(afp,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S
SF:\n")%r(giop,1E,"\nFLAG:\x20Dc4GChlyxd3jkTmapRcQ0S\n");

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 153.81 seconds
~/ctf/cyberstart/level11/11 [master|✚ 8…9] $ telnet services.cyberprotection.agency 14444
Trying 3.249.74.244...
Connected to ec2-3-249-74-244.eu-west-1.compute.amazonaws.com.
Escape character is '^]'.

FLAG: Dc4GChlyxd3jkTmapRcQ0S
Connection closed by foreign host.
```
