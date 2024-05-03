import sys
import os
import webbrowser
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QCursor
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class PennsylvaniaMap(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pennsylvania Map")
        self.setGeometry(100, 100, 800, 600)
        self.setup_ui()

    def setup_ui(self):
        # HTML content from Pennsylvania_map.html
        html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Pennsylvania Map with Districts</title>
        <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
        <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
        <style>
            #map { height: 600px; }
        </style>
        </head>
        <body>
        <div id="map"></div>

        <script>
            var map = L.map('map').setView([41.2033, -77.1945], 7); // Centered at Pennsylvania

            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
            attribution: '© OpenStreetMap contributors'
            }).addTo(map);

            // Load and display GeoJSON map data
            fetch('pennsylvania_districts.geojson')
            .then(response => response.json())
            .then(data => {
                L.geoJSON(data, {
                    style: function(feature) {
                        return {
                            fillColor: 'green', // Change color as needed
                            fillOpacity: 0.5,
                            weight: 2,
                            color: 'black'
                        };
                    }
                }).addTo(map);
            });
        </script>
        </body>
        </html>
        """

        # Create the QWebEngineView and load the HTML content
        self.map_widget = QWebEngineView(self)
        self.map_widget.setHtml(html_content, QUrl.fromLocalFile(""))
        self.map_widget.setGeometry(0, 0, 800, 600)
        self.setCentralWidget(self.map_widget)

        # Write the HTML content to the file
        file_path = "pennsylvania_map.html"
        with open(file_path, "w") as f:
            f.write(html_content)

        # Open the HTML file in the default web browser
        webbrowser.open("file://" + os.path.abspath(file_path))

        # self.map_widget = QWebEngineView(self)
        # self.map_widget.load(QUrl.fromLocalFile(os.path.abspath(file_path)))
        # self.map_widget.setGeometry(0, 0, 800, 600)
        # self.map_widget.show()

        self.label = QLabel(self)
        self.label.setText("Click here to view map in browser")
        self.label.setGeometry(300, 250, 200, 30)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.mousePressEvent = self.open_browser

    def open_browser(self, event):
        file_path = os.path.abspath("pennsylvania_map.html")
        webbrowser.open_new_tab("file://" + file_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PennsylvaniaMap()
    window.show()
    sys.exit(app.exec_())
