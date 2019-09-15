from flask import Blueprint, render_template
from iching.hex_generator import PyChing
import pygal

bp = Blueprint('web', __name__, url_prefix='/web')


@bp.route('/<int:iterations>/<int:sets>')
def web_root(iterations, sets):
    experiment = PyChing(iterations=iterations, sets=sets)
    results = experiment.run()
    results_data = results[0]

    hex_keys = results_data[0][0].keys()
    hex_chart = pygal.Line()
    hex_chart.x_labels = hex_keys

    for one_set in results_data:
        hex_values = one_set[0].values()
        hex_chart.add(f'Set #{results_data.index(one_set)}', hex_values)
    hex_chart = hex_chart.render_data_uri()

    tri_keys = results_data[0][1].keys()
    tri_chart = pygal.Line()
    tri_chart.x_labels = tri_keys
    for one_set in results_data:
        tri_values = one_set[1].values()
        tri_chart.add(f'Set #{results_data.index(one_set)}', tri_values)
    tri_chart = tri_chart.render_data_uri()

    meanings = results[1]

    return render_template('results.html',
                           hex_chart=hex_chart,
                           tri_chart=tri_chart,
                           meanings=meanings
                           )
