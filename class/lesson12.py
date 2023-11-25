
class area:

    def Area(self,lenth=None,height=None):

        ans=0
        print(lenth)
        print(height)

        if ( height==None and lenth==None):
            ans=0

        elif(height == None):
            # print("no height ")

            ans=lenth*lenth
        else:
            ans=height*lenth
            # print(" height avalible ")
        return ans


A1=area()

ans=A1.Area(10,20)

print(ans)
