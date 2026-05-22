from django.shortcuts import render, redirect
from django.views import View 
from .forms import ClanstvoForm

# Početna stranica
def pocetna(request):
    return render(request, "aplikacija/pocetna.html")

# Omladinski pogon i klub
def juniori_view(request):
    return render(request, 'aplikacija/juniori.html')

def kadeti_view(request):
    return render(request, 'aplikacija/kadeti.html')

def povijest_kluba(request):
    return render(request, 'aplikacija/povijest.html')

def seniori_view(request):
    return render(request, 'aplikacija/seniori.html')

# Izvještaji i vijesti
def izvjestaj_view(request):
    return render(request, 'aplikacija/izvjestaj.html')

def vijest1_view(request):
    return render(request, 'aplikacija/vijest1.html')

def vijest2_view(request):
    return render(request, 'aplikacija/vijest2.html')

def vijest3_view(request):
    return render(request, 'aplikacija/vijest3.html')

def sponzori_view(request):
    return render(request, 'aplikacija/sponzori.html')


# --- SEKCIJA ZA ČLANSTVO ---

# Pogled za formu članstva
def prijava_clanstvo(request):
    if request.method == 'POST':
        form = ClanstvoForm(request.POST)
        if form.is_valid():
            # 1. Izvlačenje očišćenih podataka iz forme
            ime_prezime = form.cleaned_data['name']
            email = form.cleaned_data['email']
            telefon = form.cleaned_data['phone']
            vrsta_clanstva = form.cleaned_data['membership']
            
            # 2. Ispis u tvoj crni terminal/konzolu za test
            print(f"NOVA PRIJAVA: {ime_prezime} ({email}) - Mob: {telefon} - Paket: {vrsta_clanstva}")
            
            # 3. Preusmjeravanje na stranicu uspjeha
            return redirect('uspjeh')
    else:
        form = ClanstvoForm()

    return render(request, 'aplikacija/clanstvo.html', {'form': form})

# Pogled za stranicu uspjeha (nakon slanja)
def uspjeh_stranica(request):
    return render(request, 'aplikacija/uspjeh.html')