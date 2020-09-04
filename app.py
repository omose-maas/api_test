from flask import Flask, render_template
#from pathlib import Path
#from ament_index_python.packages import get_package_share_directory
from PIL import Image

app = Flask(__name__, static_folder='/')

map_filepath = "/Users/ichika/agbee/map/map.pgm"
map_png_filename = "map.png"

@app.route('/')
@app.route('/index')
def index():
    #map_ = Path(get_package_share_directory('navigation2_agbee'), 'map')
    #map_filename = "/home/omose/Desktop/map.pgm" #map_ / 'test.png'
    pgm_file = Image.open(map_filepath)
    pgm_file.save(map_png_filename, "png")
    map_filename = map_png_filename
    return render_template("app.html", map_image=map_filename)

if __name__ == "__main__":
    app.run(debug=True)
