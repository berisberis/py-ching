from flask import Blueprint, render_template
from iching.generator import PyChing
import pygal

bp = Blueprint('web', __name__, url_prefix='/web')


@bp.route('/<int:iterations>/<int:sets>')
def web_root(iterations, sets):
    experiment = PyChing(iterations=iterations, sets=sets)
    results = experiment.run()

    hex_keys = list(results[0][0].keys())
    hex_chart = pygal.Line()
    hex_chart.x_labels = hex_keys
    for each_set in results:
        hex_values = each_set[0].values()
        hex_chart.add(f'Set #{results.index(each_set)}', hex_values)
    hex_chart = hex_chart.render_data_uri()

    tri_keys = list(results[0][1].keys())
    tri_chart = pygal.Line()
    tri_chart.x_labels = tri_keys
    for each_set in results:
        tri_values = each_set[1].values()
        tri_chart.add(f'Set #{results.index(each_set)}', tri_values)
    tri_chart = tri_chart.render_data_uri()

    return render_template('results.html', hex_chart=hex_chart, tri_chart=tri_chart)
