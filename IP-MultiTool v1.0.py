import socket
import os
import requests
import platform

class bcolors:
    RED = '\033[91m'
    YELLOW ='\033[93m'
    BLUE ='\033[96m'
    TEZ ='\033[95m'

def back():
    print()
    back = input('\033[92mDo You Want To Continue? [Yes/No]: ')
    if back[0].upper() == 'Y':
        print()
        iseeverything()
    elif back[0].upper() == 'N':
        print('\033[92mRemember https://GitHackTools.blogspot.com')
        exit
    else:
        print('\033[92m?')
        exit


def clear():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print(bcolors.TEZ + '            ==================================================')
    print(bcolors.YELLOW + '            ~~~~~~~~~~~~~[DynamicSecurityServices]~~~~~~~~~~~~')
    print(bcolors.TEZ + '            ==================================================')


def bill():
    clear()

    print(bcolors.BLUE + """            ==================================================             """)
    print(bcolors.YELLOW + "                  \>- DynamicSec | IP-MultiTool v1.0 -</""")
    print("                    \>- https://discord.gg/vQdd6za -</""")
    print("                     \>- Instagram = CodingUrLife -</")
    print("                      \>- Coded By: CodingUrLife -</")
    print(bcolors.BLUE + "            ==================================================")
    print(bcolors.TEZ + "            ==================================================")
    print(bcolors.YELLOW + '            ~~~~~~~~~~~~~~[YouTube = DynamicSec]~~~~~~~~~~~~~~')
    print(bcolors.TEZ + "            ==================================================")
    print(" ")



def banner():
    print("""\033[96m
  1) DNS Lookup                 13) Host DNS Finder
  2) Whois Lookup               14) Reserve IP Lookup
  3) GeoIP Lookup               15) Email Gathering 
  4) Subnet Lookup              16) Subdomain Scanner 
  5) Port Scanner               17) Find Admin Login Site 
  6) Page Links                 18) Check & Bypass CloudFlare 
  7) Zone Transfer              19) Website Copier 
  8) HTTP Header                20) Host Info Scanner 
  9) Host Finder                21) About IP-Multitool v1.0
 10) IP-Locator                 22) (Exit)
 11) Find Shared DNS Servers
 12) Get Robots.txt""")
    print(" ")


