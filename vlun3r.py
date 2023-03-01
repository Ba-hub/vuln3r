import argparse
import os
import sys
import time
import colorama
import subprocess as sp
import requests
from os import system
from time import sleep 
from colorama import Fore
from alive_progress import alive_bar

isgit = sp.getoutput('which git')
if os.path.isfile(isgit):
    print("")
else:
    print(Fore.RED + 'Git Not Found Install Git & Run Again [!]')
    sys.exit()

isnmap = sp.getoutput('which nmap')
if os.path.isfile(isnmap):
    print("")
else:
    print(Fore.RED + 'Nmap Not Found Install Nmap & Run Again [!]')
    sys.exit()
    
banner = (Fore.RED + """
                                                                        
                    .     /                                                     
                   .     ,,                            *     ,                  
                   (                                    (                       
                  ,     (&                              *(    %%                
                 %%    *,,                              (#                      
                 //    &                                /@*    @#               
                @.     &#%@%@@@@&@%  %     /.  %&&&@@@&@#(@    /,%              
                ..      #         @*@@#(@%.@@,@         &      &*@              
               @           /&/(&@&./         *,(&@%/(%         ( *,             
                 %(&/,%@*         #,         *%%         #@%,((%@               
                           /%.%@#  #(        ,/ *@&%/%                          
                         &(%#   .(%/ #     .# %,%    @((%                       
                      @(%#   @*,&  (#       /#   @*,(   @#/#                    
                  /#,@       . ,&   #@      //   , ,&      %%(%                 
              #@#%,          & #     @     @&    & /           @&@@             
                #.           @&%     @*    @      #,            @@*             
               (#.           &((      %@  (/      %#            @@@             
               @#.           &%        %@/%       @&/           #&(             
               *%.           &&                   .%&           /@              
                @(           &%                    %#           (&              
                ,*           &%                    &,           (               
                 %           &%                    %           #                
                  *          (#                    #           %                
                   *          (                    &          (                 
                    ,         /,                  /          ,                  
                               /                 (                              
                                 ,              #                               
                                    

""")    
    
print(banner)
print(Fore.YELLOW + '')
parser = argparse.ArgumentParser(description='Easy Vulnerability Detection & Hints With CVE Number For Exploitation.\n Made By Ghosthub')
parser.add_argument('-u','--url', help='Input URL/IP [https://example.com] Or [IP Address]',required=True)
parser.add_argument('-o','--output',help='Output file name [results.txt]',required=True)
args = parser.parse_args()

url = args.url

def progressBar():
    with alive_bar(100) as bar:
        for i in range(100):
            sleep(1)
            bar()

def checkElement(url):
    if url.startswith("https://"):
        return url[8:]
    elif url.startswith("http://"):
        return url[7:]
    elif url.startswith("www."):
        return url[4:]
    else:
        return url

def CheckPath():
    nurl = checkElement(url)
    if os.path.exists('/usr/share/nmap/scripts/vulscan'):
        cmd = "nmap -sV --script=vulscan/vulscan.nse " + nurl
        vuln = sp.check_output(cmd, shell=True, stderr=sp.STDOUT).decode().strip()
        print(Fore.YELLOW + '[+] Please Wait.. Saveing Data into ' + args.output)
        with open(f'{args.output}', "w") as f:
            f.write(vuln)    
    else:
        check = sp.getoutput('git clone https://github.com/scipag/vulscan scipag_vulscan')
        link = sp.getoutput('mv `pwd`/scipag_vulscan vulscan')
        link_mv = sp.getoutput('mv `pwd`/vulscan $PREFIX/usr/share/nmap/scripts/vulscan')
        cmd = "nmap -sV --script=vulscan/vulscan.nse " + nurl
        vuln = sp.check_output(cmd, shell=True, stderr=sp.STDOUT).decode().strip()
        print(Fore.YELLOW + '[+] Please Wait.. Saveing Data into ~ ' + args.output)
        with open(f'{args.output}', "w") as f:
            f.write(vuln)
   
try:
    response = requests.get(args.url)
    print(Fore.WHITE + '[!] Finding Vulnerability to ~ ' + args.url) 
    CheckPath()
    print(Fore.GREEN + '')
    progressBar()
    print(Fore.BLUE + '[~] Process Complete, File saved in ~ ' + args.output)
except requests.ConnectionError as exception:
    print(Fore.RED +  args.url + 'Does Not Exits')
    sys.exit()  s