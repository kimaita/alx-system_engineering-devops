# Firewall

A firewall is a network security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. A firewall typically establishes a barrier between a trusted network and an untrusted network. Firewalls are categorized as a **network-based** or a **host-based** system. Network-based firewalls are positioned between two or more networks while Host-based firewalls are deployed directly on the host itself to control network traffic or other computing resources.

Traffic into or out of a computer is filtered through "ports," which are relatively arbitrary designations appended to traffic packets destined for use by a particular application. Traffic to particular applications can be allowed or blocked by "opening" or "closing" (i.e. filtering) the ports designated for a particular type of traffic.  This is done by opening and closing TCP and UDP "ports" in the firewall. Additionally, firewalls can be configured to allow or restrict access to specific IP addresses (or IP address ranges).

## UFW

UFW (Uncomplicated Firewall) is a front-end for `iptables` which contains rules for packet filtering and is configured from the terminal. These rules are used by the `netfilter` subsystem which is used to manipulate or decide the fate of network traffic headed into or through your computer (packet filtering). UFW is particularly well-suited for host-based firewalls.
