INTRODUCTION:
------------

This module contains script files to commission hosts.


REQUIREMENTS:
------------

This module requires the following modules:

 * Python 3
   Libraries
  * requests
  * sys
  * json
  * time

 * The scripts must be run outside sddc-manager environment.

 * DNS resolution must be done for sddc-manager.


PREREQUSITES:
--------------

The following data is required

	Username of each host

	Password of each host

	FQDN of each host

	Network pool name to which each host has to be associated with (Optional)

	Network pool ID to which each host has to be associated with

	TIP
	Refer to: Get the Network Pools and Get a Network of a Network Pool
	The host, if intended to be used for a vSAN domain, should be vSAN compliant and certified as per the VMware Hardware Compatibility Guide.

BIOS, HBA, SSD, HDD, etc. of the host must match the VMware Hardware Compatibility Guide.

The host must have the drivers and firmware versions specified in the VMware Hardware Compatibility Guide.

The host must have the supported version of ESXi (i.e 6.7.0-13006603) pre-installed on it.

SSH and syslog must be enabled on the host.

The host must be configured with DNS server for forward and reverse lookup and FQDN.

The host name must be same as the FQDN.

The host must have a standard switch with two NIC ports with a minimum 10 Gbps speed.

The management IP must be configured to the first NIC port.

Ensure that the host has a standard switch and the default uplinks with 10Gb speed are configured starting with traditional numbering (e.g., vmnic0) and increasing sequentially.

Ensure that the host hardware health status is healthy without any errors.

All disk partitions on HDD / SSD are deleted.

The hosts, if intended to be used for vSAN domain must be associated with vSAN enabled network pool.

The hosts, if intended to be used for NFS domain must be associated with NFS enabled network pool.


USAGE:
-----
Sample specification file "commission_hosts_spec.json" will be used for commission host operation. So fill the required details and validate before executing the script.
For more information on the provided sample file, please refer to API reference documentation.

Usage:	python commission_hosts.py <hostname> <username> <password>

commission_hosts_spec.json is the sample spec file

