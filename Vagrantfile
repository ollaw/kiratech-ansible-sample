Vagrant.configure("2") do |config|

  config.vm.box = "centos/7"
  config.ssh.insert_key = false

  config.vm.define "vm-master" do |master|
    master.vm.hostname ="vmMaster"
    master.vm.network :private_network, ip: "192.168.2.10"
  end

  config.vm.define "vm-worker" do |worker|
    worker.vm.hostname ="vmWorker"
    worker.vm.network :private_network, ip: "192.168.2.11"
  end
  
end
