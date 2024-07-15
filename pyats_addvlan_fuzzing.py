import atheris
import sys
from pyats import aetest
from pyats.topology import loader

class AddVlanToTrunk(aetest.Testcase):
    @aetest.setup
    def setup(self, testbed):
        self.testbed = loader.load(testbed)
        self.device = self.testbed.devices['switch']
        self.device.connect()

    @aetest.test
    def add_vlan(self, vlan_id, interface_name):
        try:
            # Add the VLAN to the trunk interface
            self.device.configure(f'''
                interface {interface_name}
                switchport
                switchport mode trunk
                switchport trunk allowed vlan add {vlan_id}
            ''')
        except Exception as e:
            self.failed(f'Failed to configure VLAN {vlan_id} on interface {interface_name}: {str(e)}')

    @aetest.test
    def verify_vlan(self, vlan_id, interface_name):
        try:
            # Verify the VLAN is added to the trunk interface
            output = self.device.execute(f'show interface {interface_name} switchport')
            if f'Trunking VLANs Enabled: {vlan_id}' in output:
                self.passed(f'VLAN {vlan_id} successfully added to trunk interface {interface_name}')
            else:
                self.failed(f'Failed to add VLAN {vlan_id} to trunk interface {interface_name}')
        except Exception as e:
            self.failed(f'Failed to verify VLAN {vlan_id} on interface {interface_name}: {str(e)}')

    @aetest.cleanup
    def cleanup(self):
        self.device.disconnect()

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)
    vlan_id = fdp.ConsumeIntInRange(1, 4094)  # Valid VLAN range
    interface_name = fdp.ConsumeUnicodeNoSurrogates(20)  # Random interface name
    testbed = "testbed.yaml"

    add_vlan_to_trunk = AddVlanToTrunk()
    add_vlan_to_trunk.setup(testbed)
    add_vlan_to_trunk.add_vlan(vlan_id, interface_name)
    add_vlan_to_trunk.verify_vlan(vlan_id, interface_name)
    add_vlan_to_trunk.cleanup()

def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()

if __name__ == '__main__':
    main()
