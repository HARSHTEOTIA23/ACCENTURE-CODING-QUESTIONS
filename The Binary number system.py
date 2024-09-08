s=input();
f=ord(s[0])-48;
for i in range(1,len(s),2):
    if s[i]=="A":
        f=f & (ord(s[i+1])-48);
        
    elif s[i]=="B":
        f=f|(ord(s[i+1])-48);
       
    else:
        f=f^(ord(s[i+1])-48);
        
    i=i+2;
print(f);
