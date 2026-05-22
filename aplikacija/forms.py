from django import forms

class ClanstvoForm(forms.Form):
    VRSTE_CLANSTVA = [
        ('', 'Odaberite vrstu članstva'),
        ('redovna', 'Vrsta članstva redovna'),
        ('premium', 'Vrsta članstva premium'),
    ]

    name = forms.CharField(
        label="Ime i prezime",
        widget=forms.TextInput(attrs={'placeholder': 'Vaše ime i prezime', 'class': 'form-input'})
    )
    email = forms.EmailField(
        label="Email adresa",
        widget=forms.EmailInput(attrs={'placeholder': 'vas.email@primjer.com', 'class': 'form-input'})
    )
    phone = forms.CharField(
        label="Telefon",
        widget=forms.TextInput(attrs={'placeholder': '+385 99 123 4567', 'class': 'form-input'})
    )
    dob = forms.DateField(
        label="Datum rođenja",
        widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-input'})
    )
    address = forms.CharField(
        label="Adresa",
        widget=forms.TextInput(attrs={'placeholder': 'Ulica i broj, Grad, Poštanski broj', 'class': 'form-input'})
    )
    membership = forms.ChoiceField(
        label="Vrsta članstva",
        choices=VRSTE_CLANSTVA,
        widget=forms.Select(attrs={'class': 'form-input'})
    )
    message = forms.CharField(
        label="Dodatna poruka (opcionalno)",
        required=False,
        widget=forms.Textarea(attrs={'rows': 4, 'placeholder': 'Želite li nam nešto dodatno poručiti?', 'class': 'form-input'})
    )


  

class KontaktForm(forms.Form):
    name = forms.CharField(label="Ime i prezime", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Vaše ime i prezime'}))
    email = forms.EmailField(label="E-mail", widget=forms.EmailInput(attrs={'class': 'form-input', 'placeholder': 'ime@primjer.hr'}))
    phone = forms.CharField(label="Telefon", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': '+385 91 123 4567'}))
    subject = forms.CharField(label="Naslov", widget=forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Kratak naslov poruke'}))
    message = forms.CharField(label="Poruka", widget=forms.Textarea(attrs={'class': 'form-input', 'placeholder': 'Napišite svoju poruku...', 'rows': 5}))