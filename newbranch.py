#====================================================================================
#  Script: newbranch.py
#  Author: Chirantan Saha
#  Desc. : New Branch Creation Script 
#
#  (C) Copyright, 2009, MyCompany Limited
#
#  Modification history:
#
#  DATE          Narrative                                       Author
#  dd/mm/yyyy      (succinct)                                   John Q. Public
#  ----------    --------------------------------------------   --------------
#  07/01/2010	New Branch Creation Script      		Chirantan
#===================================================================================

import p4,pprint,os,sys,pprint


class PerforceClient:

    def __init__(self,perforce,source,target,changelist_no=None):
        self.perforce = perforce
        self.source = source
        self.target = target
        self.changelist_no = changelist_no
        self.connectToPerforce()
        self.branch_spec = "cm-branch-automation-client"


    def connectToPerforce(self):
        self.p4c = p4.P4()
        self.p4c.parse_forms()
        self.p4c.port = self.perforce
        self.p4c.user = "sysbuildsvc"
        self.p4c.password = ""
        self.p4c.client = "cm-branch-automation-client"
        self.p4c.connect()
        self.p4c.login(self.p4c.password)

        
    def getUnresolveFiles(output):
        unresolved_files = []
        for lin in output:
            if " - resolve skipped." in lin:
                unresolved_files.append(lin.replace(" - resolve skipped.",""))
        print "Unresolved Files"
        pprint.pprint(unresolved_files)
        return unresolved_files


    def CreateBranchWithFileSpecification(self):

        #Add View To Client
        client_spec = self.p4c.fetch_client(self.p4c.client)
        root_depot = self.source.lstrip("//").split("/")[0]
        client_spec["View"] =["//"+ root_depot  + "/... //" + self.p4c.client + "/" + root_depot + "/..."]
        self.p4c.save_client(client_spec)
                              
        #Sync The source Branch
        self.p4c.run("sync","-f",self.source)
        #Sync The Target Branch
        self.p4c.run("sync","-f",self.target)

        # Get Client Root
        client_spec = self.p4c.fetch_client()
        client_root = client_spec["Root"]

        # Make Path to The Client view of the source Branch
        abs_path = os.path.abspath(client_root+self.source)

        #Change p4client cwd to source branch
        self.p4c.cwd  = abs_path

        #Run integration
        self.p4c.run("integ","-f",self.source+"@"+self.changelist_no,self.target)
        #Get ChangeList Template
        change_spec = self.p4c.fetch_change()
        #Change change Descrption
        change_spec["Description"] = self.source.split("/")[-2] + "@ " +self.changelist_no + "--> "+ self.target.split("/")[-2]
        
        #Save Changelist and get ChangeList No
        change_no = self.p4c.save_change(change_spec)[0].split(" ")[1]
        
        print change_no
        #Resolve And Accept Source Files If there is any conflicts
        result = self.p4c.run("resolve","-at",self.target)

        #unresolved_files = self.getUnresolveFiles(result)
        #for fil in unresolved_files:
        #    result = self.p4c.run("resolve","-at",self.target)
        #pprint.pprint(aa)
        #self.a

        #Submit ChangeList
        self.p4c.run("submit","-c",change_no)
        
        
    def CreateBranchWithBranchSpecification(self):
        #Add View To Client
        client_spec = self.p4c.fetch_client(self.p4c.client)
        root_depot = self.source.lstrip("//").split("/")[0]
        client_spec["View"] =["//"+ root_depot  + "/... //" + self.p4c.client + "/" + root_depot + "/..."]
        self.p4c.save_client(client_spec)
        
        #Sync The source Branch
        self.p4c.run("sync","-f",self.source)
        
        #Get new Branch template as python dictionery
        branch_spec = self.p4c.fetch_branch(self.branch_spec)
        
        #Change The Branch spec as required to branch
        self.source.split("/")[:-2]
        #Comment below two Lines for using same Branch Spec Temlate
        self.branch_spec = self.target.replace("//",'').replace("/...","").replace("/","-")
        src_group = self.source.replace("//",'').replace("/...","").replace("/","-") + "-submit"
        branch_spec["Branch"] = self.branch_spec
        branch_spec["View"] = [self.source + " " + self.target]
        branch_spec["Description"] = self.source.split("/")[-2] + "@ " +self.changelist_no + "--> "+ self.target.split("/")[-2]
        branch_spec["Options"] = "locked"
        
        #Save Branch Spec
        self.p4c.save_branch(branch_spec)
        
        #Set Input To Branch creation
        p4.input = branch_spec
        self.p4c.run("branch","-i")
        
        # Get Client Root
        client_spec = self.p4c.fetch_client()
        client_root = client_spec["Root"]
        #try:
        # Make Path to The Client view of the source Branch
        abs_path = os.path.abspath(client_root+self.source)
        #Change p4client cwd to source branch
        self.p4c.cwd  = abs_path
        
        #Run integration
        print self.p4c.run("integ","-b",self.branch_spec,"@"+self.changelist_no)
        
        #Get ChangeList Template
        change_spec = self.p4c.fetch_change()
        
        #Change change Descrption
        change_spec["Description"] = self.source.split("/")[-2] + "@ " +self.changelist_no + "-----> "+ self.target.split("/")[-2]
        
        #Save Changelist and get ChangeList No
        change_no = self.p4c.save_change(change_spec)[0].split(" ")[1]
        
        print change_no
        #Submit ChangeList
        self.p4c.run("submit","-c",change_no)

        #Set Protection Table
        protect_dict = self.p4c.fetch_protect()
        protect_dict['Protections'].append("write group " + self.branch_spec+"-submit " +"* " + self.target)
        self.p4c.save_protect(protect_dict)

        #Set Group for New Branch Created
        group_dict = self.p4c.fetch_group(src_group)
        group_dict['Group'] = self.branch_spec+"-submit"
        self.p4c.save_group(group_dict)
                                              

def main(perforce,src,trg,chg_no,from_branch=True):
    
    p4 = PerforceClient(perforce,src,trg,chg_no)
    if from_branch:
        p4.CreateBranchWithBranchSpecification()
    else:
        p4.CreateBranchWithFileSpecification()
        

if __name__ == "__main__":
    try:
        print sys.argv
        if len(sys.argv)<6:
            print "Usage:  python newbranch.py PerforceSevere:1666, Source,Target, ChangeListNo,FromBranchTrue"
            sys.exit()
        p4 = PerforceClient(sys.argv[1],sys.argv[2],sys.argv[3],sys.argv[4])

        if sys.argv[5]!='False':
            print "Calling CreateBranchWithBranchSpecification"
            p4.CreateBranchWithBranchSpecification()
        else:
            print "Calling CreateBranchWithFileSpecification"
            p4.CreateBranchWithFileSpecification()


    except Exception,ex:print ex
