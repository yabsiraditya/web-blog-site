from django import forms
import datetime


JENIS_KELAMIN = (
    ('p','Pria'),
    ('w','Wanita'),
)

TAHUN = range(1, datetime.date.today().year+1, 1)
today = datetime.date.today()
MONTHYEAR = datetime.date(today.year, today.month, 1)


class KontakForms(forms.Form):
    nama = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control'
            }
        )
    )
    email = forms.EmailField(
        help_text='Masukan Email Anda Dengan Benar.'
    )
    jenkel = forms.ChoiceField(
        widget = forms.RadioSelect(
            attrs= {
                'class':'from-check-input',
            }
        ), 
        choices = JENIS_KELAMIN, 
        label = 'Jenis Kelamin',
    )
    tgl_lahir = forms.DateField(
        initial=MONTHYEAR,
        widget = forms.SelectDateWidget(
            years=TAHUN,
            attrs= {
                'class':'form-select mb-2'
            },
        ),
    )
    pesan = forms.CharField(
        widget=forms.Textarea(
            attrs= {
                'class':'form-control'
            }
        )
    )
    agree = forms.BooleanField()

    email.widget.attrs.update({'class':'form-control',})