from infinini import ibox_login
def sg_delete(sg_name):
	system=ibox_login("ibox1499")
	sg=system.cons_groups.find(system.cons_groups.fields.name == sg_name).to_list()
	if sg:
		for sgn in sg:
			if sgn.get_type() != 'SNAPSHOT':
				print "{} is not an Snap Group".format(sg_name)	
				return False

			members=sgn.get_members().to_list()
			for member in members:	
				print "member is {} has_children is {}".format(member,member.has_children())
				if member.has_children():
					print "{} - has snapshot(s)!!! cannot delete".format(member.get_name())
					return False
			print "Deleting {}".format(sg_name)
			return sgn.delete(delete_members=True)
	else:
		print "{} - Cannot be found".format(sg_name)


