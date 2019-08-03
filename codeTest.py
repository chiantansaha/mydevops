#====================================================================================
#  Script: buildManager.py
#  Author: Chirantan Saha
#  Desc. : Build Manager script  
#
#  (C) Copyright, 2009, MyCompany Limited
#
#  Modification history:
#
#  DATE             Narrative                                     Author
#  dd/mm/yyyy      (succinct)                                   John Q. Public
#  ----------   --------------------------------------------   --------------
#       	Basic structure of script created		Chirantan
#  12/08/2009	IMP Modifications & Header added        	Chirantan
#===================================================================================


import os, sys
#import P4
import string, shutil
import utils
import time
import ftplib
#import odbc
#import mailer
import smtplib
import socket

P4CMD = 'p4 '
P4CMD2 = 'p4 '


'''
p4c = P4.P4()
run = p4c.run
#p4c.parse_forms()
p4c.port = "perforce:1666"
p4c.user = "sysbuildsvc"
p4c.password = ""
p4c.client = "csaha-test"
p4c.connect()
#p4c.run("login")
p4c.input = "abc"
p4c.run("login")

labelFileStat = []

SPECS = 'C:\BuildManager\specs'
all_clients = p4c.run("fstat","-P","//...@BB.75")

#print all_clients
for item in all_clients:
    #print item['depotFile'] , "#", item['headRev']
    labelFileStat.append(item['depotFile']+"#"+item['headRev'])


print labelFileStat

'''

"""

all_clients = p4c.run("clients","-u","sahachir")
#print all_clients #[0]["client"]

list_of_clients = []

for item in all_clients :
    #print item
    client_n = item["client"]
    list_of_clients.append(client_n)


print list_of_clients


files_opened = []

for client_item in list_of_clients :
    temp_opened_files = p4c.run("opened", "-C", client_item)
    files_opened.append(temp_opened_files)

print "files_opened =" , files_opened





#releaseid = "TB.36"


def getQClist(releasid):


    filespec = "//depot/...@" + releaseid

    aa = p4c.run("fstat","-Op",filespec)
    return aa #['clientFile']
    #print aa




all_qcs = getQClist("TB.36")

for item in all_qcs :
    print item['depotFile'] ,item['headRev']


#versionInfoFile = "//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/RSR/versioninfo.ini"


def getVersioninfoDetails(versionInfoFile):

    
try:
    # Run a "p4 client -t template -o" and convert it into a Python dictionary
    client = p4c.fetch_client("-t", template)
    print client

    # Now edit the fields in the form
    client["Root"] = client_root

    # Now save the udpated spec and sync it
    #p4c.save_client(client)
    #p4c.run_sync()

except:
    # If any errors occur, we'll jump in here. Just log them
    # and raise the exception up to the higher level
    for e in p4c.errors:
        
        print e
        raise e


    
#print aa
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    # Note: The versioninfo.ini file must have a new line after Build Number
    info = p4c.run("print","-q",versionInfoFile)
    p4c.disconnect()
    allLines = info[1].split("\n")
    
    for eachLine in allLines:
        
        print eachLine
        if eachLine.find("Major") >= 0:
            eachLine=eachLine.replace("\n", "").replace("\r", "") 
            majorNumber=eachLine.split("=").pop()
        if eachLine.find("Minor") >= 0:
            eachLine=eachLine.replace("\n", "").replace("\r", "")  
            minorNumber=eachLine.split("=").pop()
        if eachLine.find("BranchNumber") >= 0:
            eachLine=eachLine.replace("\n", "").replace("\r", "") 
            branchNumber=eachLine.split("=").pop()
        if eachLine.find("BuildNumber") >= 0:
            eachLine=eachLine.replace("\n", "").replace("\r", "") 
            buildNumber=eachLine.split("=").pop()

    print majorNumber, minorNumber, branchNumber, buildNumber
                
    
    

getVersioninfoDetails("//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/RSR/versioninfo.ini")





def deleteClient(clientName):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    aa = p4c.run("client","-d",clientName)

    print aa


deleteClient("cm-test-sys")

"""


