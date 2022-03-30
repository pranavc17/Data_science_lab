import filecmp
f1=input("enter the first file name : ")
f2=input("enter the second file name : ")
result=filecmp.cmp(f1,f2)
print(result)
result=filecmp.cmp(f1,f2,shallow="false")
print(result)
