from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, "home.html")
def count(request):
    textname=request.GET['textname']
    wordlist=textname.split()
    word_dict={}
    for word in wordlist:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1
    sortedwords=sorted(word_dict.items(), key=operator.itemgetter(1), reverse=True)
    return render(request, "count.html", {"textname":textname, "sortedwords":sortedwords, "count":len(wordlist), "word_dict":word_dict, "worddictionary":sortedwords })
def about(request):
    return render(request, "about.html")
