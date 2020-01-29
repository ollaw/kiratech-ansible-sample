[![Build Status](https://travis-ci.org/ollaw/kiratech-ansible-sample.svg?branch=master)](https://travis-ci.org/ollaw/kiratech-ansible-sample)

# kiratech-ansible-sample

### Run the playbook 

This project uses *vagrant* to create VM(s). <br>
To run the playbook (`provisioning/site.yml`), from the root of the project just type

- ``` vagrant up ```

to start the VM and provision it with given playbook.<br>
If instead the machine is already on, just type

- ``` vagrant provision ```

### What this Playbook do

1. Ping the machine (simple test);
2. Install *docker*;
3. Configure *docker* to expose (in insecure mode yet) REST API.

### TODO List on Playbook

1. Resize partition used by docker if is smaller than 40GB;
1. Expose REST API in a secure mode;
2. Configure *docker-swarm*.

#### Additional notes
Network address of the VM (to test REST API) is `192.168.2.10` (specified on `Vagrantfile`)
