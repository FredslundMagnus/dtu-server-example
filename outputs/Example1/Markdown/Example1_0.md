4.0 dsf

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12561536: <Example1_0> in cluster <dcc> Done

Job <Example1_0> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Sat Feb  5 22:03:09 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat Feb  5 22:03:10 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/dtu-server-example/dtu-server-example> was used as the working directory.
Started at Sat Feb  5 22:03:10 2022
Terminated at Sat Feb  5 22:03:11 2022
Results reported at Sat Feb  5 22:03:11 2022

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   0.48 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   117 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

