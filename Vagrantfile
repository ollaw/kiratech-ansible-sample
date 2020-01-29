Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.ssh.insert_key = false

  #config.vm.provision :ansible do |ansible|
  #  ansible.playbook = "provisioning/site.yml"
  #end

  config.vm.define "vm-master" do |master|
    master.vm.hostname ="vm-master"
    config.vm.network :private_network, ip: "192.168.2.10"
  end

  config.vm.define "vm-worker" do |worker|
    worker.vm.hostname ="vm-worker"
    config.vm.network :private_network, ip: "192.168.2.11"
  end
  
end
