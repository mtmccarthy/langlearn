import Constants
from Types import *
from typing import Tuple


"""
In Chapter 1, Figure 1.3, we learned that devices must register with the kernel in order get a file.
In a typical operating system this would have side effect by adding a new file in the device layer(/dev/*)
"""
def register_device(kernel: KernelType, device: DeviceDriverType) -> FileType:
    return _create_file("/dev/" + _generate_device_name(kernel, device))


"""
In Chapter 1, Figure 1.3, we learned that the kernel associates a file descriptor when a program attempts to open
a file (remember everything is a file, so this can be any resource)
"""
def open_file(kernel: KernelType, path: str) -> FileDescriptorType:
    current_fd_table = _get_fd_table(kernel)  # Kernel retrieves the fd table of this process
    new_fd = _allocate_fd(kernel, current_fd_table)  # Kernel allocates space for a new file descriptor
    _insert_fd(kernel, current_fd_table, new_fd)  # Kernel adds device to process fd table and updates -
    # the system fd table and file system
    return new_fd

"""
Generates a device name from a device driver
"""
def _generate_device_name(kernel: KernelType, dev: DeviceDriverType):
    return ""  # Not a necessary implementation

"""
Create a file at the given file location
"""
def _create_file(path: str) -> FileType:
    # Kernel creates file as a side effect
    return FileType(path)

"""
Retrieves the current FileDescriptorTable in the given process
"""
def _get_fd_table(kernel: KernelType) -> FileDescriptorTableType:
    return {FileDescriptorType(0): FileType("")}  # Unnecessary to implement


"""
Kernel allocates a new file descriptor for later insertion into the given table
"""
def _allocate_fd(kernel: KernelType, table: FileDescriptorTableType) -> FileDescriptorType:
    return 0  # Unnecessary to implement


"""
Kernel inserts the given fd into the given fd table
"""
def _insert_fd(kernel: KernelType, table: FileDescriptorTableType, fd: FileDescriptorType) -> FileDescriptorTableType:
    return {FileDescriptorType(0): FileType("")}  # Unnecessary to implement


def main():
    pass

if __name__ == "__main__":
    main()