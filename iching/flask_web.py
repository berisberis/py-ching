from flask import Blueprint, render_template
from iching.generator import PyChing
import pygal

bp = Blueprint('web', __name__, url_prefix='/web')


@bp.route('/<int:iterations>/<int:sets>')
def web_root(iterations, sets):
    experiment = PyChing(iterations=iterations, sets=sets)
    results = experiment.run()

    hex_values = list(results[0][0].values())
    hex_keys = list(results[0][0].keys())
    hex_chart = pygal.Line(range=(45, 90))
    hex_chart.x_labels = hex_keys
    hex_chart.add('Hexagrams', hex_values)
    hex_chart = hex_chart.render_data_uri()

    tri_values = list(results[0][1].values())
    tri_keys = list(results[0][1].keys())
    tri_chart = pygal.Line(range=(900, 1100))
    tri_chart.x_labels = tri_keys
    tri_chart.add('Trigrams', tri_values)
    tri_chart = tri_chart.render_data_uri()

    return render_template('results.html', hex_chart=hex_chart, tri_chart=tri_chart)