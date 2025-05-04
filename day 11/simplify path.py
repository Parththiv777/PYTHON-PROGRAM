
class Solution(object):
    def simplifyPath(self, path):
        newlist=[]
        newpath=path.split('/')
        n=len(newpath)
        for i in range(n):
            if newpath[i]=='..' and newlist:
                newlist.pop()
            elif newpath[i]=='..' and not newlist:
                continue
            elif newpath[i]=='.' or newpath[i]=='':
                continue
            else:
                newlist.append(newpath[i])

        return '/'+'/'.join(newlist)
        
