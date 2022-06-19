#my solution

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ans=[]
        products.sort()
        for i in range(1,len(searchWord)+1):
            temp=[]
            count=0
            for word in products:
                if searchWord[:i] == word[:i] and count<3:
                    temp.append(word)
                    count+=1
            ans.append(temp)
        return ans


#better Solution

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, cur = [], ''
        for c in searchWord:
            cur += c
            i = bisect.bisect_left(products, cur)
            res.append([w for w in products[i:i+3] if w.startswith(cur)])
        return res
