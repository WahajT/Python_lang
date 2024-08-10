

def CheckFrequence(givenWord,Setence):
    count=0
    for i in Setence:
      if givenWord==i:
         count=count+1
         print(count)


Setence= "Me my self and I and me me ME"
CheckFrequence('M',Setence)