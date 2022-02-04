2.0 fd 1

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548596: <Example2_0> in cluster <dcc> Done

Job <Example2_0> was submitted from host <n-62-27-17> by user <s183905> in cluster <dcc> at Fri Feb  4 18:52:40 2022
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Feb  4 18:52:41 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 18:52:41 2022
Terminated at Fri Feb  4 18:52:42 2022
Results reported at Fri Feb  4 18:52:42 2022

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   53 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

2.0 fd 1

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548604: <Example2_0> in cluster <dcc> Done

Job <Example2_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:07:48 2022
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:07:49 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:07:49 2022
Terminated at Fri Feb  4 19:07:50 2022
Results reported at Fri Feb  4 19:07:50 2022

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   77 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.
