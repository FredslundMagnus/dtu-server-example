{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f80b3872430>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f80b3877a60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f80b370a790>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f80b370a550>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f80b370a940>, '__hash__': None}

name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
GPU False <class 'bool'>
GPU False True
GPU False False
time 3600 <class 'int'>
time 3600 True
time 3600 False
b 2.0 <class 'float'>
b 2.0 True
b 2.0 False
a 2 <class 'int'>
a 2 True
a 2 False
d fd <class 'str'>
d fd True
d fd False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 21, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 94, in override
    _type = cls.__annotations__[key]
KeyError: 'ID'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548637: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:37:17 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:37:18 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:37:18 2022
Terminated at Fri Feb  4 19:37:19 2022
Results reported at Fri Feb  4 19:37:19 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.32 sec.
    Max Memory :                                 2 MB
    Average Memory :                             2.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16382.00 MB
    Max Swap :                                   -
    Max Processes :                              1
    Max Threads :                                2
    Run time :                                   25 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f2732297670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f273229caf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f273212e820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f273212e5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f273212e9d0>, '__hash__': None}

name Example3-1 str
name Example3-1 False
name Example3-1 True
GPU False bool
GPU False False
GPU False True
time 3600 int
time 3600 False
time 3600 True
b 2.0 float
b 2.0 False
b 2.0 True
a 2 int
a 2 False
a 2 True
d fd str
d fd False
d fd True
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 94, in override
    _type = cls.__annotations__[key]
KeyError: 'ID'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548641: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:39:02 2022
Job was executed on host(s) <n-62-31-23>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:39:03 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:39:03 2022
Terminated at Fri Feb  4 19:39:04 2022
Results reported at Fri Feb  4 19:39:04 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.44 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   21 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f0b5ccde670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f0b5cce3b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f0b5cb75820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f0b5cb755e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f0b5cb759d0>, '__hash__': None}

name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
GPU False <class 'bool'>
GPU False True
GPU False False
time 3600 <class 'int'>
time 3600 True
time 3600 False
b 2.0 <class 'float'>
b 2.0 True
b 2.0 False
a 2 <class 'int'>
a 2 True
a 2 False
d fd <class 'str'>
d fd True
d fd False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 94, in override
    _type = cls.__annotations__[key]
KeyError: 'ID'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548647: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:42:56 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:42:58 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:42:58 2022
Terminated at Fri Feb  4 19:42:59 2022
Results reported at Fri Feb  4 19:42:59 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.44 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   55 sec.
    Turnaround time :                            3 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f74224f9670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f74224feb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f7422390820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f74223905e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f74223909d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 100, in override
    cls.__setattr__(key, _type(value))
TypeError:  expected 2 arguments, got 1

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548650: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:45:28 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:45:29 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:45:29 2022
Terminated at Fri Feb  4 19:45:29 2022
Results reported at Fri Feb  4 19:45:29 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.43 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   30 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f8715e5b670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f8715e60b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f8715cf1820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f8715cf15e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f8715cf19d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 95, in override
    cls.__setattr__(key, _type.__call__(value))
TypeError:  expected 2 arguments, got 1

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548657: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:47:43 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:47:44 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:47:44 2022
Terminated at Fri Feb  4 19:47:44 2022
Results reported at Fri Feb  4 19:47:44 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.43 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   15 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fcb7c98a670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcb7c98fb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fcb7c821820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fcb7c8215e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fcb7c8219d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 94, in override
    print(f"{_type.__name__}({value})", eval(f"{_type.__name__}({value})"))
  File "<string>", line 1, in <module>
NameError: name 'Example3' is not defined

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548668: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:54:45 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:54:46 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:54:46 2022
Terminated at Fri Feb  4 19:54:47 2022
Results reported at Fri Feb  4 19:54:47 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.43 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   74 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f037dc41670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f037dc46b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f037dad7820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f037dad75e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f037dad79d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
False
False
False
True
GPU False <class 'bool'>
GPU False True
GPU False False
False
True
False
False
time 3600 <class 'int'>
time 3600 True
time 3600 False
True
False
False
False
b 2.0 <class 'float'>
b 2.0 True
b 2.0 False
False
False
True
False
a 2 <class 'int'>
a 2 True
a 2 False
True
False
False
False
d fd <class 'str'>
d fd True
d fd False
False
False
False
True
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 89, in override
    _type = cls.__annotations__[key]
