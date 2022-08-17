class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        s=set()
        symbols=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        for word in words:
            transformation=""
            for letter in word:
                transformation+=symbols[ord(letter)-97]
            s.add(transformation)
        return len(s)
