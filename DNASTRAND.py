for _ in range(int(input())):
    n=int(input())
    s=input()
    null=""
    for i in range(n):
        if s[i]=="A":
            null+="T"
        elif s[i]=="T":
            null+="A"
        elif s[i]=="C":
            null+="G"
        elif s[i]=="G":
            null+="C"
    print(null)
            