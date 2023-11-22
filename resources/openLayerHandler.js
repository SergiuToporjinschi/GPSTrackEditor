var map;

var mainTrackVectorLayer;
var currentPositionPointVectorLayer;
var trimmedTrackVectorLayer;

var zoomLevel = 2;

var styleConfig = {
    mainTrack: { stroke: { color: 'gray', width: 4 } },
    currentPositionPoint: {
        radius: 6,
        fill: { color: 'red' },
        stroke: { color: 'white', width: 2 }
    },
    trimmedTrack: { stroke: { color: 'lightgray', width: 4 } },
    stationaryMarker: { stroke: { color: 'red', width: 4 } },
    customMarker: { stroke: { color: 'yellow', width: 4 } },
}

function initMap(coordinates) {
    btn = new SettingsControl({
        target: 'your-target-element', // Specify the target element to render the control
    });
    map = new ol.Map({
        target: 'basicMap', // ID of the div element where the map will be rendered
        layers: [
            new ol.layer.Tile({
                source: new ol.source.OSM()
            })
        ],
        view: new ol.View({
            center: ol.proj.fromLonLat([0, 0]), // Center of the map
            zoom: zoomLevel
        })
    });
    map.getView().on('change:resolution', saveZoom);
    map.addControl(btn)
}

function setMainTrack(newCoordinates) {
    clearAllLayers()

    // Clear existing vector layer
    if (mainTrackVectorLayer) {
        map.removeLayer(mainTrackVectorLayer);
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
        stroke: new ol.style.Stroke(styleConfig.mainTrack.stroke)
    });
    feature.setStyle(trackStyle);

    mainTrackVectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [feature]
        })
    });

    map.addLayer(mainTrackVectorLayer);

    var extent = feature.getGeometry().getExtent();

    // Zoom to fit the extent of the feature
    map.getView().fit(extent, { padding: [20, 20, 20, 20] }); // Adjust padding as needed
}

function setCurrentPositionPoint(pointCoordinates) {
    if (currentPositionPointVectorLayer) {
        map.removeLayer(currentPositionPointVectorLayer);
    }
    var point = new ol.geom.Point(ol.proj.fromLonLat(JSON.parse(pointCoordinates)));

    var pointFeature = new ol.Feature({
        geometry: point
    });

    // Define a style for the marker
    var style = new ol.style.Style({
        image: new ol.style.Circle({
            radius: styleConfig.currentPositionPoint.radius,
            fill: new ol.style.Fill(styleConfig.currentPositionPoint.fill),
            stroke: new ol.style.Stroke(styleConfig.currentPositionPoint.stroke)
        })
    });

    pointFeature.setStyle(style);

    // Create a vector layer for the marker
    currentPositionPointVectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [pointFeature]
        })
    });
    map.addLayer(currentPositionPointVectorLayer);
    map.getView().fit(point, { maxZoom: zoomLevel })
}

function setTrimmedTrack(newCoordinates) {
    firstLoad = true
    if (trimmedTrackVectorLayer) {
        firstLoad = false
        map.removeLayer(trimmedTrackVectorLayer);
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
        stroke: new ol.style.Stroke(styleConfig.trimmedTrack.stroke)
    });
    feature.setStyle(trackStyle);

    trimmedTrackVectorLayer = new ol.layer.Vector({
        source: new ol.source.Vector({
            features: [feature]
        })
    });

    map.addLayer(trimmedTrackVectorLayer);

    // Zoom to fit the extent of the feature
    // map.getView().fit(extent, { padding: [20, 20, 20, 20] }); // Adjust padding as needed
    if (firstLoad) {
        var extent = feature.getGeometry().getExtent();
        map.getView().fit(extent, { padding: [20, 20, 20, 20] }); // Adjust padding as needed
    }
}

function saveZoom(event) {
    zoomLevel = map.getView().getZoom();
}

function configChanged(newConfig) {
    styleConfig = JSON.parse(newConfig)

    if (currentPositionPointVectorLayer) {
        var markerStyle = new ol.style.Style({
            image: new ol.style.Circle({
                radius: styleConfig.currentPositionPoint.radius,
                fill: new ol.style.Fill(styleConfig.currentPositionPoint.fill),
                stroke: new ol.style.Stroke(styleConfig.currentPositionPoint.stroke)
            })
        });
        currentPositionPointVectorLayer.getSource().getFeatures()[0].setStyle(markerStyle);
        currentPositionPointVectorLayer.changed()
    }

    if (mainTrackVectorLayer) {
        var trackStyle = new ol.style.Style({
            stroke: new ol.style.Stroke(styleConfig.mainTrack.stroke)
        });
        mainTrackVectorLayer.getSource().getFeatures()[0].setStyle(trackStyle);
        mainTrackVectorLayer.changed()
    }
}

function clearAllLayers() {
    map.removeLayer(mainTrackVectorLayer);
    map.removeLayer(trimmedTrackVectorLayer);
    map.removeLayer(currentPositionPointVectorLayer);

    mainTrackVectorLayer = undefined;
    trimmedTrackVectorLayer = undefined;
    currentPositionPointVectorLayer = undefined;
}
