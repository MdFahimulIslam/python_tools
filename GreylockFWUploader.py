"""
1. After successful build rename the *.hex file to *.img file
2. Create sha of that file and save in *.hsh format
3. Try to save that file in drive name: "FIRMWARE".
4. Wait for 2 minutes until that drive is found.
"""

f = open("Test.txt")
print(f.read())
