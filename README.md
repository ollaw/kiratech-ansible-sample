[![Build Status](https://travis-ci.org/ollaw/kiratech-ansible-sample.svg?branch=master)](https://travis-ci.org/ollaw/kiratech-ansible-sample)

# kiratech-ansible-sample

# Overview

Purpose of this project is to test some of [ansible](https://www.ansible.com/) basic functionalities, writing a playbook with following requirements:

- Provision two CentOS VMs;
- Partition used by `docker` must have at least 40 GB of available space;
- Configure REST API of `docker` daemon in a secure way;
- `docker` has to be a service that load on startup;
- Configure a `docker-swarm` on the VMs, accessible in a secure way;
- Be able to interact or deploy services on the swarm from the local machine.

---

# Run the project

To create the VMs is used [vagrant](https://www.vagrantup.com/), so from the root of the project typing `vagrant up` is enough to build both VMs.

To start the provisioning, move to `\ansible` and type `ansible-playbook -i invetory.yml site.yml`.

# Testing

For the testing is used [molecule](https://molecule.readthedocs.io/en/stable/). To perform a test, is enough to move on the selected role directory (for example `\secure-api`) and then typing `molecule test`.

Following `roles` contains at least one test :

- `secure-api`

---

## Not implemented yet

- Resize partition used by docker if is smaller than 40GB;

---

## Additional notes

Network address of the VMs are

- `192.168.2.10` _(master in swarm)_
- `192.168.2.11` _(worker swarm)_

REST endpoint are available on both machines, typing `curl https://192.168.2.10:2376/images/json --cert client_tls/client-cert.pem --key client_tls/client-key.pem --cacert client_tls/ca.pem ` (on machine `192.168.2.10` in this example)

Security part has been developed following [this tutorial](https://docs.docker.com/engine/security/https/).