KeyError: 'ID'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548671: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:58:00 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:58:01 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:58:01 2022
Terminated at Fri Feb  4 19:58:01 2022
Results reported at Fri Feb  4 19:58:01 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.44 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   38 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fdf0e4c6670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fdf0e4cbb50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fdf0e35c8b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fdf0e35c670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fdf0e35ca60>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 22, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 96, in override
    cls.__setattr__(key, value)
TypeError:  expected 2 arguments, got 1

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548675: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:01:01 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:01:03 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:01:03 2022
Terminated at Fri Feb  4 20:01:04 2022
Results reported at Fri Feb  4 20:01:04 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.45 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   63 sec.
    Turnaround time :                            3 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fa11bfce670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa11bfc4970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fa11be648b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fa11be64670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fa11be64a60>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 23, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 96, in override
    cls.__setattr__(cls, key, value)
TypeError: can't apply this __setattr__ to type object

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548678: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:04:35 2022
Job was executed on host(s) <n-62-31-2>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:04:36 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:04:36 2022
Terminated at Fri Feb  4 20:04:37 2022
Results reported at Fri Feb  4 20:04:37 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.44 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   93 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f84130b1670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f84130a79a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f8412f47820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f8412f475e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f8412f479d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
GPU False <class 'bool'>
GPU False True
GPU False False
time 3600 <class 'int'>
time 3600 True
time 3600 False
b 2.0 <class 'float'>
b 2.0 True
b 2.0 False
a 2 <class 'int'>
a 2 True
a 2 False
d fd <class 'str'>
d fd True
d fd False
Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Test/dtu-server-example/main.py", line 23, in <module>
    Defaults.start()
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 62, in start
    override = cls.override(argv[1:])
  File "/zhome/ee/d/137643/Desktop/Test/project-env/lib/python3.9/site-packages/dtu/server.py", line 85, in override
    _type = cls.__annotations__[key]
KeyError: 'ID'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548687: <Example3_1> in cluster <dcc> Exited

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:11:08 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:11:10 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:11:10 2022
Terminated at Fri Feb  4 20:11:22 2022
Results reported at Fri Feb  4 20:11:22 2022

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   0.34 sec.
    Max Memory :                                 3 MB
    Average Memory :                             3.00 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16381.00 MB
    Max Swap :                                   -
    Max Processes :                              1
    Max Threads :                                2
    Run time :                                   19 sec.
    Turnaround time :                            14 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7ff62e60a670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7ff62e4a0820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7ff62e4a05e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7ff62e4a09d0>, '__hash__': None}
name Example3-1 <class 'str'>
name Example3-1 True
name Example3-1 False
GPU False <class 'bool'>
GPU False True
GPU False False
time 3600 <class 'int'>
time 3600 True
time 3600 False
b 2.0 <class 'float'>
b 2.0 True
b 2.0 False
a 2 <class 'int'>
a 2 True
a 2 False
d fd <class 'str'>
d fd True
d fd False
ID 1 <class 'int'>
ID 1 True
ID 1 False
{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7ff62e60a670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff62e6009a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7ff62e4a0820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7ff62e4a05e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7ff62e4a09d0>, '__hash__': None}
2.0 fd 2
<class 'float'> <class 'str'> <class 'int'>
['main.py', '-name', 'Example3-1', '-GPU', 'False', '-time', '3600', '-b', '2.0', '-a', '2', '-d', 'fd', '-ID', '1']

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548693: <Example3_1> in cluster <dcc> Done

Job <Example3_1> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:14:42 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:14:44 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:14:44 2022
Terminated at Fri Feb  4 20:14:44 2022
Results reported at Fri Feb  4 20:14:44 2022

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

    CPU time :                                   0.32 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   1 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

