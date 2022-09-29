class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        while 'R.' in dominoes or '.L' in dominoes:
            dominoes = dominoes.replace('R.L','xxx').replace('.L','LL').replace('R.','RR')
        return dominoes.replace('xxx','R.L')
