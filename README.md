# PyATS VLAN Trunk Interface Test
[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/emomeni/pyATS_add_vlan)

[![Run in Cisco Cloud IDE](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-runable-icon.svg)](https://developer.cisco.com/codeexchange/devenv/emomeni/pyATS_add_vlan/)

## Overview
This repository contains a PyATS test script to add a VLAN to a trunk interface on a Cisco switch and verify the configuration. The script is designed to automate the process of VLAN configuration on network devices, ensuring that the VLAN is correctly added and operational.

### Integrate fuzzing into your PyATS script for adding a VLAN to a trunk interface
Fuzz testing (or fuzzing) is a software testing technique that involves providing invalid, unexpected, or random data as inputs to a computer program. Fuzzing can help find vulnerabilities and bugs that might not be discovered through regular testing. To integrate fuzzing into your PyATS script for adding a VLAN to a trunk interface, you can use a Python fuzzing library such as Atheris or python-afl.

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
   If necessary, update the VLAN ID and the trunk interface name in the script (`pyats_addvlan.py`):

    ```python
    vlan_id = 10
    interface_name = 'GigabitEthernet0/1'
    ```

## Usage
To run the test script, execute the following command:

```bash
python pyats_addvlan.py --testbed testbed.yaml
 ```

## Script Details
This script will:
1. Connect to the network device defined in the testbed.
2. Add the specified VLAN to the trunk interface.
3. Verify that the VLAN has been successfully added.
4. Disconnect from the device.

## Script Phases
* Setup Phase: Connects to the device using the details provided in the testbed file.
* Test Phase: Adds the specified VLAN to the trunk interface and verifies the configuration.
* Cleanup Phase: Disconnects from the device.

## Explanation of the Fuzzing Integration
* FuzzedDataProvider: This class is used to generate fuzzed inputs for the VLAN ID and the interface name.
* TestOneInput Function: This function is called with fuzzed data, which it then uses to generate VLAN IDs and interface names. It performs the setup, configuration, verification, and cleanup steps using these fuzzed inputs.
* Main Function: This function sets up and starts the fuzzing process using Atheris.

### Considerations
* Valid Ranges and Inputs: The ConsumeIntInRange method ensures that the fuzzed VLAN ID falls within the valid range (1-4094). The interface name is fuzzed to be a random Unicode string.
* Exception Handling: The script includes exception handling to catch and report errors that occur during configuration and verification.
* Resource Management: Ensure that the network devices and test environments are properly managed and that resources are cleaned up after tests.

## Notes
* Ensure you have the necessary permissions to modify the VLAN configurations on the network device.
* Test the script in a controlled environment before deploying it to production.

## License
This project is licensed under the MIT License.
