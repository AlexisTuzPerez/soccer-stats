from flask import Blueprint
from api.personas import obtener_persona, obtener_partidos_persona

personas_bp = Blueprint('personas', __name__)

@personas_bp.route('/personas/<int:jugador_id>')
def persona(jugador_id):
	return obtener_persona(jugador_id)

@personas_bp.route('/personas/<int:jugador_id>/partidos')
def persona_partidos(jugador_id):
	return obtener_partidos_persona(jugador_id)
