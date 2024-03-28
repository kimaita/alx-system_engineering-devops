# Configuration management

Configuration management (CM) refers to the process of systematically handling changes to a system in a way that it maintains integrity over time.  
In this, **automation** plays an essential role as it’s the mechanism used to make the server reach a desirable state which is defined by provisioning scripts, written in a tool’s specific language and features.  
Another common term used to describe the automation features implemented by configuration management tools is **Server Orchestration** or **IT Orchestration**, since these tools are typically capable of managing one to hundreds of servers from a central controller machine.

There are a number of configuration management tools available in the market like Puppet, Ansible, Chef and Salt.

## Puppet

A popular CM tool capable of managing complex infrastructure using a master server to orchestrate the configuration of the nodes.
Features:

- Custom DSL based on Ruby
- Puppet Master synchronizes configuration on Puppet Nodes
- Requires specialized software for nodes
- Provides centralized point of control via Puppet Master.
- Non-sequential task execurion order.
