def string_change(mstr):
	new=""
	length=len(mstr)
	for i in range(length):
        	if(mstr[i].islower()):
        		new=new+mstr[i].upper()
		elif(mstr[i].isupper()):
                	new=new+mstr[i].lower()
		elif(m_str[i].isdigit()):
                	new+= m_str[i]
               	elif(m_str[i].isdigit()):
                	new = ""
               	else:
                	new+= m_str[i]
        return new

def list(ml):
        nlist=[]
        length=len(ml)
        for i in range(length):
                nE = string_change(ml[i])
                nlist.append(nE)
        return nlist
def main():
        size = 1
        mstr = []
        for i in range(size):
                mstr.append(input("enter string: "))
        print("original string: ")
        print(mstr)
        nlist = change(mstr)
        print("new string: ")
        print(nlist)
main()
