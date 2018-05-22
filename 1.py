from infinini import ibox_login
system=ibox_login("ibox1499")
header="""--------------------+---------------------------------------+-------+-----------
Volume Collection    Snapshot Collection                     Num     Replication
Name                 Name                                    Snaps   Status
--------------------+---------------------------------------+-------+-----------"""

cgs=system.cons_groups.find(system.cons_groups.fields.type == 'master').to_list()
for cg in cgs:
	print header
	cg_name=cg.get_name()
	count=cg.get_members_count()
	rep_stat=cg.is_replicated()
	children=cg.get_children().to_list()
	for child in children:
		sg_name=child.get_name()
		print "{} {}     {} {}".format(cg_name,sg_name,count,rep_stat)
	

