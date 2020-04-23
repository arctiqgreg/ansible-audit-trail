Vagrant.configure("2") do |config|
  config.vm.box = "debian/jessie64"
  config.vm.network "private_network", ip: "192.168.33.10"
  config.vm.provision :ansible do |ansible|
    ansible.playbook = "provisionning/playbook.yaml"
    ansible.verbose = "-v"
  end
end