'''8. Decode the message:
A message containing the letters from A-Z can be encoded into the numbers using the mapping 
A-> 1, B-> 2, C-> 3, ..., Z-> 26. To decode an encoded message, you need to group the digits 
and do the reverse mapping. You are required to display all the possible decoded messages. 
For example: "11106" can be decoded into:
a. "AAJF" with the grouping (1 1 10 6)
b. "KJF" with the grouping (11 10 6)'''
class decoder:
    
    def __init__(self,msg):
        self.msg=msg
    
    def decode_help(self,index,cur,result):
        if index==len(self.msg):
            result.append("".join(cur))
            return
        
        #for single digit:
        num1=int(self.msg[index])
        if 1<=num1<=9:
            self.decode_help(index+1,cur+[chr(num1+64)],result)
            
        if index+1<len(self.msg):
            num2=int(self.msg[index:index + 2])
            # for double digit:
            if 10 <= num2 <= 26:
                self.decode_help(index+2,cur+[chr(num2+64),result])

    def decode(self):
        result=[]
        if self.msg:
            self.decode_help(0,[],result)
        return result        

msg=int(input("Enter the message ypu want to decode: "))
decoder=decoder(msg)
decoded_msg=decoder.decode()
for i in decoded_msg:
    print(i)
