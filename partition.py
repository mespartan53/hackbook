import subprocess

def create_two_partitions():
    #Here the usb will be split into 2 partitions

    device_path = '/dev/disk2'
    print("Getting partition ready")
    #Unmount the drive
    subprocess.run(['diskutil', 'unmountDisk', device_path])

    #create partition layout
    subprocess.run(['diskutil', 'partitionDisk', device_path, '2', 'GPT', 'FAT32', 'KALI', '50G', 'FAT32', 'FILES', '0b'])

    print("partitions created")
    return


