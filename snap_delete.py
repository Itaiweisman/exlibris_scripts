from infinini import ibox_login
def snap_delete(snap_name):
        try:
                system=ibox_login("ibox1499")
                snap=system.volumes.find(system.volumes.fields.name == snap_name,type='SNAPSHOT').to_list()
                if snap:
			snapn=snap[0]
			if snapn.get_family_master().get_cons_group():
				print "Snapshot master volume is in a CG ";
				return False,"Master is in CG";
			return snapn.delete()
                else:
                        print "{} - Cannot be found".format(snap_name)
			return False, "Cannot be found"
        except Exception as E:
                print "caught exception {}".format(E)
                return False,E
snap_delete('s1')