"""
def generateClientSpec(clientName):
    'create clientspec text file and create the client'

    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "regit-build-template" #"csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")


    template = "regit-build-template"
    client_root = 'c:\\myroot'


    try :
        
        # Run a "p4 client -t template -o" and convert it into a Python dictionary
        client_tem = p4c.fetch_client("-t", template)
        print client_tem['View']

        new_client = client_tem
        # Now edit the fields in the form
        new_client["Root"] = client_root
        new_client["Client"]= clientName
        newView = "//depot/FinanceIT/RegIT/... //" + clientName + "/depot/FinanceIT/RegIT/..."
        new_client['View'] = [newView]
        #print client_tem["Root"]
        # Now save the udpated spec and sync it
        aa = p4c.save_client(new_client)
        print aa
        sync_exec = p4c.run_sync("-f","//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/...@REGULATORY_IT.REG_GLOBAL.QC2866")

        file_list = [] 
        for item in sync_exec:
            print item['clientFile']
            file_details = item['clientFile'].split("\\")[-3] + "+-+-+" + item['clientFile'].split("\\")[-2] + "+-+-+" + item['clientFile'].split("\\")[-1]
            file_list.append(file_details)
        print file_list
        #return file_list



    except:
        # If any errors occur, we'll jump in here. Just log them
        # and raise the exception up to the higher level
        for e in p4c.errors:
            
            print e
            raise e


        
    #print aa


generateClientSpec("csaha-test-sys")

"""

"""

def syncClientSpec(clientName,labelName):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = clientName #"csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    fileSpec = "//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/...@" + labelName

    file_list = [] 
    try:
       sync_exec = p4c.run_sync("-f",fileSpec)
         
       for item in sync_exec:
           only_file_name = item['clientFile'].split("\\")[-1]
           file_list.append(only_file_name)
       print file_list
            
    

        
    except:
        # If any errors occur, we'll jump in here. Just log them
        # and raise the exception up to the higher level
        for e in p4c.errors:
            
            print e
            #raise e

    
    
syncClientSpec("csaha-test-sys","REGULATORY_IT.REG_GLOBAL.TB_UNIX_CHANGES")    

"""



