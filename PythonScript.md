# Database-Python-scripting
#Adds,Updates,displays,Associates users to respective HVDs
import os
import MySQLdb
import random
import optparse

class User():
        def Insert(self):
                print('To Add your information follow the procedure')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                Fname = raw_input("Enter your FName: ")
                Email = raw_input("Enter your email: ")
                Address = raw_input("Enter your address: ")
                Phoneno = int(raw_input("Enter your number: "))
                Age = int(raw_input("Enter your age: "))
                try:
                    curr.execute("""INSERT INTO hvduser(Fname,Email,Address,Phoneno,Age) VALUES ('%s','%s','%s',%d,%d)""" %(Fname,Email,Address,Phoneno,Age))
                    db.commit()
                except:
                    db.rollback()
                print("Information Added")
                curr.execute("""SELECT * FROM hvduser;""")
                print curr.fetchall()
                ((Fname,Email,Address,Phoneno,Age),)
                return("%s,%s,%s,%d,%d") % (Fname,Email,Address,Phoneno,Age)

        def Delete(self):
                print('Deletion Process')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                idnumber = int(raw_input("Enter the id number,You want to delete: "))
                curr.execute(("""DELETE FROM hvduser WHERE idhvduser = %d;""") % (idnumber))
                db.commit()  
                print("Information Deleted")
                curr.execute("""SELECT * FROM hvduser;""")
                return("%d") % (idnumber)
                

        def Update(self):
                print('Updation process')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                idnumberr = int(raw_input("Input the ID number you want to update: "))
                curr.execute(("""SELECT idhvduser FROM hvduser WHERE idhvduser = %d;""") % (idnumberr))
                newFname = raw_input("Enter new name")
                newEmail = raw_input("Enter new email")
                newAddress = raw_input("Enter new address")
                newPhoneno = int(raw_input("Enter new Phoneno"))
                newAge = int(raw_input("Enter new Age"))
                curr.execute(("""UPDATE hvduser set Fname = '%s',Email ='%s',Address = '%s',Phoneno=%d,Age=%d WHERE (Fname,Email,Address,Phoneno,Age);""") % (newFname,newEmail,newAddress,newPhoneno,newAge))
                db.commit()
                print("Information DUpdated")
                curr.execute("""SELECT * FROM hvduser;""")
                print curr.fetchall()
                ((newFname,newEmail,newAddress,newPhoneno,newAge),)
                return("%d") % (idnumberr)
                

        def Display():
                print("Listing all the users of Database")
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""SELECT * FROM hvduser;""")
                return;

        def AddRecordHVD(self):
                print('To Add your HVD record information,follow the procedure')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                FName = raw_input("Enter your FName: ")
                CPU = raw_input("Enter your CPU: ")
                Diskfb = raw_input("Enter your DiskFb: ")
                GivenDate = long(raw_input("Enter Given Date: "))
                try:
                    sql=("""INSERT INTO hvdinfo(FName,CPU,Diskfb,GivenDate) VALUES ('%s','%s','%s',%d)""" %(FName,CPU,Diskfb,GivenDate))
                    curr.execute(sql)
                    db.commit()
                except:
                    db.rollback()
                print("Record Added")
                curr.execute("SELECT * FROM hvdinfo;")
                print curr.fetchall()
                ((FName,CPU,Diskfb,GivenDate),)
                return("%s,%s,%s,%d") % (FName,CPU,Diskfb,GivenDate)
                

        def bool():
                    v = raw_input("Enter the status of HVD")
                    if v.lower():
                            print("status is on")
                    else:
                            print("Status is off")
                    return v.lower() in ("Yes","true","t","1")

        def DeleteHVDRecords():
                print('Delete the HVD Record')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                idnumber = int(raw_input("Enter the id number,You want to delete: "))
                curr.execute(("""DELETE FROM hvdinfo WHERE idhvdinfo = %d;""") % (idnumber))
                db.commit()
                print("Record Deleted")
                curr.execute("""SELECT * FROM info;""")
                return("%d") % (idnumber)
                

        def UpdateHVDRecord():
                print('Update HVD record')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                idnumberr = int(raw_input("Input the ID number you want to update: "))
                curr.execute(("""SELECT idhvdinfo FROM hvdinfo WHERE idhvdinfo = %d;""") % (idnumberr))
                newFname = raw_input("Enter new name")
                newCPU = raw_input("Enter new CPU")
                newDiskfb = raw_input("Enter new Diskfb")
                newGivenDate = int(raw_input("Enter new Date"))
                curr.execute(("""UPDATE info set Fname = '%s',CPU ='%s',Diskfb = '%s',GivenDate=%d WHERE (Fname,CPU,Disfb,GivenDate);""") % (newFname,newCPU,newDiskfb,newGivenDate))
                db.commit()
                print("Record Updated")
                curr.execute("""SELECT * FROM info;""")
                return("%d") % (idnumberr)
                

        def HVDRecordsUsers():
                print('Displaying all the records associated to users')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""SELECT hvduser.idhvduser,hvduser.Fname,hvdinfo.CPU,hvdinfo.DISKfb,hvdinfo.GivenDate FROM hvdinfo INNER JOIN hvduser ON hvduser.Fname = hvdinfo.FName;""")
                db.commit()
                curr.execute("""SELECT * FROM info;""")
                return;
                

        def HVDNRecordsUsers():
                print('Displaying all the records notassociated to users')
                db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
                curr = db.cursor()
                curr.execute("""SELECT idhvduser,FName,CPU,DISKfb,GivenDate FROM hvduser,hvdinfo WHERE hvduser.Fname = hvdinfo.FName AND hvdinfo.FName = NULL;""")
                return;

