from flask import Blueprint
from api.equipos import obtener_equipo, listar_equipos, obtener_partidos_equipo

equipos_bp = Blueprint('equipos', __name__)

@equipos_bp.route('/equipos')
def equipos():
	return listar_equipos()

@equipos_bp.route('/equipos/<int:equipo_id>')
def equipo(equipo_id):
	return obtener_equipo(equipo_id)

@equipos_bp.route('/equipos/<int:equipo_id>/partidos')
def equipo_partidos(equipo_id):
	return obtener_partidos_equipo(equipo_id)