"""
def createWrapperScript(buildNumber,release_prefix,full_list_of_files,releaseWrapperFile):
    
    f = open(releaseWrapperFile,mode='w')
    f.write("/********************************************************************************\n")
    f.write("*  Script Name : " + release_prefix + "." + str(buildNumber) + ".sql\n") 
    f.write("*  Description : Wrapper script\n")
    f.write("*  Created On  : " + str(time.localtime()[2]) + "-" + str(time.localtime()[1]) + "-" + str(time.localtime()[0]) + "\n")
    f.write("*  Author      : Chirantan Saha \n")
    f.write("* \n")
    f.write("*  CHANGE History \n")
    f.write("* \n")
    f.write("*  DATE        VERSION  Author         	  Description \n")
    f.write("*  =====       =======  ===================    ========== \n")
    f.write("*  End Change  History  Chirantan Saha \n")
    f.write("* \n")
    f.write("********************************************************************************/\n\n\n")
    f.write("spool " + release_prefix + "." + str(buildNumber) + ".out\n\n\n")

    for item in full_list_of_files :
        f.write("prompt ---------------------------------------------- \n")
        f.write(" \n")
        f.write("prompt Compilation for " + item.keys()[0] + "\n")
        f.write(" \n")        
        f.write("prompt ---------------------------------------------- \n\n")

        for file_item in item.values()[0]:
            f.write("prompt Compiling " + file_item + "\n")
            f.write("@$RSR_RUNTIME/sql/3_1/"+ release_prefix + "/" + release_prefix + "." + buildNumber + "/" + file_item + "\n" )
            f.write(" \n")
        f.write(" \n\n")
            


    f.write("prompt ---------------------------------------------- \n\n\n\n\n")    
    f.write("BEGIN \n")
    f.write("  pk_release.pr_rsr_release_ccver    ( pScriptName       => '" + release_prefix + "." + buildNumber + ".sql'\n")
    f.write("                                     , pReleaseName      => '" + release_prefix + "." + buildNumber + "'\n")
    f.write("                                     , pSubReleaseLabel  => 'QC List'\n") # To be done later
    f.write("                                     , pMajorVersion     => 3.1\n")
    f.write("                                     , pMinorVersion     => 1\n")
    f.write("                                     , pCandidateVersion => " + buildNumber + "\n")
    f.write("                                     , pPatchVersion     => 0\n")
    f.write("                                     );\n")
    f.write("END;\n")
    f.write("/\n\n\n\n")    
    f.write("spool off\n")    
    f.close()

release_prefix = "TB"
file_list = [{'REGULATORY_IT.REG_GLOBAL.QC2510': ['TradingBook.br+-+-+RSR+-+-+versioninfo.ini', 'Ddl+-+-+Pkg+-+-+pk_cache.bdy', 'Ddl+-+-+Pkg+-+-+pk_tb_rwa.bdy']}, {'REGULATORY_IT.REG_GLOBAL.QC2564': ['Ddl+-+-+Pkg+-+-+pk_cache.bdy', 'Ddl+-+-+Pkg+-+-+pk_tb_rwa.bdy', 'Ddl+-+-+Pkg+-+-+pk_tb_exp_rolling_reversing.bdy']}, {'REGULATORY_IT.REG_GLOBAL.TB_UNIX_CHANGES': ['Ddl+-+-+Pkg+-+-+pk_tb_exp_rolling_reversing.bdy', 'Unix+-+-+load+-+-+gmis_hierarchy_load.ctl', 'Unix+-+-+load+-+-+sap_company_group_to_mcu_load.ctl', 'Unix+-+-+load+-+-+sap_company_load.ctl', 'Unix+-+-+load+-+-+sap_prod_hierarchy_load.ctl', 'Unix+-+-+load+-+-+us_sublink_load.ctl', 'Unix+-+-+Perl+-+-+CASTLE.pm', 'Unix+-+-+Perl+-+-+recalc_check.pl', 'Unix+-+-+Perl+-+-+rsr_trading_book_calc.pl', 'Unix+-+-+Perl+-+-+sap_company_load.pl', 'Unix+-+-+Perl+-+-+static_no_staging_load.pl', 'Unix+-+-+Perl+-+-+tb_static_file_get.pl', 'Unix+-+-+Perl+-+-+us_sublink_load.pl']}]
#label_list = ["label1", "label2", "label3"]
createWrapperScript("12","TB",file_list,"C:\\aa.sql")
"""


"""

def ftpFiles(ftpServer):

    cwd = os.getcwd()
    
    #os.chdir("C:\\data")

    fftp = ftplib.FTP(ftpServer)

    try :
        fftp.login(user='rrllt1o',passwd='impreza')
    except :
        print "unable to do ftp login in " + ftpServer + " server."
        sys.exit()
    
    currnt_working_dir = fftp.pwd( )
    print "Cuurent dir is ",currnt_working_dir

    fftp.cwd("/apps/lqdln-uat1/apps01/RSR_runtime/sql/3_1/TB") 
    
    currnt_working_dir = fftp.pwd( )
    print "Now cuurent dir is ", currnt_working_dir

    '''
    try:
        fftp.mkd("mytest")
    except:
        print "failed to create dir mytest as it already exists"
        sys.exit()
        

    fftp.cwd("mytest") 
    
    currnt_working_dir = fftp.pwd( )
    print "Now cuurent dir is ", currnt_working_dir

    


    local = open('aa.txt', 'r')
    fftp.storlines('STOR aa.txt', local)
    '''

    aa = os.popen(fftp.retrlines('LIST -p '))

    #print "aa = ", aa
    print aa.read( )


    os.chdir(cwd)


            
ftpFiles("lqdln-uat1.ldn.bzwint.com") 

"""    

