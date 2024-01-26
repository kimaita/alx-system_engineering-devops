# Processes and signals

This project gets into Linux processes and signals, covering tasks like viewing running processes, getting process IDs and killing processes.

A process is a running instance of a program. Each process has its own unique process identification number(PID) through which it is identified in the system. PIDs are non-negative integers.

Running processes can be viewed using the `ps`, `pstree`, or `top` commands.
- `ps` shows the PIDs for the processes currently on the system
- `pstree` shows the process names and PIDs in a tree diagram
- `top` displays running process info continuously - in realtime.  

For a specific program, one can use `pidof` to get all its PIDs.

A signal is a software interrupt, practically an integer, providing a means for communicatoon with processes. A process receiving a signal can execute a defined routine for that signal or otherwise the system executes the default signal handler. A signal is sent with the `kill` command. Available signals can viewed by running `man signal` 