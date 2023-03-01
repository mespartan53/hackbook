import partition
import downloadKali
import createusb as cu

partition.create_two_partitions()
downloadKali.download_kali()
cu.create_bootable_usb("/Users/admin/downloads/kali.iso", "/dev/disk2s2")