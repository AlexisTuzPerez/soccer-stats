    

from flask import Blueprint
from api.competiciones import get_competiciones, get_competiciones_by_id, get_competiciones_equipos, get_tabla_competicion, get_partidos, get_goleadores

competiciones_bp = Blueprint('competiciones', __name__)

@competiciones_bp.route('/competiciones')
def competiciones():
    return get_competiciones()

@competiciones_bp.route('/competiciones/<int:competition_id>')
def competicion(competition_id):
    print("competition_id:", competition_id)
    return get_competiciones_by_id(competition_id)

@competiciones_bp.route('/competiciones/<int:competition_id>/posiciones')
def competicion_posiciones(competition_id):
    print("competition_id:", competition_id)
    return get_tabla_competicion(competition_id)


@competiciones_bp.route('/competiciones/<int:competition_id>/partidos')
def competicion_partidos(competition_id):
    print("competition_id:", competition_id)
    return get_partidos(competition_id)




@competiciones_bp.route('/competiciones/<int:competition_id>/teams')
def competicion_teams(competition_id):
    print("competition_id:", competition_id)
    return get_competiciones_equipos(competition_id)


@competiciones_bp.route('/competiciones/<int:competition_id>/goleadores')
def competicion_goleadores(competition_id):
    print("competition_id:", competition_id)
    return get_goleadores(competition_id) 

