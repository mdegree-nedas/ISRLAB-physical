###### rasberry os install (using linux)

* *(download rasberry os image from official site)*
* *(in this example,* `/dev/mmcblk0` *is the location of the SDcard in which you will install the OS)*

```console
user@host:~$ mkdir image
user@host:~$ unzip 2021-03-04-raspios-buster-armhf.zip -d image
user@host:~$ cd image 
user@host:~$ sudo dd if=2021-03-04-raspios-buster-armhf.img of=/dev/mmcblk0 bs=1M conv=fsync status=progress
```

###### rasberry os env config (docker install)

```console
user@raspberry:~$ sudo apt update
user@raspberry:~$ sudo apt upgrade
user@raspberry:~$ sudo apt install -y apt-transport-https ca-certificates curl gnupg2 software-properties-common
user@raspberry:~$ curl -fsSL https://download.docker.com/linux/$(. /etc/os-release; echo "$ID")/gpg | sudo apt-key add -
user@raspberry:~$ echo "deb [arch=$(dpkg --print-architecture)] https://download.docker.com/linux/$(. /etc/os-release; echo "$ID") $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list
user@raspberry:~$ sudo apt update
user@raspberry:~$ sudo apt install -y --no-install-recommends docker-ce cgroupfs-mount
user@raspberry:~$ sudo systemctl enable docker
user@raspberry:~$ sudo systemctl start docker
user@raspberry:~$ sudo usermod -aG docker pi
user@raspberry:~$ sudo systemctl reboot
```

###### rasberry os env config (docker test)

```console
user@raspberry:~$ docker run hello-world
```

###### rasberry os env config (docker-compose install)

```console
user@raspberry:~$ sudo apt update
user@raspberry:~$ sudo apt install python3-pip libffi-dev
user@raspberry:~$ sudo pip3 install docker-compose
```

###### rasberry os env config (ros2 dashing full env container install)

```console
user@raspberry:~$ docker pull isrlab/ros2_dashing_rpi:full
```

###### more docs

[virtual robotics repository](https://github.com/mdegree-nedas/intelligent_systems_and_robotics_lab-virtual-proj/tree/master/docs)
