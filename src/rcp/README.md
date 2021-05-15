###### RCP - Robot Configuration Parser
---
##### code generation
---
###### 1 -- define the robot configuration yml file
###### (yml file structure)
```yaml
<robot-name>:
  sensors:
    <sensor-name>:
      id: <id>
      type: <type>
      address: <address>
      topic: <topic>
      data: <data>
    <sensors-list ...>
  actuators:
    <actuator-name>:
      id: <id>
      address: <address>
      topic: <topic>
      commands:
        - <command-1>
        - <command-2>
        - <command-list ...>
    <actuators-list ...>
  commands:
    <command-1>:
      data: <data>
      time: <time>
    <command-2>:
      data: <data>
      time: <time>
    <command-list ...>
```
---
###### 2 -- generate the code
###### (rcp call synopsis, single config file)
```console
user@hostname:~$ python rcp.py config-file.yml
```
###### (rcp call synopsis, multiple config files)
```console
user@hostname:~$ python rcp.py config-file-1.yml config-file-2.yml ...
```
---
###### 3 -- generated code, filesystem tree
```
out
├── <robot-name-1>
│   ├── noros
│   │   ├── __init__.py
│   │   ├── broker.py
│   │   ├── core.py
│   │   └── template.py
│   └── ros
│       ├── __init__.py
│       ├── broker.py
│       ├── core.py
│       └── interface.py
├── <robot-name-2>
│   ├── noros
│   │   ├── __init__.py
│   │   ├── broker.py
│   │   ├── core.py
│   │   └── template.py
│   └── ros
│       ├── __init__.py
│       ├── broker.py
│       ├── core.py
│       └── interface.py
├── ...
...
```
---
##### usage
---
###### ROS
###### 1 -- download a docker virtual machine w/ a ros2 full environment
###### (example: link: , ros dashing, ubuntu-based)
```console
user@hostname:~$ docker pull
```
###### 2 -- install dependency
```console
user@dockervirtmach:~$ pip install redis
```
###### 3 -- create a ros2 python package (or 4)
```console
user@dockervirtmach:~$ ros2 pkg create --build-type ament_python <package_name>
user@dockervirtmach:~$ colcon build --symlink-install
user@dockervirtmach:~$ source install/setup.bash
user@dockervirtmach:~$ ros2 run <package_name> <node-name>
```
###### 4 -- use shared volume

TODO
