from flask import Flask, render_template, request, redirect, url_for
from business_rules import run_all
from business_rules.actions import BaseActions, rule_action
from business_rules.fields import FIELD_NUMERIC
from business_rules.variables import BaseVariables, numeric_rule_variable

app = Flask(__name__)

# Clase para variables del sistema de reglas
class EvaluacionVariables(BaseVariables):
    def __init__(self, evaluacion_data):
        self.evaluacion_data = evaluacion_data
    
    @numeric_rule_variable
    def portada_practica(self):
        return float(self.evaluacion_data.get('portada_practica', 0))
    
    @numeric_rule_variable
    def problema_1_practica(self):
        return float(self.evaluacion_data.get('problema_1_practica', 0))
    
    @numeric_rule_variable
    def problema_2_practica(self):
        return float(self.evaluacion_data.get('problema_2_practica', 0))
    
    @numeric_rule_variable
    def conclusiones_practica(self):
        return float(self.evaluacion_data.get('conclusiones_practica', 0))
    
    @numeric_rule_variable
    def indicador_e(self):
        return float(self.evaluacion_data.get('indicador_e', 0))
    
    @numeric_rule_variable
    def indicador_f(self):
        return float(self.evaluacion_data.get('indicador_f', 0))
    
    # Valor del indicador A multiplicado por 5 (en el form se usa 1 para "Sí")
    @numeric_rule_variable
    def indicador_a(self):
        val = self.evaluacion_data.get('indicador_a', '0')
        return float(val) * 5 if val else 0
    
    @numeric_rule_variable
    def indicador_b(self):
        return float(self.evaluacion_data.get('indicador_b', 0))
    
    @numeric_rule_variable
    def indicador_c(self):
        return float(self.evaluacion_data.get('indicador_c', 0))
    
    @numeric_rule_variable
    def indicador_d(self):
        return float(self.evaluacion_data.get('indicador_d', 0))
    
    # Variables para el proyecto (criterios 1-10)
    @numeric_rule_variable
    def criterio_1_proyecto(self):
        return float(self.evaluacion_data.get('criterio_1_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_2_proyecto(self):
        return float(self.evaluacion_data.get('criterio_2_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_3_proyecto(self):
        return float(self.evaluacion_data.get('criterio_3_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_4_proyecto(self):
        return float(self.evaluacion_data.get('criterio_4_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_5_proyecto(self):
        return float(self.evaluacion_data.get('criterio_5_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_6_proyecto(self):
        return float(self.evaluacion_data.get('criterio_6_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_7_proyecto(self):
        return float(self.evaluacion_data.get('criterio_7_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_8_proyecto(self):
        return float(self.evaluacion_data.get('criterio_8_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_9_proyecto(self):
        return float(self.evaluacion_data.get('criterio_9_proyecto', 0))
    
    @numeric_rule_variable
    def criterio_10_proyecto(self):
        return float(self.evaluacion_data.get('criterio_10_proyecto', 0))
    
    # Variables para la entrega del proyecto
    @numeric_rule_variable
    def entrega_proyecto_criterio1(self):
        return float(self.evaluacion_data.get('entrega_proyecto_criterio1', 0))
    
    @numeric_rule_variable
    def entrega_proyecto_criterio2(self):
        return float(self.evaluacion_data.get('entrega_proyecto_criterio2', 0))
    
    @numeric_rule_variable
    def entrega_proyecto_criterio3(self):
        return float(self.evaluacion_data.get('entrega_proyecto_criterio3', 0))
    
    @numeric_rule_variable
    def entrega_proyecto_criterio4(self):
        return float(self.evaluacion_data.get('entrega_proyecto_criterio4', 0))
    
    @numeric_rule_variable
    def entrega_proyecto_criterio5(self):
        return float(self.evaluacion_data.get('entrega_proyecto_criterio5', 0))

# Clase para acciones del sistema de reglas
class EvaluacionActions(BaseActions):
    def __init__(self, result):
        self.result = result
    
    @rule_action(params={"puntuacion": FIELD_NUMERIC})
    def add_to_practica(self, puntuacion):
        # Aseguramos que puntuacion sea un número, no un diccionario
        if isinstance(puntuacion, dict) and 'value' in puntuacion:
            self.result['practica'] += float(puntuacion['value'])
        else:
            self.result['practica'] += float(puntuacion)
    
    @rule_action(params={"puntuacion": FIELD_NUMERIC})
    def add_to_proyecto(self, puntuacion):
        # Aseguramos que puntuacion sea un número, no un diccionario
        if isinstance(puntuacion, dict) and 'value' in puntuacion:
            self.result['proyecto'] += float(puntuacion['value'])
        else:
            self.result['proyecto'] += float(puntuacion)
    
    @rule_action(params={"puntuacion": FIELD_NUMERIC})
    def add_to_entrega_proyecto(self, puntuacion):
        # Aseguramos que puntuacion sea un número, no un diccionario
        if isinstance(puntuacion, dict) and 'value' in puntuacion:
            self.result['entrega_proyecto'] += float(puntuacion['value'])
        else:
            self.result['entrega_proyecto'] += float(puntuacion)
    
    @rule_action(params={"puntuacion": FIELD_NUMERIC})
    def add_to_indicadores(self, puntuacion):
        # Aseguramos que puntuacion sea un número, no un diccionario
        if isinstance(puntuacion, dict) and 'value' in puntuacion:
            self.result['indicadores'] += float(puntuacion['value'])
        else:
            self.result['indicadores'] += float(puntuacion)
    
    @rule_action(params={"puntuacion": FIELD_NUMERIC})
    def add_to_total(self, puntuacion):
        # Importante: Este método debe manejar tanto valores directos como diccionarios
        if isinstance(puntuacion, dict) and 'value' in puntuacion:
            self.result['total'] += float(puntuacion['value'])
        else:
            self.result['total'] += float(puntuacion)

# Definir reglas para la evaluación
def get_rules():
    rules = [
        # Reglas para práctica
        {
            'conditions': {
                'all': [
                    {
                        'name': 'portada_practica',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_practica',
                    'params': {'puntuacion': 'portada_practica'}
                }
            ]
        },
        {
            'conditions': {
                'all': [
                    {
                        'name': 'problema_1_practica',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_practica',
                    'params': {'puntuacion': 'problema_1_practica'}
                }
            ]
        },
        {
            'conditions': {
                'all': [
                    {
                        'name': 'problema_2_practica',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_practica',
                    'params': {'puntuacion': 'problema_2_practica'}
                }
            ]
        },
        {
            'conditions': {
                'all': [
                    {
                        'name': 'conclusiones_practica',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_practica',
                    'params': {'puntuacion': 'conclusiones_practica'}
                }
            ]
        },
        
        # Reglas para indicadores E y F
        {
            'conditions': {
                'all': [
                    {
                        'name': 'indicador_e',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_indicadores',
                    'params': {'puntuacion': 'indicador_e'}
                }
            ]
        },
        {
            'conditions': {
                'all': [
                    {
                        'name': 'indicador_f',
                        'operator': 'greater_than',
                        'value': 0
                    }
                ]
            },
            'actions': [
                {
                    'name': 'add_to_indicadores',
                    'params': {'puntuacion': 'indicador_f'}
                }
            ]
        },
        
        # Reglas para criterios de proyecto (1-10)
        {
            'conditions': {'all': [{'name': 'criterio_1_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_1_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_2_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_2_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_3_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_3_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_4_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_4_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_5_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_5_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_6_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_6_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_7_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_7_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_8_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_8_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_9_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_9_proyecto'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'criterio_10_proyecto', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'criterio_10_proyecto'}}
            ]
        },
        
        # Regla para indicador A (criterio 11)
        {
            'conditions': {'all': [{'name': 'indicador_a', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_indicadores', 'params': {'puntuacion': 'indicador_a'}},
                {'name': 'add_to_proyecto', 'params': {'puntuacion': 'indicador_a'}}
            ]
        },
        
        # Reglas para indicadores B, C, D
        {
            'conditions': {'all': [{'name': 'indicador_b', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_indicadores', 'params': {'puntuacion': 'indicador_b'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'indicador_c', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_indicadores', 'params': {'puntuacion': 'indicador_c'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'indicador_d', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_indicadores', 'params': {'puntuacion': 'indicador_d'}}
            ]
        },
        
        # Reglas para entrega de proyecto
        {
            'conditions': {'all': [{'name': 'entrega_proyecto_criterio1', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_entrega_proyecto', 'params': {'puntuacion': 'entrega_proyecto_criterio1'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'entrega_proyecto_criterio2', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_entrega_proyecto', 'params': {'puntuacion': 'entrega_proyecto_criterio2'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'entrega_proyecto_criterio3', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_entrega_proyecto', 'params': {'puntuacion': 'entrega_proyecto_criterio3'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'entrega_proyecto_criterio4', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_entrega_proyecto', 'params': {'puntuacion': 'entrega_proyecto_criterio4'}}
            ]
        },
        {
            'conditions': {'all': [{'name': 'entrega_proyecto_criterio5', 'operator': 'greater_than', 'value': 0}]},
            'actions': [
                {'name': 'add_to_entrega_proyecto', 'params': {'puntuacion': 'entrega_proyecto_criterio5'}}
            ]
        }
    ]
    return rules

@app.route('/', methods=['GET'])
def index():
    return render_template('checklist.html')

@app.route('/evaluar', methods=['POST'])
def evaluar():
    # Recoger todos los datos del formulario
    evaluacion_data = request.form.to_dict()
    
    # Para manejar valores vacíos y convertir a tipo numérico
    for key, value in evaluacion_data.items():
        if value == '':
            evaluacion_data[key] = '0'
    
    # Inicializar resultado
    result = {
        'practica': 0,
        'proyecto': 0,
        'entrega_proyecto': 0,
        'indicadores': 0,
        'total': 0
    }
    
    # Función para convertir a float de manera segura
    def safe_float(value, default=0):
        try:
            return float(value) if value else default
        except (ValueError, TypeError):
            return default
    
    # Cálculo directo para asegurar que los datos se procesen correctamente
    # Práctica
    practica_puntos = (
        safe_float(evaluacion_data.get('portada_practica')) +
        safe_float(evaluacion_data.get('problema_1_practica')) +
        safe_float(evaluacion_data.get('problema_2_practica')) +
        safe_float(evaluacion_data.get('conclusiones_practica'))
    )
    result['practica'] = practica_puntos
    
    # Proyecto
    proyecto_puntos = 0
    for i in range(1, 11):
        proyecto_puntos += safe_float(evaluacion_data.get(f'criterio_{i}_proyecto'))
    # Añadir indicador A (multiplicado por 5 porque en el form es 1 para "Sí")
    indicador_a = safe_float(evaluacion_data.get('indicador_a')) * 5
    proyecto_puntos += indicador_a
    result['proyecto'] = proyecto_puntos
    
    # Entrega proyecto
    entrega_puntos = 0
    for i in range(1, 6):
        entrega_puntos += safe_float(evaluacion_data.get(f'entrega_proyecto_criterio{i}'))
    result['entrega_proyecto'] = entrega_puntos
    
    # Indicadores
    indicadores_puntos = (
        indicador_a +  # Ya multiplicado por 5
        safe_float(evaluacion_data.get('indicador_b')) +
        safe_float(evaluacion_data.get('indicador_c')) +
        safe_float(evaluacion_data.get('indicador_d')) +
        safe_float(evaluacion_data.get('indicador_e')) +
        safe_float(evaluacion_data.get('indicador_f'))
    )
    result['indicadores'] = indicadores_puntos
    
    # Total (evitando contar indicador_a dos veces)
    result['total'] = practica_puntos + proyecto_puntos + entrega_puntos + (indicadores_puntos - indicador_a)
    
    # Intentar usar el motor de reglas como complemento, pero confiar en el cálculo directo
    try:
        # Crear variables y acciones para el rule engine
        variables = EvaluacionVariables(evaluacion_data)
        actions = EvaluacionActions(result)
        
        # Ejecutar las reglas
        rules = get_rules()
        run_all(rule_list=rules, 
                defined_variables=variables, 
                defined_actions=actions,
                stop_on_first_trigger=False)
    except Exception as e:
        print(f"Error al ejecutar rules: {e}")
        # Continuamos con nuestro cálculo manual aunque el motor de reglas falle
    
    # Calcular porcentajes y calificación final
    max_score = 320  # Nuevo valor máximo ajustado
    porcentaje = min(100, round((result['total'] / max_score) * 100, 2))
    
    # Determinar valoración y calificación
    def get_calificacion(puntuacion):
        if puntuacion >= 95:
            return "Excelente", 100
        elif puntuacion >= 85:
            return "Muy bien", 90
        elif puntuacion >= 75:
            return "Bien", 80
        elif puntuacion >= 70:
            return "Suficiente", 70
        else:
            return "No Aprobado", 60
    
    valoracion, calificacion = get_calificacion(porcentaje)
    
    # Datos detallados para mostrar en el resultado (usando los valores directos del formulario)
    detalles = {
        'portada_practica': safe_float(evaluacion_data.get('portada_practica')),
        'problema_1_practica': safe_float(evaluacion_data.get('problema_1_practica')),
        'problema_2_practica': safe_float(evaluacion_data.get('problema_2_practica')),
        'conclusiones_practica': safe_float(evaluacion_data.get('conclusiones_practica')),
        'indicador_e': safe_float(evaluacion_data.get('indicador_e')),
        'indicador_f': safe_float(evaluacion_data.get('indicador_f')),
        'criterios_proyecto': [
            safe_float(evaluacion_data.get(f'criterio_{i}_proyecto')) for i in range(1, 11)
        ],
        'indicador_a': indicador_a,
        'indicador_b': safe_float(evaluacion_data.get('indicador_b')),
        'indicador_c': safe_float(evaluacion_data.get('indicador_c')),
        'indicador_d': safe_float(evaluacion_data.get('indicador_d')),
        'entrega_proyecto': [
            safe_float(evaluacion_data.get(f'entrega_proyecto_criterio{i}')) for i in range(1, 6)
        ]
    }
    
    # Imprimir para debug
    print(f"Puntuación total: {result['total']}")
    print(f"Porcentaje: {porcentaje}%")
    print(f"Resultado: {valoracion}, Calificación: {calificacion}")
    
    return render_template('resultado.html', 
                          resultado=result, 
                          porcentaje=porcentaje,
                          valoracion=valoracion,
                          calificacion=calificacion,
                          detalles=detalles)

if __name__ == '__main__':
    app.run(debug=True)