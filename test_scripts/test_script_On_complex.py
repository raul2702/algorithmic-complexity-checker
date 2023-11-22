import threading
import time
import os
import sys

clusters = ["mcr-cay-cluster-15"]
hosts=["mcr-host-253"]
user = "superuser"
port = "22"

format_string = "==============================================================================================================================================================================="
livedump = "no"
concurrentnodedumps = "no"
svc_snap = "no"
host_snap="no"

def take_concurrent_node_dump(cluster_list):
    for cluster in cluster_list:
        print("Taking concurrent node dumps on cluster: " + cluster)
        result, output, stderr = test_utils.runSSHCommand(user, cluster, "svctask concurrentnodedump", port)
        if(result):
            print(output[0].decode('utf-8'))
            time.sleep(300)
        else: 
            print(stderr[0].decode('utf-8'))

def take_livedumps(cluster_list):
    for cluster in cluster_list:
        print("taking livedump on on cluster: " + cluster)
        node_list = build_node_list(cluster)
       # print(str(len(node_list)))
        test_utils.runSSHCommand(user, cluster, "for i in {1.." + str(len(node_list)) + "}; do svctask preplivedump node$i;done", port)
       
        print("Prepared livedump on all nodes in cluster: "+ cluster + ", pausing for 10 seconds")
        time.sleep(10)

        print("Triggering livedumps on all nodesin cluster: " + cluster + ", this can take 5 minutes to complete.")
        test_utils.runSSHCommand(user, cluster, "for i in {1.." + str(len(node_list)) + "}; do svctask triggerlivedump node$i;done", port)
        time.sleep(300)
        print("livedumps collection completed on cluster: " + str(cluster))

        def take_node_snaps(cluster_list):
            for cluster in cluster_list:
                result, snap_output, stderr = test_utils.runSSHCommand(user, cluster, "svc_snap -a", port)
                if(result):
                    time.sleep(240)
                    print("Please continue to wait, snaps are still being taken.")
                    time.sleep(240)
                    for line in snap_output:
                        print(line.decode('utf-8'))
                else:
                    print(stderr[0].decode('utf-8'))
    
    