def iseeverything():
    try:
        what = input('\033[92m Select What Type Of Target You Want To Scan [Website/IP]: ')
        if what[0].upper() == 'W':
            victim = input(' Enter The Target Website: ')
            print(bcolors.RED + ' Launching IP-MultiTool v1.0...')
            banner()
        elif what[0].upper() == 'I':
            victim = input(' Enter The Target IP Address: ')
            print(" ")

            print(bcolors.RED + '   [][][]>- Launching: IP-MultiTool v1.0 -<[][][]')
            victim = socket.gethostbyname(victim)
            print(bcolors.RED + '       [][][]>- Initializing Program -<[][][]')
            print(bcolors.RED + '   [][][]>- Program Successfully Started -<[][][]')
            print(bcolors.RED + '    [][][]>- Starting IP-Multitool v1.0 -<[][][]')


            banner()
            print(" ===================================================")
            print(" ~~~~~~~~~~~~~~~[Coded In Python3.8]~~~~~~~~~~~~~~~~")
            print(" ===================================================")
            print(" ")
        else:
            print('?')
            iseeverything()

        choose = input(' Select What Program You Would Like To Use - (1-20): ')

        if choose == '1':
            dnslook = 'https://api.hackertarget.com/dnslookup/?q=' + victim
            info = requests.get(dnslook)
            print('\033[91m', info.text)
            back()

        elif choose == '2':
            whois = 'https://api.hackertarget.com/whois/?q=' + victim
            info = requests.get(whois)
            print('\033[91m', info.text)
            back()

        elif choose == '3':
            ipgeo = 'https://api.hackertarget.com/geoip/?q=' + victim
            info = requests.get(ipgeo)
            print('\033[91m', info.text)
            back()

        elif choose == '4':
            subnet = 'http://api.hackertarget.com/subnetcalc/?q=' + victim
            info = requests.get(subnet)
            print('\033[91m', info.text)
            back()

        elif choose == '5':
            port = 'https://api.hackertarget.com/nmap/?q=' + victim
            info = requests.get(port)
            print('\033[91m', info.text)
            back()

        elif choose == '6':
            pagelink = 'https://api.hackertarget.com/pagelinks/?q=' + victim
            info = requests.get(pagelink)
            print('\033[91m', info.text)
            back()

        elif choose == '7':
            zone = 'https://api.hackertarget.com/zonetransfer/?q=' + victim
            info = requests.get(zone)
            print('\033[91m', info.text)
            back()

        elif choose == '8':
            header = 'https://api.hackertarget.com/httpheaders/?q=' + victim
            info = requests.get(header)
            print('\033[91m', info.text)
            back()

        elif choose == '9':
            host = 'https://api.hackertarget.com/hostsearch/?q=' + victim
            info = requests.get(host)
            print('\033[91m', info.text)
            back()

        elif choose == '10':
            iplt = 'https://ipinfo.io/' + victim + '/json'
            info = requests.get(iplt)
            print('\033[91m', info.text)
            back()

        elif choose == '11':
            shared = 'https://api.hackertarget.com/findshareddns/?q=' + victim
            info = requests.get(shared)
            print('\033[91m', info.text)
            back()

        elif choose == '12':
            robots = 'http://' + victim + '/robots.txt'
            info = requests.get(robots)
            print('\033[91m', info.text)
            back()

        elif choose == '13':
            hostdns = 'https://api.hackertarget.com/mtr/?q=' + victim
            info = requests.get(hostdns)
            print('\033[91m', info.text)
            back()

        elif choose == '14':
            reserve = 'https://api.hackertarget.com/reverseiplookup/?q=' + victim
            info = requests.get(reserve)
            print('\033[91m', info.text)
            back()

        elif choose == '15':
            clear()
            os.system('cd modules/Infoga && python3 infoga.py --domain ' + victim)
            back()

        elif choose == '16':
            clear()
            os.system('cd modules/Sublist3r && python3 sublist3r.py -d ' + victim)
            back()

        elif choose == '17':
            clear()
            os.system('cd modules/Breacher && python breacher.py -u ' + victim)
            back()

        elif choose == '18':
            clear()
            os.system('ruby ./modules/HatCloud/hatcloud.rb -b ' + victim)
            back()

        elif choose == '19':
            os.system('cd websource && mkdir ' + victim)
            os.system('cd websource && cd ' + victim + ' && httrack ' + victim)
            print(bcolors.RED + "The Website Source Code Was Saved In A Folder 'websource'")
            print(bcolors.RED + ' Developer = CodingUrLife | IF Your Having Issues Then Contact The "DEV" ')
            print(bcolors.RED + ' Coded In Python3.8.3 :)')
            print(bcolors.RED + " Instagram = codingurlife")
            back()

        elif choose == '20':
            clear()
            os.system('whatweb -v ' + victim)
            back()

        elif choose == '21':
            print("""\033[93m DynamicSec | IP-MultiTool v1.0 - Information Gathering Of A Website Or IP Address""")
            back()

        elif choose == '22':
            exit

        else:
            print('?')
            iseeverything()

    except socket.gaierror:
        print('Name Or Service Invalid!\033[93m')
        print()
        iseeverything()
    except UnboundLocalError:
        print('The Information You Entered Was Incorrect')
        print()
        iseeverything()
    except requests.exceptions.ConnectionError:
        print('Your Internet Is Offline')
        exit
    except IndexError:
        print('?')
        print()
        iseeverything()


bill()
iseeverything()