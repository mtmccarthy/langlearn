from typing import NewType, Dict

"""
In Chapter 1, we learned that 'Everything is a File!'. Here we've created a new type, 'FileType' which models a file
as its path in the filesystem.
"""
FileType = NewType('FileType', str)

"""
In Chapter 1, we learned about FileDescriptors, which are essentially integer indexes into a table
stored by the kernel called the file descriptor table (shocking!)
Since a file descriptor is essentially just an integer, we can model it as such.
"""
FileDescriptorType = NewType('FileDescriptorType', int)

"""
We can model the table as a dictionary with key file descriptor and value file.

The fd table is generated for every process and holds a pointer to the system fd table, but the model still holds up.
"""
FileDescriptorTableType = Dict[FileDescriptorType, FileType]

"""
In Chapter 1, we learned about Device Drivers are software which provide an abstraction between the kernel and
external devices such as a keyboard, mouse, monitor etc.
"""
DeviceDriverType = NewType('DeviceDriverType', None)

"""
Programs are files that can also be executed. We can model that like this:
"""
ProgramType = NewType('ProgramType', FileType)

"""
In Chapter 1, the kernel was mentioned. The kernel is essentially a program executed when the system boots.
The kernel is responsible for processing low level system calls, examples include input/output and memory management.

Since the kernel is just a special type of program, we can model it like this:
"""
KernelType = NewType('KernelType', ProgramType)
