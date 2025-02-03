import string
from linkedQFile import LinkedQ
import os

def makechildrenv1(word, wordlist):
    '''Kör igenom och kollar efter barn på naivt sätt'''
    gamla = []
    for i in range(len(word)):
        word_as_list = list(word)
        for letter in string.ascii_lowercase:
            word_as_list[i] = letter
            switched = "".join(word_as_list)
            if switched in wordlist:
                if switched not in gamla and switched != word:
                    gamla.append(switched)
                    print(switched)
def makechildren(word, q:LinkedQ, buckets,  target, seen):
    '''Söker igenom med breddenförstsökning (lägger till varje barn till noden i kön)'''
    for bucket in get_buckets(word):
        for node in buckets[bucket]:
            if node not in seen:
                if node == target:
                    print("Det finns en väg till", target)
                    exit(0)
                q.enqueue(node)
                seen[node] = None
    return (q, seen)
            

def get_word_list():
    '''Tar fram listan med ord'''
    wordlist = []
    with open('word3.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for word in line.split(' '):
                word = word.strip()
                wordlist.append(word)
    return wordlist
def get_buckets(word):
    '''Tar fram vilka buckets ordet tillhör'''
    buckets = []
    for i in range(len(word)):
        word_as_list = list(word)
        word_as_list[i] = '_'
        buckets.append("".join(word_as_list))
    return buckets

def ver1():
    '''Första verisionen, kollar alla barn av söt'''
    wordlist = get_word_list()
    makechildrenv1('söt', wordlist)


def ver2():
    '''Andra verisionen av sökningen, använder sig av buckets såsom i boken'''
    start = input("Startord: ")
    target = input("Slutord: ")
    buckets = {}
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    with open('word3.txt', 'r', encoding='utf-8') as file:
        for line in file.readlines():
            for word in line.split(' '):
                word = word.strip()
                for bucket in get_buckets(word):
                    if bucket in buckets:
                        buckets[bucket].append(word)
                    else:
                        buckets[bucket] = [word]
    q = LinkedQ()
    q.enqueue(start)
    seen = {}
    while not q.isEmpty():
        #Breddenförstsökning mha kö
        node = q.dequeue()
        q, seen = makechildren(node, q, buckets, target, seen)

if __name__ == '__main__':
    ver2()  