"""
def arrangeIt(givenList):

    for item in givenList:
        item.values()[0].reverse()

    return givenList



alist = [{'REGULATORY_IT.REG_GLOBAL.QC2959': ['pk_amend_static.bdy', 'pk_amend_static.pkg']}, {'REGULATORY_IT.REG_GLOBAL.QC2875': ['PK_TB_BULK_CLIENT_ADJ.bdy', 'PK_TB_BULK_SUBFAC_ADJ.bdy', 'pk_tb_phoenix_client.bdy', 'pk_tb_phoenix_country.bdy', 'pk_tb_sub_facility.bdy']}, {'REGULATORY_IT.REG_GLOBAL.QC3000': ['pk_tb_rwa.bdy', 'pk_wra.bdy', 'pk_wra_data.bdy', 'pk_wra_data.pkg', 'wra_ddl_1.sql']}, {'REGULATORY_IT.REG_GLOBAL.QC2832_1': ['pk_wra_static_ext_write.bdy']}, {'REGULATORY_IT.REG_GLOBAL.QC2943_1': ['v_tb_rwa_adjustments.sql']}, {'REGULATORY_IT.REG_GLOBAL.QC2943': ['pk_tb_bulk_exp_adj.bdy', 'pk_tb_exp_rolling_reversing.bdy', 'pk_tb_exp_rolling_reversing.pkg', 'v_tb_rwa_adjustments.sql']}, {'REGULATORY_IT.REG_GLOBAL.QC2930': ['pk_tb_rwa.bdy', 'pk_tb_rwa.pkg']}]

newlist = arrangeIt(alist)
print newlist
"""

"""

def editsubmit(versionInfoFilePath,versionInfoFile):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "cm-sgpdwm019296"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    majorNumber="3.1"
    minorNumber="1"
    branchNumber="0"
    buildNumber="64"

    buildNumber = int(buildNumber) + 1
    buildNumber = str(buildNumber)

    p4c.run("edit",versionInfoFile)

    print "new .... ", majorNumber, minorNumber, branchNumber, buildNumber
    print "versionInfoFilePath = " , versionInfoFilePath
    try:
        f = open(versionInfoFilePath,mode='w')
        f.write("Major=" + majorNumber + "\n")
        f.write("Minor=" + minorNumber + "\n")
        f.write("BranchNumber=" + branchNumber + "\n")
        f.write("BuildNumber=" + buildNumber + "\n")
        f.close()
    except:
        print "Some problem here while writing on file"

    #cwd = os.getcwd()
    change = p4c.fetch_change()
    # Files were opened elsewhere and we want to
    # submit a subset that we already know about.
    print change
    myfiles = [versionInfoFile]
    change._description = "My changelist\nSubmitted from P4Python\n"
    change._files = myfiles # This attribute takes a Python list

    #cmd = P4CMD + ' -s login sysbuildsvc'
    #os.system(cmd)
    print change
    savechange = p4c.save_change(change)
    print savechange

    changelist_number = savechange[0].split(" ")[1]

    submit_change = p4c.run("submit","-c",changelist_number)
    print submit_change
        
##    submitDesc = 'build done'
##    filename = 'specs/submitspec.txt'
##    cmd = P4CMD + ' change -o > ' + filename
##    os.system(cmd)
##    utils.searchReplace(filename, "<enter description here>", submitDesc)
##    cmd = P4CMD2 + ' submit -i < ' + filename
##    os.system(cmd)

        

    #p4c.run_submit()  
    #p4c.input = "My submit"
    #p4c.run("submit",versionInfoFile)

versionInfoFilePath=r'C:\build\CASTLE1-branches-TradingBook.br-10\depot\FinanceIT\RegIT\CASTLE1\branches\TradingBook.br\RSR\versioninfo.ini'
versionInfoFile="//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/RSR/versioninfo.ini"

editsubmit(versionInfoFilePath,versionInfoFile)

"""
"""
def revertChanges(clientName):

    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "cm-sgpdwm019296"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    aa = p4c.run("revert","-a","//cm-sgpdwm019296/...")
    print aa
    p4c.disconnect()   

revertChanges("cm-sgpdwm019296")

"""

