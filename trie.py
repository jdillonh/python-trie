
class trieNode:
    def __init__(self, letter, isEnd):
        self.letter = letter
        self.isEnd = isEnd
        self.children = []

    def __str__(self):
        return self.letter + ' trieNode object'

    def childrenHave(self, l):
        for child in self.children:
            if child.letter == l:
                return True, child
        return False, None


class trie:
    def __init__(self):
        self.head = []

    def add(self, word):
        """adds a word (string or char list) to the the trie"""
        if len(word) == 0:
            raise Exception("Cannot add empty object")

        curr = None
        for node in self.head:
            if node.letter == word[0]:
                curr = node
                break
        if curr == None:
            new = trieNode(word[0], False)
            self.head.append(new)
            curr = new

        if len(word) == 1:
            curr.isEnd = True
            return
        else:
            word = word[1:]
        
        for letter in word:
            has_it, child = curr.childrenHave(letter)
            if has_it:
                curr = child
            else:
                newNode = trieNode(letter, False)
                curr.children.append(newNode)
                curr = newNode
        curr.isEnd = True

    def contains(self, word):
        """checks whether a word is in the trie"""
        if len(word) == 0:
            raise Exception("Trie cannot contain empty object")

        has_first = False
        for node in self.head:
            if node.letter == word[0]:
                curr = node
                if len(word) == 1:
                    return curr.isEnd
                has_first = True
                word = word[1:]
        if not has_first:
            return False

        for letter in word:
            has_it, child = curr.childrenHave(letter)
            if not has_it:
                return False
            curr = child

        if curr.isEnd:
            return True

        return False

                




### Tests 1 ###
# Checking corect object initialization 
myTrie = trie()

# Adding
myTrie.add('hi')
assert(myTrie.head[0].letter == 'h')
assert(myTrie.head[0].isEnd == False)
assert(len(myTrie.head[0].children) == 1)
assert(myTrie.head[0].children[0].letter == 'i')
assert(myTrie.head[0].children[0].isEnd == True)
assert(len(myTrie.head[0].children[0].children) == 0)

myTrie.add('hello')
myTrie.add('500') 
myTrie.add('High')
assert(len(myTrie.head) == 3) #h H 5
assert(myTrie.head[1].letter == '5')
assert(myTrie.head[1].children[0].letter == '0')
assert(myTrie.head[1].children[0].children[0].isEnd == True)
assert(myTrie.head[2].letter == 'H')

myTrie.add('z')
assert(myTrie.head[len(myTrie.head) -1].letter == 'z')
assert(myTrie.head[len(myTrie.head) -1].isEnd == True)

# Finding
assert(myTrie.contains('z'))
assert(myTrie.contains('hi'))
assert(not myTrie.contains('h'))
assert(not myTrie.contains('i'))
assert(myTrie.contains('500'))
assert(not myTrie.contains('50'))
assert(not myTrie.contains('5'))
assert(not myTrie.contains('0'))


### Tests 2 ###
# similar substrings
t2 = trie()

t2.add("Everyday may not be a good day, but there is good in every day")
t2.add("Everyday may not be a good day, ")
t2.add("Everyday may not")
t2.add("Everyday")
t2.add("Every")
#t2.add("Ever")
t2.add("Eve")
t2.add("Ev")
t2.add("E")

assert(t2.contains("Everyday may not be a good day, but there is good in every day"))
assert(t2.contains("Everyday may not be a good day, "))
assert(not t2.contains("Everyday may not be a good day,"))
assert(not t2.contains("Everyday may not be a "))
assert(t2.contains("Everyday may not"))
assert(not t2.contains("Everyday "))
assert(t2.contains("Everyday"))
assert(not t2.contains("Everyda"))
assert(not t2.contains("Everyd"))
assert(t2.contains("Every"))
assert(not t2.contains("Ever"))
assert(t2.contains("Eve"))
assert(t2.contains("Ev"))
assert(t2.contains("E"))


print('Tests Pass')
