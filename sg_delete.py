from infinini import ibox_login
def sg_delete(sg_name):
        try:
                system=ibox_login("ibox1499")
                sg=system.cons_groups.find(system.cons_groups.fields.name == sg_name).to_list()
                if sg:
                        for sgn in sg:
                                if sgn.get_type() != 'SNAPSHOT':
                                        print "{} is not an Snap Group".format(sg_name) 
                                        return False,"Not SnapGroup provided"

                                #members=sgn.get_members().to_list()
                                #for member in members:  
                                #        print "member is {} has_children is {}".format(member,member.has_children())
                                #        if member.has_children():
                                #                print "{} - has snapshot(s)!!! cannot delete".format(member.get_name())
                                #                return False,"Volume has snapshots, cannot be deleted"
                                print "Deleting {}".format(sg_name)
                                sgn.delete(delete_members=True)
                                return True,"Deleted"
                else:
                        print "{} - Cannot be found".format(sg_name)
			return False, "Cannot be found"
        except Exception as E:
                print "caught exception {}".format(E)
                return False,E

