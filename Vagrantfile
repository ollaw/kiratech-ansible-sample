Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.hostname ="vm1"
  config.vm.network :private_network, ip: "192.168.2.10"
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/site.yml"
  end
end
