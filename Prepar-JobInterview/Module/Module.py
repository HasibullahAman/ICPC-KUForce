import platform
import willImort_module
# by using this code we access to our OS!
Os = platform.system()
# print(Os)

x = dir('libc_ver')
print(x)

# car2 = willImort_module.Vehicle()
companyName = willImort_module.CompanyName
carList = willImort_module.myCar()