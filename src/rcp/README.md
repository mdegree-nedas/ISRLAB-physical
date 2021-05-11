###### RCP - Robot Configuration Parser
---
##### test (freenove)

###### sensors
```
 ultrasound: vector, 3 values (left, center, right)
lightsensor: vector, 2 values (left, right)
linetracker: vector, 3 values (3 binaries)
```

###### actuators
```
motion: vector[vector,vector], 6 values [linear[x,y,z], angular[x,y,z]]
   led: vector, 3 values
```

###### commands (in general)
```
          atomic: (no data, no time)
      indefinite: (data, no time)
durative_no_data: (no data, time)
        durative: (data, time)
```
---
##### todo

###### (parser) add redis/ros abstract topic name:
```yaml
robot-name:
  sensors:
    topic: <topic-name>
    <sensors-list>
  actuators:
    topic: <topic-name>
    <actuators-list>
```
###### (code-generator) build a redis client init routine
###### (code-generator) add redis client library dependency
###### (code-generator) build json messages wrapper
