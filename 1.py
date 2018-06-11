from infinini import ibox_login
system=ibox_login("infinibox01-vip.dc01")
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
        reps=cg.get_replicas().to_list()
        if (reps):
                if reps[0].get_progress() == 100:
                        rep_stat='Complete'
                else:
                        rep_stat='In-progress'
        else:
                rep_stat='N/A'
        children=cg.get_children().to_list()
        for child in children:
                sg_name=child.get_name()
                print "{} {}     {} {}".format(cg_name,sg_name,count,rep_stat)
        
