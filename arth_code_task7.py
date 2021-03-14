def lvm() :
        import os
        os.system("clear")
        from time import sleep
        os.system("tput setaf 4")
        os.system("\t\t\t\t figlet -kc LVM-MENU -f big")
 
        while True :
                os.system("tput setaf 1")
		
                print(""" 
			  \t\t\t-----------------------------
			  \t\t\t\tAVAILABLE MENUES
			  \t\t\t-----------------------------
		     """)
                os.system("tput setaf 2")		

                print(""" 
			  \t\t\tPress 0: to see the list of disk
		          \t\t\tPress 1: to create Physical Volume (PV)
		          \t\t\tPress 2: to create Volume Group (VG)
		          \t\t\tPress 3: to create Logical Volume (LV)
		          \t\t\tPress 4: to format Logical Volume (LV) partition
			  \t\t\tPress 5: to mount  Logical Volume (LV)
			  \t\t\tPress 6: to extend Volume Group (VG)
			  \t\t\tPress 7: to increase the size of Logical Volume (LV)
			  \t\t\tPress 8: to decrease the size of Logical Volume (LV)
                          \t\t\tPress 9: to display Volume Group (VG)
                          \t\t\tPress 10: to display Logical Volume (LV)
                          \t\t\tPress 11: to see all mounted drive/folder
                          \t\t\tPress 12: to exit from menu program
			  
		     """)
                os.system("tput setaf 3")
                ent=input("\n\t\t\t\tenter your choise from above: ")
                os.system("tput setaf 9")

                if int(ent)==0 :
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#displaying all the disk........",end="\n\n\n")
                        os.system("tput setaf 9")
                       	os.system("lsblk")
                        print("\n")
                        print("-"*118)

				
		
                elif int(ent)==1 :
                        os.system("tput setaf 3")
                        pv=input("\n\t\t\t\tenter your PV/disk name: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#creating PV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("pvcreate /dev/{}".format(pv))
                        print("\n")
                        print("-"*118)
		
                elif int(ent)==2 :
                        os.system("tput setaf 3")
                        vg=input("\n\t\t\t\tenter your VG name: ")
                        pv=input("\n\t\t\t\tenter your PV name: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#creating VG........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("vgcreate {} /dev/{} ".format(vg,pv))
                        print("\n")
                        print("-"*118)

                elif int(ent)==3 :
                        os.system("tput setaf 3")
                        lvm=input("\n\t\t\t\tenter your LV name: ")
                        vg=input("\n\t\t\t\tenter vg name: ")
                        ls=input("\n\t\t\t\tenter size in G of LV that you want : ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#creating LV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("lvcreate --size {} --name {} {}".format(ls,lvm,vg))
                        print("\n")
                        print("-"*118)

                elif int(ent)==4 :
                        os.system("tput setaf 3")
                        path=input("\n\t\t\t\tenter your LV path: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#formatting the LV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("mkfs.ext4 {}".format(path))
                        print("\n")
                        print("-"*118)

                elif int(ent)==5 :
                        os.system("tput setaf 3")
                        mf=input("\n\t\t\t\tenter the folder name to mount: ")
                        path=input("\n\t\t\t\tenter the path of your LV: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#mounting the LV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("mkdir {}".format(mf))
                        os.system("mount {} {}".format(path,mf))
                        print("\n")
                        print("-"*118)

                elif int(ent)==6 :
                        os.system("tput setaf 3")
                        vg=input("\n\t\t\t\tenter the name of VG: ")
                        pv=input("\n\t\t\t\tenter the PV name: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#extending the size of VG........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("vgextend {} /dev/{}".format(vg,pv))
                        print("\n")
                        print("-"*118)

                elif int(ent)==7 :
                        os.system("tput setaf 3")
                        path=input("\n\t\t\t\tenter the path of LV: ")
                        ls=input("\n\t\t\t\tenter the size that you want to increase: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#increasing the size of LV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("\nlvextend --size +{}  {}".format(ls,path))
                        os.system("\nresize2fs {}".format(path))
                        print("\n")
                        print("-"*118)

                elif int(ent)==8 :
                        os.system("tput setaf 3")
                        path=input("\n\t\t\t\tenter the path of LV: ")
                        ls=input("\n\t\t\t\tenter the size of LV that you want to remain: ")
                        mf=input("\n\t\t\t\tenter the mount point: ")
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#reducing the size of LV........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("umount {} -y".format(mf))
                        os.system("e2fsck -f {} -y".format(path))
                        os.system("resize2fs {} {} -y".format(path,ls))
                        os.system("lvreduce --size {}  {} -y".format(ls,path))
                        os.system("mount {} {}".format(path,mf))
                        print("\n")
                        print("-"*118)

                elif int(ent)==9 :
                        os.system("tput setaf 4")
                        print("""
                        \t\t\tPress 1: to display all VG
                        \t\t\tPress 2: to display specific VG
                              """)
                        os.system("tput setaf 6")
                        ch=input("\n\t\t\t\tenter your choise from above: ")
                        if int(ch)==1 :
                            print("\n")
                            os.system("tput setaf 4")
                            print("\t#displaying all the VG........",end="\n\n\n")
                            os.system("tput setaf 9")
                            os.system("vgdisplay")
                        if int(ch)==2 :
                            vg=input("\n\t\t\t\tenter the VG name: ")
                            print("\n")
                            os.system("tput setaf 4")
                            print("\t#displaying specific VG........",end="\n\n\n")
                            os.system("tput setaf 9")
                            os.system("vgdisplay {}".format(vg))
                        print("\n")
                        print("-"*118)
 
                elif int(ent)==10 :
                         os.system("tput setaf 4")
                         print("""
                        \t\t\tPress 1: to display all LV
                        \t\t\tPress 2: to display specific LV
                              """)
                         os.system("tput setaf 6")
                         ch=input("\n\t\t\t\tenter your choise from above: ")
                         if int(ch)==1:
                             print("\n")
                             os.system("tput setaf 4")
                             print("\t#displaying all the LV........",end="\n\n\n")
                             os.system("tput setaf 9")
                             os.system("lvdisplay")
                         elif int(ch)==2:
                             vg=input("\n\t\t\t\tenter the VG name: ")
                             print("\n")
                             os.system("tput setaf 4")
                             print("\t#displaying specific LV.......",end="\n\n\n")
                             os.system("tput setaf 9")
                             os.system("lvdisplay {}".format(vg))
                         print("\n")
                         print("-"*118)
                             
                elif int(ent)==11 :
                        print("\n")
                        os.system("tput setaf 4")
                        print("\t#displaying all the mounted disk........",end="\n\n\n")
                        os.system("tput setaf 9")
                        os.system("df -hT")
                        print("\n")
                        print("-"*118)
 
                elif int(ent)==12 :
                        os.system("tput setaf 4")
                        print("\n\t\t\tthanks for using this menu program !!!\n")
                        os.system("tput setaf 9")
                        exit()


                else :
                        os.system("tput setaf 1")
                        print("\n\t\t\t\tpls enter valid choise....")


                os.system("tput setaf 5")
                cn=input("\n\t\t\t\tDo you want to continue (y/n): ")
                os.system("tput setaf 9")
                if ("n" in cn) :
                        os.system("tput setaf 4")
                        print("\n\t\t\tthanks for using this menu program !!!\n")
                        os.system("tput setaf 9")
                        exit()
						
	
		
		
	
