from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    unidades = {
        'Unidad 1': [
            'Elaboración de Manual IDE con imágenes y color',
            'Exposición del Manual IDE',
            'Constancia de Curso en Línea edX, Google, Coursera',
            'El Manual IDE contiene programas de ejemplo'
        ],
        'Unidad 2': [
            'Práctica de programación (24/Feb/2022)',
            'Proyecto 2 y 3',
            'Trabajo del proyecto 2 y 3'
        ],
        'Unidad 3': [
            'Práctica de programación (17/Mar/2022)',
            'Constancia de Curso en Línea',
            'Explica problemas propuestos'
        ],
        'Unidad 4': [
            'Práctica de programación (07/Abr/2022)',
            'Proyecto (08/Abr/2022)',
            'Trabajo del proyecto (26/Abr/2022)',
            'Diseñar opciones adicionales al proyecto',
            'Participación en clase'
        ],
        'Unidad 5': [
            'Práctica de programación (13/May/2022)',
            'Proyecto',
            'Trabajo del proyecto',
            'Proyecto en beneficio de su Comunidad'
        ],
        'Unidad 6': [
            'Práctica de programación (25/May/2022)',
            'Resolución de problemas adicionales',
            'Entregar trabajos en tiempo y forma'
        ]
    }

    mensaje = None
    if request.method == 'POST':
        seleccionados = request.form.getlist('checks')
        mensaje = f"¡Checklist enviado correctamente! {len(seleccionados)} elementos seleccionados."

    return render_template('checklist.html', unidades=unidades, mensaje=mensaje)

if __name__ == '__main__':
    app.run(debug=True)
