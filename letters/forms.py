from django import forms
from .models import IncomingLetter, OutgoingLetter
from jalali_date.widgets import AdminJalaliDateWidget

class IncomingLetterForm(forms.ModelForm):
    class Meta:
        model = IncomingLetter
        fields = ['subject', 'document']

class OutgoingLetterForm(forms.ModelForm):
    class Meta:
        model = OutgoingLetter
        fields = ['subject', 'document']


class IncomingLetterAdminForm(forms.ModelForm):
    sent_date = forms.DateField(
        widget=AdminJalaliDateWidget(),
        label="تاریخ نامه وارده",
        required=True  # Set to True if it's a required field
    )

    class Meta:
        model = IncomingLetter
        fields = '__all__'

class OutgoingLetterAdminForm(forms.ModelForm):
    received_date = forms.DateField(
        widget=AdminJalaliDateWidget(),
        label="تاریخ نامه صادره",
        required=False  # Set to True if it's a required field
    )

    class Meta:
        model = OutgoingLetter
        fields = '__all__'

