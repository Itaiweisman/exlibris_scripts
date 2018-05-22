from __future__ import print_function
from infinini import ibox_login
system=ibox_login("ibox1499")
cgs=system.cons_groups.find(system.cons_groups.fields.type == 'master').to_list()
for cg in cgs:
	cg_name=cg.get_name()
	print(cg_name+":",end=' ')
	children=cg.get_children().to_list()
	for child in children:
		sg_name=child.get_name()
		print (sg_name,end='  ')
	print('\n')
	

