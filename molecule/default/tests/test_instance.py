import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('instance')


def test_ood_portal_conf(host):
    ood_portal_conf = '/opt/rh/httpd24/root/etc/httpd/conf.d/ood-portal.conf'
    header = '# Ansible managed:'
    assert host.file(ood_portal_conf).contains(header)


def test_rnode_config(host):
    ood_portal_yml = '/etc/ood/config/ood_portal.yml'
    assert host.file(ood_portal_yml).contains('rnode_uri: /myrnode')
