from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from ..models import Tier, Perk, Hackathon, Sponsorship
from ..forms import TierForm, PerkForm, HackathonForm, SponsorshipForm

def hackathons(request):
    hackathons = Hackathon.objects.all()
    return render(request, "hackathons.html", {"hackathons": hackathons})

def hackathon_detail(request, h_pk):
    hackathon = get_object_or_404(Hackathon, pk=h_pk)
    return render(request, "hackathon_detail.html", {"hackathon": hackathon})

def hackathon_new(request):
    if request.method == "POST":
        form = HackathonForm(request.POST)
        if form.is_valid():
            hackathon = form.save(commit=False)
            hackathon.save()
            return redirect("hackathons:index")
    else:
        form = HackathonForm()
    return render(request, "hackathon_new.html", {"form": form})


def hackathon_edit(request, h_pk):
    hackathon = get_object_or_404(Hackathon, pk=h_pk)
    if request.method == "POST":
        form = HackathonForm(request.POST, instance=hackathon)
        if form.is_valid():
            hackathon = form.save(commit=False)
            hackathon.save()
            return redirect("hackathons:index")
    else:
        form = HackathonForm(instance=hackathon)
    return render(request, "hackathon_edit.html", {"form": form})