def Main():
                parser = optparse.OptionParser(('usage %prog :'+\
                        "-a=Insert,-d=Delete,-u=Upgrade,--ih=AddRecordHVD,-b=bool,--dh=DeleteHVDRecords,--uh=UpdateHVDRecord,--rh=RecordsHVDUsers,--nh=NRecordsHVDUsers"))
                parser.add_option('-a',action='store',dest='Insert',help='To Insert your user Information')
                parser.add_option('-d',dest='Delete',help="To delete your user Information")
                parser.add_option('-u',action='store',dest='Update',help="To update your user information")
                parser.add_option('--ih',action='store',dest='AddRecordHVD',help='To Enter HVD Record')
                parser.add_option('-b',action='store_true',dest='bool',default=False,help='Enter the HVD status')
                parser.add_option('--dh',dest='DeleteHVDRecords',help='To Delete your HVD record')
                parser.add_option('--uh',action='store',dest='UpdateHVDRecord',help='Update your HVD Record')
                parser.add_option('--rh',dest='RecordsHVDUsers',help='Displays Records associated to Users')
                parser.add_option('--nh',dest='NRecordsHVDUsers',help='Displays Records not associated to Users')
                parser.add_option('--du',dest='Display',help='Displays user information')
                (options, args) = parser.parse_args()
                if(options.Insert):
                        obj = User()
                        obj.Insert()
                elif(options.Delete):
                        obj = User()
                        obj.Delete()
                elif(options.Update):
                        obj = User()
                        obj.Update()
                elif(options.Display):
                        obj = User()
                        obj.Display()
                elif(options.AddRecordHVD):
                        obj = User()
                        obj.AddRecordHVD()
                elif(options.bool):
                        obj = User()
                        obj.bool()
                elif(options.DeleteHVDRecords):
                        obj=User()
                        obj.DeleteHVDRecords()
                elif(options.UpdateHVDRecord):
                        obj=User()
                        obj.UpdateHVDRecords()
                elif(options.RecordsHVDUsers):
                        obj=User()
                        obj.RecordsHVDUsers()
                elif(options.NRecordsHVDUsers):
                        obj=User()
                        obj.NRecordsHVDUsers()
                else:
                       exit()
                
if __name__== '__main__':
         Main()
              
db = MySQLdb.connect(host="localhost",user="root",passwd="hamzabaig",db="hvd")
curr = db.cursor()

curr.close()
db.close()
