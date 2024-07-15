from hypothesis import given, strategies as st
from pyats import aetest
from pyats.topology import loader
import io

# Assuming the device configuration functions are accessible
def add_vlan(device, vlan_id, interface_name):
    config_commands = f'''
        interface {interface_name}
        switchport mode trunk
        switchport trunk allowed vlan add {vlan_id}
    '''
    device.configure(config_commands)

def verify_vlan(device, vlan_id, interface_name):
    output = device.execute(f'show interfaces {interface_name} switchport')
    return f'Trunking VLANs Enabled: {vlan_id}' in output

@given(vlan_id=st.integers(min_value=1, max_value=4095), interface_name=st.text())
def test_add_vlan(vlan_id, interface_name):
    # Replace with actual testbed loading and device connection
    testbed = loader.load('testbed.yaml')
    device = testbed.devices['switch']
    device.connect()
    
    # Run fuzzing
    add_vlan(device, vlan_id, interface_name)
    assert verify_vlan(device, vlan_id, interface_name)
    
    device.disconnect()
