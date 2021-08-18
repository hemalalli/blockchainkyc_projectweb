f = open('C:/Users/Downloads/hempdataoutput.txt', "r")
o = open('C:/Users/Downloads/hempdata.txt', "w+")

matchstring = "0186F0"
replacestring = "00C6F0"


def HexToByte(hexStr):

    bytess = []
    sum = 0
    hexStr = ''.join(hexStr.split(" "))

    for i in range(0, len(hexStr), 2):
        bytess.append(int(hexStr[i:i + 2], 16))
    
    
    for i in range(0, len(bytess)):    
        sum = sum + bytess[i];    
    #print(sum)
    hems = hex((sum^0xff)&0xFF)[2:].upper()
    print("Printing HEX with 0Xff")
    print(hems)

    return(hems)


for x in f:
  print(x)
  first,middle,last = x[:4],x[4:10],x[10:]
  ch = x[2:42]
  cs = HexToByte(ch)
  #print(cs)
 
  #print(middle)
  if middle == matchstring:
        
        matchstring = str('{:06X}'.format(int(matchstring,16) + 16))
        #print(matchstring)
        newvalue = str(first + replacestring + last)
        nn = newvalue[:-3]
        n = nn + cs
        o.write(n + "\n")
        replacestring = str('{:06X}'.format(int(replacestring,16) + 16))
        print(n)
        
