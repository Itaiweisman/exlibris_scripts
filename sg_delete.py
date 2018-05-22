from infinini import ibox_login
def sg_delete(sg_name):
	system=ibox_login("ibox1499")
	sg=system.cons_groups.find(system.cons_groups.fields.name == sg_name).to_list()
	for sgn in sg:
		if (sgn.get_children().to_list()):
			print "Cannot delete SG {} which has snapshots".format(sgn)
		else:
			sgn.delete()


