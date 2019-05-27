from django import forms
from .models import Usuario_admin
from .models import Course
from .models import Usuario_evaluador


import json

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

def generateJsonFromPost(post):
    rubrica=post


    return rubrica

def jsonisacion(data,rubrica,idUsuario):
    if data:
        a=data

        a[str(idUsuario)][rubrica.get("tituloRubrica")]=rubrica
    else:
        a={str(idUsuario):{rubrica.get("tituloRubrica"): rubrica}}
    return a
class NuevaRubrica(forms.Form):


    def save(self,POST,userId):
        ##aqui va json

        rubrica=generateJsonFromPost(POST)

        with open('rubricaJson.json','r') as f:
            data = json.load(f)


        newJson=jsonisacion(data,rubrica,userId)





        with open('rubricaJson.json', 'w') as json_file:
            json.dump(newJson, json_file)


        ##aqui va json

        #print(POST)
        print("guardado")

        return False


class NuevoEvaluador(forms.Form):
    nombre = forms.CharField(max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)

    app_paterno=forms.CharField(max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)

    correo=forms.EmailField(max_length=200,
                                  widget=forms.TextInput(attrs={'class': 'form-control'}),
                                  required=True)

    def is_valid(self):
        return super(NuevoEvaluador, self).is_valid()


    def save(self,POST):
        nuevoEvaluador = Usuario_evaluador(nombreEvaluador=self.cleaned_data['nombre'], app_paterno=self.cleaned_data['app_paterno'], correo=self.cleaned_data['correo'])

        nuevoEvaluador.save()

        return nuevoEvaluador




