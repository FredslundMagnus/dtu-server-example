2.0 fd 1
['main.py', '-name', 'Example2-0', '-GPU', 'True', '-time', '3600', '-b', '4.0', '-a', '1', '-d', 'dssf', '-ID', '0']

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548612: <Example2_0> in cluster <dcc> Done

Job <Example2_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:12:13 2022
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:12:13 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:12:13 2022
Terminated at Fri Feb  4 19:12:15 2022
Results reported at Fri Feb  4 19:12:15 2022

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

    CPU time :                                   0.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   5 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f442a20b430>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f442a210b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f442a09c790>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f442a09c550>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f442a09c940>, '__hash__': None}
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 21, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 63, in start
    cls.override(argv[1:])
TypeError: override() takes 1 positional argument but 2 were given

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548615: <Example2_0> in cluster <dcc> Exited

Job <Example2_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:18:11 2022
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:18:13 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:18:13 2022
Terminated at Fri Feb  4 19:18:15 2022
Results reported at Fri Feb  4 19:18:15 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   16 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fa2ab036430>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa2ab03bb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fa2aaec7790>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fa2aaec7550>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fa2aaec7940>, '__hash__': None}
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 21, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 63, in start
    cls.override(argv[1:])
TypeError: override() takes 1 positional argument but 2 were given

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548618: <Example2_0> in cluster <dcc> Exited

Job <Example2_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:19:50 2022
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:19:51 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:19:51 2022
Terminated at Fri Feb  4 19:19:52 2022
Results reported at Fri Feb  4 19:19:52 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.35 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   97 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

