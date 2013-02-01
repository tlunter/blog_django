from django.shortcuts import render
import feedparser as fp

def about(request):
    return render(request, 'pages/about.html')

def feeds(request):
    so = fp.parse('http://stackoverflow.com/feeds/user/714452')
    so_entries = so.entries[0:5]

    gh = fp.parse('https://github.com/tlunter.atom')
    gh_entries = gh.entries[0:5]

    return render(request, 'pages/feeds.html',
            { 'so_entries': so_entries, 'gh_entries': gh_entries })
