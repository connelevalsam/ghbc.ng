from django.shortcuts import render


def home_view(request):
    return render(request, 'index.html')


def media_view(request):
    return render(request, 'media.html')


def give_view(request):
    return render(request, 'give.html')


def kids_view(request):
    return render(request, 'kids.html')


def store_view(request):
    return render(request, 'store.html')


def what_to_expect_view(request):
    return render(request, 'what-to-expect.html')


def who_we_are_view(request):
    return render(request, 'who-we-are.html')

def contact(request):
    return render(request, 'contact.html')

# messages
def msg1(request):
    return render(request, 'message01.html')

def msg2(request):
    return render(request, 'message02.html')

def msg3(request):
    return render(request, 'message03.html')

def msg4(request):
    return render(request, 'message04.html')

# kids messages
def kids_msg1(request):
    return render(request, 'kids_msg1.html')

def kids_msg2(request):
    return render(request, 'kids_msg2.html')

def kids_msg3(request):
    return render(request, 'kids_msg3.html')

def kids_msg4(request):
    return render(request, 'kids_msg4.html')

def kids_stry1(request):
    return render(request, 'kids_stry1.html')

def kids_stry2(request):
    return render(request, 'kids_stry2.html')

def kids_stry3(request):
    return render(request, 'kids_stry3.html')

def kids_stry4(request):
    return render(request, 'kids_stry4.html')

def privacy(request):
    return render(request, 'privacy-policy.html')

def coming_soon(request):
    return render(request, 'comingsoon.html')
