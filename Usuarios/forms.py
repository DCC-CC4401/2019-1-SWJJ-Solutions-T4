from django import forms
from .models import Usuario_admin, Usuario_evaluador
from .models import Course


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
        admin = Usuario_admin(name=self.cleaned_data['name'], app_paterno=self.cleaned_data['app_paterno'],
                              app_materno=self.cleaned_data['app_materno'], password=self.cleaned_data['password'])

        admin.save()
        return admin


class NuevoCurso(forms.Form):
    nombreCurso = forms.CharField(max_length=250,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)
    codigoCurso = forms.CharField(max_length=8,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)
    numSeccionCurso = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    anioCurso = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)
    semesterCurso = forms.IntegerField(
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=True)


    def is_valid(self):
        return super(NuevoCurso, self).is_valid()

    def save(self, *args, **kwargs):
        course = Course(nombreCurso=self.cleaned_data['nombreCurso'], codigoCurso=self.cleaned_data['codigoCurso'],
                        numSeccionCurso=self.cleaned_data['numSeccionCurso'], anioCurso=self.cleaned_data['anioCurso'],
                        semesterCurso=self.cleaned_data['semesterCurso'])

        course.save()
        return course

class RegistroEvaluadorForm(forms.Form):
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
    correo = forms.EmailField(max_length=100,
                              widget=forms.TextInput(attrs={'class' : 'form-control'}),
                              required=True)

    def is_valid(self):
        return super(RegistroEvaluadorForm, self).is_valid()

    def save(self, usuario_id,  *args, **kwargs):
        evaluador = Usuario_evaluador(name=self.cleaned_data['name'], app_paterno=self.cleaned_data['app_paterno'],
                              app_materno=self.cleaned_data['app_materno'], password=self.cleaned_data['password'],
                                      correo=self.cleaned_data['correo'])
        evaluador.myAdminID = Usuario_admin.objects.get(pk=usuario_id)
        evaluador.save()
        return evaluador



#class NuevaRubrica(forms.Form):

#    def is_valid(self):
#        return super(NuevaRubrica, self).is_valid()

#    def save(self, *args, **kwargs):
#        return rubrica
