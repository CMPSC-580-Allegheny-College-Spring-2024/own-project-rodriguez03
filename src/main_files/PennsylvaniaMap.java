// <!DOCTYPE html>
// <html lang="en">
// <head>
//   <meta charset="UTF-8">
//   <meta name="viewport" content="width=device-width, initial-scale=1.0">
//   <title>Pennsylvania Map</title>
//   <link rel="stylesheet" href="https://unpkg.com/leaflet/dist/leaflet.css" />
//   <script src="https://unpkg.com/leaflet/dist/leaflet.js"></script>
//   <style>
//     #map { height: 600px; }
//   </style>
// </head>
// <body>
//   <div id="map"></div>

//   <script>
//     // Initialize the map
//     var map = L.map('map').setView([41.2033, -77.1945], 7);

//     // Add a tile layer
//     L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
//       attribution: '© OpenStreetMap contributors'
//     }).addTo(map);

//     // Add marker for Pennsylvania
//     L.marker([41.2033, -77.1945]).addTo(map)
//       .bindPopup('Pennsylvania')
//       .openPopup();
//   </script>
// </body>
// </html>



////////// Java
import javax.swing.*;
import java.awt.*;
import java.net.URL;

public class PennsylvaniaMap extends JFrame {

    public PennsylvaniaMap() {
        setTitle("Pennsylvania Map");
        setSize(800, 600);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        // Create a JLabel to display the map
        JLabel mapLabel = new JLabel();
        mapLabel.setPreferredSize(new Dimension(800, 600));

        // Load the Leaflet map HTML file
        URL mapUrl = getClass().getResource("pennsylvania_map.html");
        if (mapUrl != null) {
            mapLabel.setText("<html><iframe src='" + mapUrl + "' width='800' height='600'></iframe></html>");
        } else {
            mapLabel.setText("Failed to load map.");
        }

        // Add the map label to the frame
        add(mapLabel);

        setVisible(true);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> new PennsylvaniaMap());
    }
}

