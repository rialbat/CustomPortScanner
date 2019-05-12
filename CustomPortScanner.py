import nmap

def main():
        print('\033[32m ---------------------INPUT DATA---------------------')
        host = raw_input(' [*] Server ip: ')
        ports = raw_input(' [*] Ports: ')
        print(" ----------------------------------------------------\n")
        keys = '-T4 -oN output.txt'
        i = 0
        nm = nmap.PortScanner()
        print("\033[31m [*] Script is starting!\n [*] Please, wait...\033[32m")
        print(' [*] Script version is 1.0')
        nm.scan(host, ports, arguments=keys) # Checking all ports from ip
        print(" Info about scaning: \n Server ip: %s\n Ports range: %s\n Arguments: -oX %s\n" % (host, ports, keys))
        def check():
                if nm[host][proto][port]['name'] == '': 
                        nm[host][proto][port]['name'] = 'unknown service'
        for host in nm.all_hosts():
                print(' ----------------------------------------------------')
                print(' Host : %s (%s)' % (host, nm[host].hostname()))
                print(' State : %s' % nm[host].state())
                for proto in nm[host].all_protocols():
                        print(' ----------')
                        print(' Protocol : %s' % proto)
                        lport = nm[host][proto].keys()
                        lport.sort()
                for port in lport:
                        if nm[host][proto][port]['state'] == 'open':
                                i = i + 1
                                check()
                                print (' port : %s\tstate : %s\tinfo: %s' % (port, nm[host][proto][port]['state'], nm[host][proto][port]['name']))
                if i == 0:
                        print("\033[31m [*] No open ports!")
try:
        main()
except KeyboardInterrupt:
        print("\033[91m[*] Script has been stopped!")