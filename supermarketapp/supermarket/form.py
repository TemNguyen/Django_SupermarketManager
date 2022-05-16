from cProfile import label
from django import forms
from .models import MatHang, Loai

class MatHangForm(forms.ModelForm):
    name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Tên mặt hàng',
        })
    )

    gia = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Giá của 1 đơn vị'
        })
    )

    stock = forms.IntegerField(
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Số lượng'
        })
    )
    class Meta:
        model = MatHang
        fields = [
            'name',
            'gia',
            'stock',
            'loai'
        ]