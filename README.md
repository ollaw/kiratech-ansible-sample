[![Build Status](https://travis-ci.org/ollaw/kiratech-ansible-sample.svg?branch=master)](https://travis-ci.org/ollaw/kiratech-ansible-sample)

# kiratech-ansible-sample

### Run the playbook 

This project uses *vagrant* to create VM(s). <br>
To run the playbook, creates the VMs typing from the root of the project

- ``` vagrant up ```

and then start the provisioning moving into `\ansible` directory and typing 

- ``` ansible-playbook -i invetory.yml site.yml ```

### What this Playbook does:

1. Ping the machine;
2. Install *docker*;
3. Configure *docker* to expose REST API;
4. Secure REST API (following [this guide](https://docs.docker.com/engine/security/https/));
4. Configure a *docker-swarm* on the two VMs created.

### TODO List on Playbook:

1. Resize partition used by docker if is smaller than 40GB;
2. Test a service with `molecule`

#### Additional notes

- Network address of the VMs are
	- `192.168.2.10` *(master in swarm)*
	- `192.168.2.11` *(worker swarm)*

- To test a REST endpoint on one of the VMs (e.g. `192.168.2.10`), run 

	```curl https://192.168.2.10:2376/images/json --cert client_tls/client-cert.pem --key client_tls/client-key.pem --cacert client_tls/ca.pem ```

