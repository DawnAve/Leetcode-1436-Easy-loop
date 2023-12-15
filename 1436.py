class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        ans = []
        for i in paths:
            ans.append(i[1])
        for i in paths:
            if i[0] in ans:
                ans.remove(i[0])
        return ans[0]

        
