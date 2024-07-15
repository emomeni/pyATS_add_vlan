from pyats import aetest
from pyats.topology import loader
from genie.libs.conf.interface import Interface

class AddVlanToTrunk(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['switch']
        self.device.connect()

    @aetest.test
    def add_vlan(self):
        vlan_id = 10
        interface_name = 'GigabitEthernet0/1'
        trunk_interface = Interface(name=interface_name, device=self.device)
        
        # Add the VLAN to the trunk interface
        trunk_interface.build_config(apply=False)
        self.device.configure(f'''
            interface {interface_name}
            switchport mode trunk
            switchport trunk allowed vlan add {vlan_id}
        ''')

    @aetest.test
    def verify_vlan(self):
        vlan_id = 10
        interface_name = 'GigabitEthernet0/1'
        
        # Verify the VLAN is added to the trunk interface
        output = self.device.execute(f'show interfaces {interface_name} switchport')
        if f'Trunking VLANs Enabled: {vlan_id}' in output:
            self.passed(f'VLAN {vlan_id} successfully added to trunk interface {interface_name}')
        else:
            self.failed(f'Failed to add VLAN {vlan_id} to trunk interface {interface_name}')

    @aetest.cleanup
    def cleanup(self):
        self.device.disconnect()

if __name__ == '__main__':
    import argparse
    from pyats import topology

    parser = argparse.ArgumentParser()
    parser.add_argument('--testbed', dest='testbed', type=topology.loader.load, required=True)
    args, unknown = parser.parse_known_args()
    
    aetest.main(testbed=args.testbed)
