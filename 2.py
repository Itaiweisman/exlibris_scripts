from __future__ import print_function
from infinini import ibox_login
from infinisdk import Q
system=ibox_login("infinibox01-vip.dc01")
vol_snaps=system.volumes.find(Q.type == 'snapshot').to_list()
fs_snaps=system.filesystems.find(Q.type == 'snapshot').to_list()
header = """ --------------------+--------------------+----------+------+-------+------------
Volume               Snapshot             Size       Online Status  New Data
Name                 Name                 (MB)                      (MB)
--------------------+--------------------+----------+------+-------+------------"""

print (header)
for snap in vol_snaps:
        parent=snap.get_family_master()
        if (parent.get_id()):
                parent_name=parent.get_name()
                name=snap.get_name()
                size=parent.get_size().bits/8/1024/1024
                new_data=snap.get_size().bits/8/1024/1024
                online_status="Okay"
                print (parent_name,name,size,online_status,new_data)

print (header)
for snap in fs_snaps:
        parent=snap.get_family_master()
        if (parent.get_id()):
                parent_name=parent.get_name()
                name=snap.get_name()
                size=parent.get_size().bits/8/1024/1024
                new_data=snap.get_size().bits/8/1024/1024
                online_status="Okay"
                state='No'
                print (parent_name,name,size,state,online_status,new_data)      

        

