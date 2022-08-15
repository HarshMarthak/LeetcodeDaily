class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        gcd = math.gcd(p,q)
        top = q // gcd
        side = p // gcd        
        if top % 2:
            return 1 if side % 2 else 2 
        else:
            return 0      