# Python program to Decode Sugarloaf error messages

while True:
    # 10/11/2019 06:41:28,Error Code,7169,
    num = int(input("Enter error code seen on server: "))

    errorCode = (0xFF00 & num) >> 8
    errorParam = (0x00FF & num)

    print(f"\nError Code = {errorCode} (cERR_{errorCode}) \nError Parameter = {errorParam} \n")
