import os
import getpass
import mytask
import mytask_remote

os.system("tput setaf 5")
os.system("clear")
print("\t\t<---------------YOUR WELCOME TO AUTOMATION MEMU PROGRAM----------------->\n\n")
passwd=getpass.getpass("\t\t\tEnter the automation program  password : ")
if passwd!="#arth" :
        os.system("tput setaf 1")
        print("\t\t\t\t\t incorrect password.....")
        exit()
os.system("tput setaf 2")
print("\n\t\t\t\t\t\t you have succesfully logged in !!!!!\n")
os.system("tput setaf 1")
print("""
                         \t\t******************************************************
                         \t\t\tMENU LIST OF PROGFRAM TO BE AUTOMATED
                         \t\t******************************************************

       """,end= "")
os.system("tput setaf 4")

print("""
                          \t\tPress 1: to setup all big-data hadoop technology
                          \t\tPress 2: to configure yum 
                          \t\tPress 3: to configure your system as a webserver
                          \t\tPress 4: to use lvm technology
                          \t\tPress 5: to setup docker technology  
                          \t\tPress 6: to setup  ansible tecnology  
                          \t\tPress 7: to setup  kubernetis technology
                          \t\tPress 8: to exit from automation program

                     """)
os.system("tput setaf 9")
ent=input("\n\t\t\t\tenter your choise from above : ")
os.system("tput setaf 3")
ws=input("\n\t\t\t\tenter your workspace --> (local / remote) : ")
os.system("tput setaf 9")

if ws=="local":
    if int(ent)==4:
          mytask.lvm()

elif ws=="remote":
    if int(ent)==4:
          ip=input("\n\t\t enter the ip-address of remote system :  ")
          mytask_remote.lvm_remote(ip)

elif int(ent)==8 :
    exit()