"""
def addAndSubmit(FilePath,user):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    p4c.run("add",FilePath)
    #cwd = os.getcwd()
    change = p4c.fetch_change()
    # Files were opened elsewhere and we want to
    # submit a subset that we already know about.
    print change
    
    #myfiles = [FilePath]
    change._description = "Build Triggered by " + user + " - This is the autogenerated Wrapper Script"
    #change._files = myfiles # This attribute takes a Python list

    #cmd = P4CMD + ' -s login sysbuildsvc'
    #os.system(cmd)
    print change
    savechange = p4c.save_change(change)
    print savechange

    changelist_number = savechange[0].split(" ")[1]

    submit_change = p4c.run("submit","-c",changelist_number)
    print submit_change


filepath =  r'C:\p4clients\csaha-test\depot\FinanceIT\RegIT\CASTLE1\users\sahachir\mydev\BuildManager\specs\test.txt'

addAndSubmit(filepath,"csaha")
"""


def connDB():

    connectString = 'PCGLNT01_DS' #The DSN name
    connect = odbc.odbc("PCGLNT01_DS/RSR/PCGLNT01")
    cursor = connect.cursor()
    cursor.execute("select * from TAB")
    results = cursor.fetchall()
    print results

#connDB()


def labelFiles():
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    aa = p4c.run("tag","-l","TB123","//depot/FinanceIT/RegIT/CASTLE1/branches/TradingBook.br/...@REGULATORY_IT.REG_GLOBAL.QC3060")
    print aa

#labelFiles()

   
def emailerMail(sub):
    print sub
    message = mailer.Message()
    message.From = "REGIT"
    message.To = "chirantan.saha@barcap.com"
    message.Subject = "My Test"
    message.Body = "AA" #open("letter.txt", "rb").read()
    print message.Body
    message.attach("build.log")

    mailer1 = mailer.Mailer('smtpmail.barcapint.com')
    mailer1.send(message)

#emailerMail("here")


def sendMail():
    ' send email messages using Python SMTO mail interface'
    mailServer = 'smtpmail.barcapint.com'
    fromAddress = 'REGIT-BuildManager'
    
    toAddress = "chirantan.saha@barcap.com,chirantan.saha@MyCompanyLimited.com"
    subject = 'Test mail '
    message = subject
    message = message + "\n\nThanks & Regards \nChirantan Saha\n\n"

      
    currentTime = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    print currentTime
    emailText = ('From: %s\nTo: %s\nSubject: %s\nDate:%s\n\n%s\n' % (fromAddress, toAddress, subject, currentTime, message))
    print emailText
            
    mailAddressList = toAddress.split(',') 
    for eachAddress in mailAddressList:
        server = smtplib.SMTP(mailServer)
        failed = server.sendmail(fromAddress, eachAddress, emailText)
        server.quit()
        if failed:
            print 'email failed', failed
        else:
            print 'email sent successfully'

#sendMail()


