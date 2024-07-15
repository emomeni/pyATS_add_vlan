# PyATS VLAN Trunk Interface Test

## Overview
This repository contains a PyATS test script to add a VLAN to a trunk interface on a Cisco switch and verify the configuration. The script is designed to automate the process of VLAN configuration on network devices, ensuring that the VLAN is correctly added and operational.

## Prerequisites
Before running the script, ensure you have the following:
- Python 3.6+
- Cisco Test Automation Solution (PyATS) and Genie libraries
- Access to the network devices (Cisco switch) with appropriate credentials
- SSH access to the switch

## Installation
1. **Clone the repository**:
    ```bash
    git clone <repository_url>
    cd <repository_directory>
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages**:
    ```bash
    pip install pyats[full]
    pip install genie
    ```

## Configuration
1. **Create a testbed file**:
   Define the network devices in a YAML file (e.g., `testbed.yaml`). Here is an example configuration:

    ```yaml
    testbed:
      name: example_testbed
      devices:
        switch:
          os: ios
          type: switch
          connections:
            cli:
              protocol: ssh
              ip: 192.168.1.1
          credentials:
            default:
              username: your_username
              password: your_password
    ```

    Replace the placeholders with your actual network details (IP addresses, usernames, passwords).

2. **Update the test script**:
   If necessary, update the VLAN ID and the trunk interface name in the script (`test_add_vlan.py`):

    ```python
    vlan_id = 10
    interface_name = 'GigabitEthernet0/1'
    ```

## Usage
To run the test script, execute the following command:

```bash
python test_add_vlan.py --testbed testbed.yaml
 ```

## Script Details
This script will:

1. Connect to the network device defined in the testbed.
2. Add the specified VLAN to the trunk interface.
3. Verify that the VLAN has been successfully added.
4. Disconnect from the device.
