Vagrant.configure("2") do |config|
  config.vm.box = "centos/7"
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisioning/playbook.yml"
  end
end
