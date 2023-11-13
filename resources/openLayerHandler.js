// function init() {
//     var map = new ol.Map({
//         target: 'basicMap', // ID of the div element where the map will be rendered
//         layers: [
//             new ol.layer.Tile({
//                 source: new ol.source.OSM()
//             })
//         ],
//         view: new ol.View({
//             center: ol.proj.fromLonLat([0, 0]), // Center of the map
//             zoom: 2 // Initial zoom level
//         })
//     });
//     var coordinates = [
//         [24.19399667, 45.81218000],
//         [24.19401500, 45.81217000],
//         [24.19403167, 45.81216000]
//         // Add more coordinates as needed
//     ];

//     var lineString = new ol.geom.LineString(coordinates).transform('EPSG:4326', 'EPSG:3857');
//     var feature = new ol.Feature({
//         geometry: lineString
//     });
//     var vectorLayer = new ol.layer.Vector({
//         source: new ol.source.Vector({
//             features: [feature]
//         })
//     });
//     map.addLayer(vectorLayer);
//     map.getView().fit(lineString.getExtent(), map.getSize());
// }
var map;
var vectorLayer;
var markPositionVectorLayer;
function initMap(coordinates) {
    map = new ol.Map({
        target: 'basicMap', // ID of the div element where the map will be rendered
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([0, 0]), // Center of the map
            zoom: 2 // Initial zoom level
        })
    });

    loadTrack(coordinates);
}

function loadTrack(newCoordinates) {
    // Clear existing vector layer
    if (vectorLayer) {
        map.removeLayer(vectorLayer);
    }
    if (!newCoordinates || !Array.isArray(JSON.parse(newCoordinates)) || !JSON.parse(newCoordinates).length) {
        return;
    }
    newCoordinates = JSON.parse(newCoordinates)
    var lineString = new ol.geom.LineString(newCoordinates).transform('EPSG:4326', 'EPSG:3857');
    var feature = new ol.Feature({
        geometry: lineString,
    });

    var trackStyle = new ol.style.Style({
        stroke: new ol.style.Stroke({
            color: 'gray', // Set the desired color here
            width: 4
        })
    });
    feature.setStyle(trackStyle);
    vectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [feature]
        })
    });

    map.addLayer(vectorLayer);
    map.getView().fit(lineString.getExtent(), map.getSize());
}

function markPoint(pointCoordinates) {
    if (markPositionVectorLayer) {
        map.removeLayer(markPositionVectorLayer);
    }
    var point = new ol.geom.Point(ol.proj.fromLonLat(JSON.parse(pointCoordinates)));
    var pointFeature = new ol.Feature({
        geometry: point
    });

    // Define a style for the marker
    var markerStyle = new ol.style.Style({
        image: new ol.style.Circle({
            radius: 6,
            fill: new ol.style.Fill({
                color: 'red' // Set the desired color for the marker
            }),
            stroke: new ol.style.Stroke({
                color: 'white',
                width: 2
            })
        })
    });

    pointFeature.setStyle(markerStyle);

    // Create a vector layer for the marker
    markPositionVectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [pointFeature]
        })
    });

    map.addLayer(markPositionVectorLayer);
}
