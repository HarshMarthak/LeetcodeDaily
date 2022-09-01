class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for letter in ransomNote:
            if magazine.find(letter) != -1:
                magazine = magazine.replace(letter, "", 1)
            else:
                return False
        return True
