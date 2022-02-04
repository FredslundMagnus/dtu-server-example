{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f970b796430>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f970b79ba60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f970b62e790>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f970b62e550>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f970b62e940>, '__hash__': None}

name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548636: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:37:17 2022
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

    CPU time :                                   0.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   25 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fe5fe651670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fe5fe656b50>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fe5fe4e8820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fe5fe4e85e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fe5fe4e89d0>, '__hash__': None}

name Example3-0 str
name Example3-0 False
name Example3-0 True
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
Subject: Job 12548640: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:39:01 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:39:03 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:39:03 2022
Terminated at Fri Feb  4 19:39:03 2022
Results reported at Fri Feb  4 19:39:03 2022

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

    CPU time :                                   0.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   37 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f45a16bb670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f45a16c0b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f45a1552820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f45a15525e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f45a15529d0>, '__hash__': None}

name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548646: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:42:56 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:42:58 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 19:42:58 2022
Terminated at Fri Feb  4 19:42:58 2022
Results reported at Fri Feb  4 19:42:58 2022

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
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   88 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f1c51f57670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f1c51f5cb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f1c51dee820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f1c51dee5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f1c51dee9d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548649: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:45:28 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:45:29 2022
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

    CPU time :                                   0.35 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   31 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fdb4ce92670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fdb4ce97b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fdb4cd28820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fdb4cd285e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fdb4cd289d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548656: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:47:43 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:47:44 2022
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

    CPU time :                                   0.32 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   3 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7f4e98473670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f4e98478b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f4e9830a820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f4e9830a5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f4e9830a9d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548667: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:54:45 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:54:46 2022
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

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   86 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fc18329a670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fc18329fb20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fc183130820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fc1831305e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fc1831309d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548670: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 19:58:00 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 19:58:01 2022
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

    CPU time :                                   0.34 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   74 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fb743f8b670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fb743f90b20>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fb743e218b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fb743e21670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fb743e21a60>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548674: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:01:01 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:01:03 2022
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

    CPU time :                                   0.35 sec.
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

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fa485984670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa48597a970>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fa48581a8b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fa48581a670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fa48581aa60>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548677: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:04:35 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:04:36 2022
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

    CPU time :                                   0.35 sec.
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

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7ff1187da670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7ff1187d09a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7ff118670820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7ff1186705e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7ff1186709d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
Subject: Job 12548686: <Example3_0> in cluster <dcc> Exited

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:11:08 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:11:10 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:11:10 2022
Terminated at Fri Feb  4 20:11:10 2022
Results reported at Fri Feb  4 20:11:10 2022

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
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   19 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fcdcbcf9670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fcdcbb8f820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fcdcbb8f5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fcdcbb8f9d0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
ID 0 <class 'int'>
ID 0 True
ID 0 False
{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'd': 'fd', 'run': <function Defaults.run at 0x7fcdcbcf9670>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fcdcbcef9a0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fcdcbb8f820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fcdcbb8f5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fcdcbb8f9d0>, '__hash__': None}
2.0 fd 2
<class 'float'> <class 'str'> <class 'int'>
['main.py', '-name', 'Example3-0', '-GPU', 'False', '-time', '3600', '-b', '2.0', '-a', '2', '-d', 'fd', '-ID', '0']

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548692: <Example3_0> in cluster <dcc> Done

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:14:42 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:14:42 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:14:42 2022
Terminated at Fri Feb  4 20:14:43 2022
Results reported at Fri Feb  4 20:14:43 2022

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

    CPU time :                                   0.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   81 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'c': <class 'bool'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'c': True, 'd': 'fd', 'run': <function Defaults.run at 0x7fa9c80194c0>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, c: bool = True, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'c': Field(name='c',type=<class 'bool'>,default=True,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fa9c7eaf820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fa9c7eaf5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fa9c7eafa60>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
c True <class 'bool'>
c True True
c True False
d fd <class 'str'>
d fd True
d fd False
ID 0 <class 'int'>
ID 0 True
ID 0 False
{'__module__': '__main__', '__annotations__': {'name': <class 'str'>, 'instances': <class 'int'>, 'GPU': <class 'bool'>, 'time': <class 'int'>, 'b': <class 'float'>, 'a': <class 'int'>, 'c': <class 'bool'>, 'd': <class 'str'>}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'c': True, 'd': 'fd', 'run': <function Defaults.run at 0x7fa9c80194c0>, '__doc__': "Defaults(name: str = 'local', instances: int = 1, GPU: bool = False, time: int = 3600, b: float = 2.0, a: int = 1, c: bool = True, d: str = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type=<class 'str'>,default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type=<class 'bool'>,default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type=<class 'int'>,default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type=<class 'float'>,default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type=<class 'int'>,default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'c': Field(name='c',type=<class 'bool'>,default=True,default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type=<class 'str'>,default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7fa9c800faf0>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7fa9c7eaf820>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7fa9c7eaf5e0>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7fa9c7eafa60>, '__hash__': None}
2.0 fd 2 True
<class 'float'> <class 'str'> <class 'int'> <class 'bool'>

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548697: <Example3_0> in cluster <dcc> Done

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:16:42 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:16:43 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:16:43 2022
Terminated at Fri Feb  4 20:16:43 2022
Results reported at Fri Feb  4 20:16:43 2022

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

    CPU time :                                   0.33 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   119 sec.
    Turnaround time :                            1 sec.

The output (if any) is above this job summary.

{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'c': 'bool', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'c': True, 'd': 'fd', 'run': <function Defaults.run at 0x7f492d9a8820>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, c: 'bool' = True, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'c': Field(name='c',type='bool',default=True,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f492d83f8b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f492d83f670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f492d83faf0>, '__hash__': None}
name Example3-0 <class 'str'>
name Example3-0 True
name Example3-0 False
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
c True <class 'bool'>
c True True
c True False
d fd <class 'str'>
d fd True
d fd False
ID 0 <class 'int'>
ID 0 True
ID 0 False
{'__module__': '__main__', '__annotations__': {'name': 'str', 'instances': 'int', 'GPU': 'bool', 'time': 'int', 'b': 'float', 'a': 'int', 'c': 'bool', 'd': 'str'}, 'name': 'local', 'instances': 1, 'GPU': False, 'time': 3600, 'b': 2.0, 'a': 1, 'c': True, 'd': 'fd', 'run': <function Defaults.run at 0x7f492d9a8820>, '__doc__': "Defaults(name: 'str' = 'local', instances: 'int' = 1, GPU: 'bool' = False, time: 'int' = 3600, b: 'float' = 2.0, a: 'int' = 1, c: 'bool' = True, d: 'str' = 'fd')", '__dataclass_params__': _DataclassParams(init=True,repr=True,eq=True,order=False,unsafe_hash=False,frozen=False), '__dataclass_fields__': {'name': Field(name='name',type='str',default='local',default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'instances': Field(name='instances',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'GPU': Field(name='GPU',type='bool',default=False,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'time': Field(name='time',type='int',default=3600,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'b': Field(name='b',type='float',default=2.0,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'a': Field(name='a',type='int',default=1,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'c': Field(name='c',type='bool',default=True,default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD), 'd': Field(name='d',type='str',default='fd',default_factory=<dataclasses._MISSING_TYPE object at 0x7f492d99ea60>,init=True,repr=True,hash=None,compare=True,metadata=mappingproxy({}),_field_type=_FIELD)}, '__init__': <function __create_fn__.<locals>.__init__ at 0x7f492d83f8b0>, '__repr__': <function __create_fn__.<locals>.__repr__ at 0x7f492d83f670>, '__eq__': <function __create_fn__.<locals>.__eq__ at 0x7f492d83faf0>, '__hash__': None}
2.0 fd 2 True
<class 'float'> <class 'str'> <class 'int'> <class 'bool'>

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548700: <Example3_0> in cluster <dcc> Done

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:17:54 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:17:56 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:17:56 2022
Terminated at Fri Feb  4 20:17:56 2022
Results reported at Fri Feb  4 20:17:56 2022

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
    Run time :                                   60 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

2.0 fd 2 True

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 12548703: <Example3_0> in cluster <dcc> Done

Job <Example3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Fri Feb  4 20:20:32 2022
Job was executed on host(s) <n-62-31-21>, in queue <hpc>, as user <s183905> in cluster <dcc> at Fri Feb  4 20:20:33 2022
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Test/dtu-server-example> was used as the working directory.
Started at Fri Feb  4 20:20:33 2022
Terminated at Fri Feb  4 20:20:34 2022
Results reported at Fri Feb  4 20:20:34 2022

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

    CPU time :                                   0.35 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   14 sec.
    Turnaround time :                            2 sec.

The output (if any) is above this job summary.

