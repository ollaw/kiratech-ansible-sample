Vagrant.configure("2") do |config|

  worker.vm.box = "centos/7"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/site.yml"
  end

  config.vm.define "vm-master" do |master|
    master.vm.hostname ="vm-master"
    config.vm.network :private_network, ip: "192.168.2.10"
  end

  config.vm.define "vm-worker" do |worker|
    worker.vm.hostname ="vm1"
    config.vm.network :private_network, ip: "192.168.2.11"
  end
  
end
