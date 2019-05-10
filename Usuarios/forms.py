from django import forms
from .models import Usuario_admin


class RegistroUsuarioForm(forms.Form):

  name = forms.CharField(max_length=200,
                           widget=forms.TextInput(attrs={'class': 'form-control'}),
                           required=True)
  app_paterno = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=True,
                                label='Apelido Paterno')
  app_materno = forms.CharField(max_length=200,
                                widget=forms.TextInput(attrs={'class': 'form-control'}),
                                required=False,
                                label='Apellido Materno')
  password = forms.CharField(max_length=50,
                             widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                             required=True,
                             label='Contraseña')

  def is_valid(self):
      return super(RegistroUsuarioForm, self).is_valid()

  def save(self, *args, **kwargs):
      admin=Usuario_admin(name=self.cleaned_data['name'], app_paterno=self.cleaned_data['app_paterno'],app_materno=self.cleaned_data['app_materno'], password=self.cleaned_data['password'])


      admin.save()
      return admin