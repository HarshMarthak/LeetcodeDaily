#my solution

class WordFilter:

    def __init__(self, words: List[str]):
        self.d={}
        for i,w in enumerate(words):
            l=len(w)
            for p in range(1,min(10,l)+1):
                for s in range(1,min(10,l)+1):
                    self.d[w[:p],w[-s:]]=i

    def f(self, prefix: str, suffix: str) -> int:
        return self.d[prefix, suffix] if (prefix, suffix) in self.d else -1

#better solution

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.words = set()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word, idx):

        node = self.root
        for ch in word:
            node = node.child[ch]
            node.words.add(idx)



class WordFilter:

    def __init__(self, words: List[str]):
        self.trie_pre = Trie()
        self.trie_post = Trie()
        memo = dict()
        for i in range(len(words)):
            memo[words[i]] = i

        for word, i in memo.items():
            self.trie_pre.insert(word, i)
            self.trie_post.insert(word[::-1], i)



    def f(self, prefix: str, suffix: str) -> int:
        node_pre = self.trie_pre.root
        node_post = self.trie_post.root
        for ch in prefix:
            if ch not in node_pre.child:
                return -1
            node_pre = node_pre.child[ch]
        pre_list = node_pre.words

        for ch in suffix[::-1]:
            if ch not in node_post.child:
                return -1
            node_post = node_post.child[ch]
        post_list = node_post.words
        overlap = pre_list.intersection(post_list)

        if len(overlap) == 0:
            return -1
        return max(overlap)
