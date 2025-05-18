from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('checklist.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    portada_practica = request.form.get('portada_practica')
    problema_1_practica = request.form.get('problema_1_practica')
    problema_2_practica = request.form.get('problema_2_practica')
    conclusiones_practica = request.form.get('conclusiones_practica')

    indicador_e = request.form.get('indicador_e')
    indicador_f = request.form.get('indicador_f')
    indicador_a = request.form.get('indicador_a')
    indicador_b = request.form.get('indicador_b')
    indicador_c = request.form.get('indicador_c')
    indicador_d = request.form.get('indicador_d')

    criterio_1_proyecto = request.form.get('criterio_1_proyecto')
    criterio_2_proyecto = request.form.get('criterio_2_proyecto')
    criterio_3_proyecto = request.form.get('criterio_3_proyecto')
    criterio_4_proyecto = request.form.get('criterio_4_proyecto')
    criterio_5_proyecto = request.form.get('criterio_5_proyecto')
    criterio_6_proyecto = request.form.get('criterio_6_proyecto')
    criterio_7_proyecto = request.form.get('criterio_7_proyecto')
    criterio_8_proyecto = request.form.get('criterio_8_proyecto')
    criterio_9_proyecto = request.form.get('criterio_9_proyecto')
    criterio_10_proyecto = request.form.get('criterio_10_proyecto')

    entrega_proyecto_criterio1 = request.form.get('entrega_proyecto_criterio1')
    entrega_proyecto_criterio2 = request.form.get('entrega_proyecto_criterio2')
    entrega_proyecto_criterio3 = request.form.get('entrega_proyecto_criterio3')
    entrega_proyecto_criterio4 = request.form.get('entrega_proyecto_criterio4')
    entrega_proyecto_criterio5 = request.form.get('entrega_proyecto_criterio5')

    return render_template('resultado.html')

if __name__ == '__main__':
    app.run(debug=True)
