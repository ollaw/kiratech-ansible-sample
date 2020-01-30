[![Build Status](https://travis-ci.org/ollaw/kiratech-ansible-sample.svg?branch=master)](https://travis-ci.org/ollaw/kiratech-ansible-sample)

# kiratech-ansible-sample

### Run the playbook 

This project uses *vagrant* to create VM(s). <br>
To run the playbook, creates the VMs typing from the root of the project

- ``` vagrant up ```

and then start the provisioning moving into `\ansible` directory and typing 

- ``` ansible-playbook -i invetory.yml site.yml ```

### What this Playbook do

1. Ping the machine (simple test);
2. Install *docker*;
3. Configure *docker* to expose (in insecure mode yet) REST API;
4. Configure a *docker-swarm* on the two VMs created (not fully working yet).

### TODO List on Playbook

1. Resize partition used by docker if is smaller than 40GB;
2. Expose REST API in a secure mode;

#### Additional notes
Network address of the VM (to test REST API) is `192.168.2.10` (specified on `Vagrantfile`)
