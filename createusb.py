import sys
import subprocess
import os

def create_bootable_usb(iso_file, usb_drive):
	#Unmount the USB drive
	subprocess.call(["diskutil","unmountDisk",usb_drive])

	#Write the ISO image to the USB drive
	print("Writing ISO image to drive")
	subprocess.call(["sudo","dd","if="+iso_file,"of="+usb_drive,"bs=4m"])
	print("Kali has been loaded and is now bootable")

	# Mount the USB drive
	usb_drive2 = "/dev/disk2s3"
	mount_point = "/Volumes/FILES/"
	subprocess.run(["diskutil", "mount", usb_drive2])

	# Copy the additional file to the USB drive
	additional_file = "/Users/admin/Desktop/Scripts/parttwo.py" # we need to adjust this
	os.system(f"cp {additional_file} {mount_point}")
	print("Additional files are ready for Kali")

	# Unmount the USB drive again
	subprocess.run(["diskutil", "unmount", usb_drive2])

	print("Please restart and boot to Kali. Hold option when the device starts up")


#probably make arg 1 constant and just figure out arg 2 with diskutil list
#create_bootable_usb("/Users/admin/downloads/kali.iso", "/dev/disk2")