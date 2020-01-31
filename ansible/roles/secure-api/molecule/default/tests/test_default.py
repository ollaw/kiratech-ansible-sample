import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_keys_directory(host):
    key_directory = host.file('/home/vagrant/key_sample')

    assert key_directory.exists
    assert key_directory.is_directory


def test_keys_file_exists(host):
    files_name = ['server-key.pem', 'server-cert.pem', 'ca.pem']
    files_path = map(
        lambda name: "/home/vagrant/key_sample/" + name, files_name)
    for f in [host.file(x) for x in files_path]:
        assert f.exists
        assert f.is_file
        assert f.size > 0