def changelists():
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    fileSpec = "//depot/FinanceIT/RegIT/CASTLE1/_trunk/main.br/RSR/..."
    
    full_change_dict = p4c.run("changes","-m 1000",fileSpec)

    my_cl_desc_dict = {}

    for itm in full_change_dict :
        my_cl_desc_dict[itm['change']]=itm['desc']

    cl_list = my_cl_desc_dict.keys()
    cl_list.sort()
    cl_list_old2recent = cl_list
    print "================\n"
    cl_list.reverse()
    cl_list_recent2old = cl_list
    #cl_list_recent2old = cl_list_old2recent.reverse()
 
    print cl_list_recent2old

    cl2label = []
    
    for item in cl_list_recent2old:
        cl_desc = my_cl_desc_dict[item]
        cl_desc_list = cl_desc.split(" ")
        #print cl_desc.split(" ")
        if cl_desc_list[0] == "BUILDMANAGER_SUPERBUILD" :
            break
        cl2label.append(item)

    cl2label.reverse()
    print cl2label

    for item in cl2label:
        itrm = "//depot/FinanceIT/RegIT/CASTLE1/_trunk/main.br/RSR/Database/..." + "@" + str(item) + ",@" + str(item)
        print itrm
        p4c.run("tag","-l","CSAHA_MYLABEL",itrm)

            
    #print aa

#changelists()


def revertPendingFiles(clientName):
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "Perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = clientName
    p4c.connect()
    #p4c.run("login")
    p4c.input = "abc"
    p4c.run("login")

    list_of_pending_cl_nos = []

    cl_run = p4c.run("changes","-s","pending","-c",clientName)
    print cl_run

    for item in cl_run:
        list_of_pending_cl_nos.append(item['change'])

    print list_of_pending_cl_nos

    #Now revert all files in all the pending-changelists and default changelist

    fileSpec = "//" + clientName + "/..."
    
    try:
        revert_default_pending_cl_files = p4c.run("revert","-c","default",fileSpec)
        print revert_default_pending_cl_files
    except :
        print "No files to revert in default changelist \n"
        pass


    for itr in list_of_pending_cl_nos:
        try:
            revert_numbered_pending_cl_files = p4c.run("revert","-c",itr,fileSpec)
            print revert_numbered_pending_cl_files
        except:
            print "Problem while reverting the files in numbered changelist \n"
            pass

        try:
            delete_empty_pending_cl = p4c.run("change","-d",itr)
            print delete_empty_pending_cl
        except:
            print "Problem while deleting the numbered changelist \n"
            pass
    
#revertPendingFiles("csaha-test")

def getSeqInfo(clientname):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = clientname
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    seqInfoFile = '//depot/FinanceIT/RegIT/CASTLE1/branches/NOV09REL.br/RDM/MSSQL/sequenceinfo.ini#8'
    
    i=1
    allLines=[]

    
    info = p4c.run("print","-q",seqInfoFile)
    p4c.disconnect()

    #print info

    for itm in info[1:]:
        #print itm
        checkLines = itm.split("\n")
        for itr in checkLines:
            itr = itr.replace("\n", "").replace("\r", "").replace(" ","")
            if itr != "" :
                allLines.append(itr)


    #print allLines    
    for item in allLines:
        print i,")",item
        i=i+1
    
#getSeqInfo("csaha-test")

        
def getFileListWOLabelsOnHeadRev(fileSpecList):
    
    p4c = P4.P4()
    run = p4c.run
    #p4c.parse_forms()
    p4c.port = "perforce:1666"
    p4c.user = "sysbuildsvc"
    p4c.password = ""
    p4c.client = "csaha-test"
    p4c.connect()
    p4c.input = "abc"
    p4c.run("login")

    for item in fileSpecList:
        all_files = p4c.run("files",item)

    

    filever_list_wo_labels = []
    
    for itr in all_files:
        #print itr
        headFileSpec = itr['depotFile'] + "#" + itr['rev']
        list_of_labels = p4c.run("labels","-m","4",headFileSpec)
        if list_of_labels == []:
            filever_list_wo_labels.append(headFileSpec)

    p4c.disconnect()
    
    print filever_list_wo_labels
        
        

    
getFileListWOLabelsOnHeadRev(['//depot/FinanceIT/RegIT/CASTLE1/branches/EQSMR.br/RDM/MSSQL/...'])    


