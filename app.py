from flask import Flask, render_template
from pathlib import Path
from ament_index_python.packages import get_package_share_directory
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    map_ = Path(get_package_share_directory('navigation2_agbee'), 'map')
    map_filename = "/home/omose/Desktop/map.pgm" #map_ / 'test.png'
    return render_template("app.html", map_image = map_filename)

if __name__ == "__main__":
    app.run(debug=True)
