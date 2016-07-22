# Database-Python-scripting
#Adds,Updates,displays,Associates users to respective HVDs

import os
import MySQLdb
import random
import optparse

class User():
        def Insert(self,Fname,Email,Address,Phoneno,Age):
                self.Fname = Fname
                self.Email = Email
                self.Address = Address
                self.Phoneno = Phoneno
                self.Age = Age
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()              
                curr.execute("""INSERT INTO hvduser(Fname,Email,Address,Phoneno,Age) VALUES ('%s','%s','%s',%s,%s)""" %(Fname,Email,Address,Phoneno,Age))
                db.commit()
                print("Information Added")
                curr.execute("""SELECT * FROM hvduser;""")
                print curr.fetchall()
                ((Fname,Email,Address,Phoneno,Age),)
                return("%s,%s,%s,%s,%s") % (Fname,Email,Address,Phoneno,Age)

        def Delete(self,idhvduser):
                self.idhvduser=idhvduser
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute(("""DELETE FROM hvduser WHERE idhvduser = %d;""") % (idhvduser))
                db.commit()  
                print("Information Deleted")
                curr.execute("""SELECT * FROM hvduser;""")
                return("%d") % (idhvduser)
                

        def Update(self,newFname,newEmail,newAddress,newPhoneno,newAge,idhvduser):
                self.newFname=newFname
                self.newEmail=newEmail
                self.newAddress=newAddress
                self.newPhoneno=newPhoneno
                self.newAge=newAge
                self.idhvduser=idhvduser
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute(("""SELECT idhvduser FROM hvduser WHERE idhvduser = %d;""") % (idhvduser))
                curr.execute(("UPDATE hvduser SET Fname ='%s',Email ='%s',Address ='%s',Phoneno=%d,Age=%d WHERE idhvduser = %d;" % (newFname,newEmail,newAddress,newPhoneno,newAge,idhvduser)))
                db.commit()
                print("Information Updated")
                curr.execute("""SELECT * FROM hvduser;""")
                print curr.fetchall()
                ((idhvduser,newFname,newEmail,newAddress,newPhoneno,newAge),)
                return("%s,%s,%s,%d,%d,%d") % (newFname,newEmail,newAddress,newPhoneno,newAge,idhvduser)
             

        def Display(self):
                print("Listing all the users of Database")
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""SELECT * FROM hvduser;""")
                print curr.fetchall()
                return;

        def AddRecordHVD(self,FName,CPU,DiskFb,GivenDate):
                self.FName=FName
                self.CPU=CPU
                self.DiskFb=DiskFb
                self.GivenDate=GivenDate
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""INSERT INTO hvdinfo(FName,CPU,DiskFb,GivenDate) VALUES ('%s','%s','%s',%s)""" %(FName,CPU,DiskFb,GivenDate))
                db.commit()
                curr.execute("SELECT * FROM hvdinfo;")
                print curr.fetchall()
                ((FName,CPU,DiskFb,GivenDate),)
                return("%s,%s,%s,%s") % (FName,CPU,DiskFb,GivenDate)
                

        def bool():
                    v = raw_input("Enter the status of HVD")
                    if v.lower():
                            print("status is on")
                    else:
                            print("Status is off")
                    return v.lower() in ("Yes","true","t","1")

        def DeleteHVDRecords():
                self.idhvdinfo=idhvdinfo
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute(("""DELETE FROM hvduser WHERE idhvdinfo = %d;""") % (idhvdinfo))
                db.commit()  
                print("Record Deleted")
                curr.execute("""SELECT * FROM hvdinfo;""")
                return("%d") % (idhvdinfo)
                

        def UpdateHVDRecord(self,newFName,newCPU,newDiskFb,newGivenDate,idhvdinfo):
                self.newFName=newFName
                self.newCPU=newCPU
                self.newDiskFb=newDiskFb
                self.newGivenDate=newGivenDate
                self.idhvdinfo=idhvdinfo
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute(("""SELECT idhvdinfo FROM hvdinfo WHERE idhvdinfo = %d;""") % (idhvdinfo))
                curr.execute(("UPDATE hvdinfo SET FName ='%s',CPU ='%s',DiskFb ='%s',GivenDate=%d WHERE idhvdinfo = %d;" % (newFName,newCPU,newDiskFb,newGivenDate,idhvdinfo)))
                db.commit()
                print("Record Updated")
                curr.execute("""SELECT * FROM hvdinfo;""")
                print curr.fetchall()
                ((idhvdinfo,newFName,newCPU,newDiskFb,newGivenDate),)
                return("%s,%s,%s,%d,%d") % (newFName,newCPU,newDiskFb,newGivenDate,idhvdinfo)
                

        def HVDRecordsUsers(self,idhvduser):
                self.idhvduser=idhvduser
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute(("""SELECT idhvduser FROM hvduser WHERE idhvduser = %d""") % (idhvduser))
                curr.execute("""SELECT hvduser.Fname,hvdinfo.CPU,hvdinfo.DiskFb,hvdinfo.GivenDate,hvduser.idhvduser,hvdinfo.idhvdinfo FROM hvduser INNER JOIN hvdinfo ON hvduser.idhvduser = hvdinfo.idhvdinfo;""")
                db.commit()
                curr.execute("""SELECT hvduser.Fname,hvdinfo.CPU,hvdinfo.DiskFB,hvdinfo.GivenDate FROM hvduser,hvdinfo WHERE idhvduser = idhvdinfo;""")
                print curr.fetchall()
                return;
                

        def HVDNRecordsUsers():
                print('Displaying all the records notassociated to users')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""SELECT FName,CPU,DISKfb,GivenDate FROM hvdinfo;""")
                return;

def Main():
                parser = optparse.OptionParser(('usage %prog :'+\
                        "-n=Fname,-e=Email,-a=Address,--p=Phoneno,-g=Age,--cp=CPU,-f=DiskFb,-t=GivenDate,-c=idhvduser--i=Insert,-d=Delete,-u=Upgrade,--ih=AddRecordHVD,-b=bool,--dh=DeleteHVDRecords,--uh=UpdateHVDRecord,--rh=RecordsHVDUsers,--nh=NRecordsHVDUsers"))
                parser.add_option('-n',action='store',dest='Fname',type=str,help='Enter user name')
                parser.add_option('-e',action='store',dest='Email',type=str,help='Enter user email')
                parser.add_option('-a',action='store',dest='Address',type=str,help='Enter user address')
                parser.add_option('--p',action='store',dest='Phoneno',type=int,help='Enter user phoneno')
                parser.add_option('-g',action='store',dest='Age',type=int,help='Enter user age')
                parser.add_option('--nn',action='store',dest='FName',type=str,help='Enter hvd first name')
                parser.add_option('--cp',action='store',dest='CPU',type=str,help="Enter your CPU")
                parser.add_option('-f',action='store',dest='DiskFb',type=str,help="Enter your Diskfb")
                parser.add_option('-t',action='store',dest='GivenDate',type=int,help="Enter the given date")
                parser.add_option('-c',action='store',dest='idhvduser',type=int,help='Enter id number for delete or update')
                parser.add_option('-z',action='store',dest='idhvdinfo',type=int,help='Enter the id number of HVD record')
                parser.add_option('--i',action='store',dest='Insert',help='To Insert your user Information')
                parser.add_option('-d',action='append',dest='Delete',help="To delete your user Information")
                parser.add_option('-u',action='store',dest='Update',help="To update your user information")
                parser.add_option('--ih',action='store',dest='AddRecordHVD',help='To Enter HVD Record')
                parser.add_option('-b',action='store_true',dest='bool',default=False,help='Enter the HVD status')
                parser.add_option('--dh',dest='DeleteHVDRecords',help='To Delete your HVD record')
                parser.add_option('--uh',action='store',dest='UpdateHVDRecord',help='Update your HVD Record')
                parser.add_option('--rh',dest='HVDRecordsUsers',help='Displays Records associated to Users')
                parser.add_option('--nh',dest='HVDNRecordsUsers',help='Displays Records not associated to Users')
                parser.add_option('--du',action='append',dest='Display',help='Displays user information')
                (options, args) = parser.parse_args()
                if(options.Insert):
                        Fname = options.Fname
                        Email = options.Email
                        Address = options.Address
                        Phoneno = options.Phoneno
                        Age = options.Age
                        if (options.Fname == Fname and options.Email == Email and options.Address == Address and options.Phoneno == Phoneno and options.Age == Age):
                                obj = User()
                                obj.Insert(Fname,Email,Address,Phoneno,Age)
                                print("Information added")
                        else: 
                                print('please specify all required arguments')
                                exit(-1)
                elif(options.Delete):
                        idhvduser=options.idhvduser
                        if(options.idhvduser == idhvduser):
                                obj = User()
                                obj.Delete(idhvduser)
                        else:
                                print("Specify required id")
                                exit(-1)
                elif(options.Update):
                        Fname = options.Fname
                        Email = options.Email
                        Address = options.Address
                        Phoneno = options.Phoneno
                        Age = options.Age
                        idhvduser = options.idhvduser
                        if(options.idhvduser == idhvduser):
                                obj = User()
                                obj.Update(Fname,Email,Address,Phoneno,Age,idhvduser)
                                print("Updated")
                        else:
                                print('Specify required id')
                                exit(-1)
                elif(options.Display):
                        obj = User()
                        obj.Display()
                elif(options.AddRecordHVD):
                        FName = options.FName
                        CPU = options.CPU
                        DiskFb = options.DiskFb
                        GivenDate = options.GivenDate
                        if (options.FName == FName and options.CPU == CPU and options.DiskFb == DiskFb and options.GivenDate == GivenDate):
                                obj = User()
                                obj.AddRecordHVD(FName,CPU,DiskFb,GivenDate)
                                print("Record added")
                        else: 
                                print('please specify all required arguments')
                                exit(-1)
                elif(options.bool):
                        obj = User()
                        obj.bool()
                elif(options.DeleteHVDRecords):
                        idhvdinfo=options.idhvdinfo
                        if(options.idhvdinfo == idhvdinfo):
                                obj = User()
                                obj.Delete(idhvdinfo)
                        else:
                                print("Specify required id")
                                exit(-1)
                elif(options.UpdateHVDRecord):
                        FName = options.FName
                        CPU = options.CPU
                        DiskFb = options.DiskFb
                        GivenDate = options.GivenDate
                        idhvdinfo = options.idhvdinfo
                        if(options.idhvdinfo == idhvdinfo):
                                obj = User()
                                obj.UpdateHVDRecord(FName,CPU,DiskFb,GivenDate,idhvdinfo)
                                
                        else:
                                print("Sepcify all required arguments")
                                exit(0)
                elif(options.HVDRecordsUsers):
                        idhvduser=options.idhvduser
                        if(idhvduser == options.idhvduser):
                                obj=User()
                                obj.HVDRecordsUsers(idhvduser)
                        else:
                                print("Enter the id you want to associate")
                                exit(-1)
                elif(options.HVDNRecordsUsers):
                        obj=User()
                        obj.HVDNRecordsUsers()
                else:
                       exit()
                
if __name__== '__main__':
         Main()
              
db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
curr = db.cursor()

curr.close()
db.close()

        
    

             
        
        
