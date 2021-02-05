from django.shortcuts import render

# Create your views here.
def profile(request):
    ''' diplay users profile ''' 

    template = 'profiles/profile.html'
    context = {}

    return render(request, template, context)
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
