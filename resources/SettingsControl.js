var SettingsControl = function (options) {
    var element = document.querySelector('.control-container'); // Create an empty div element

    var control = new ol.control.Control({ // Create an ol.control.Control instance
        element: element,
        render: options.render,
        target: options.target
    });

    setting = {
        mainTrack: true,
        trimmedTrack: true,
        currentPositionPoint: true
    }

    var mainTrack = element.querySelector('#mainTrackVisibleLine');
    mainTrack.querySelector('line').setAttribute('stroke', styleConfig.mainTrack.stroke.color);
    mainTrack.addEventListener('click', _onMainTrackVisible, false);

    var trimmedTrack = element.querySelector('#trimmedTrackVisibleLine');
    trimmedTrack.querySelector('line').setAttribute('stroke', styleConfig.trimmedTrack.stroke.color);
    trimmedTrack.addEventListener('click', _onTrimmedTrackVisible, false);

    var currentPositionPoint = element.querySelector('#currentPositionPointVisiblePoint');
    currentPositionPoint.querySelector('circle').setAttribute('fill', styleConfig.currentPositionPoint.fill.color);
    currentPositionPoint.addEventListener('click', _onCurrentPositionPointVisible, false);

    mainTrack = element.querySelector('#mainTrackVisible'); // Get the button element
    mainTrack.addEventListener('change', _onMainTrackVisible, false);

    trimmedTrack = element.querySelector('#trimmedTrackVisible'); // Get the button element
    trimmedTrack.addEventListener('change', _onTrimmedTrackVisible, false);

    currentPositionPoint = element.querySelector('#currentPositionPointVisible'); // Get the button element
    currentPositionPoint.addEventListener('change', _onCurrentPositionPointVisible, false);

    function _onMainTrackVisible(event) {
        mainTrackVectorLayer.setVisible(event.target.checked)
    }
    function _onTrimmedTrackVisible(event) {
        trimmedTrackVectorLayer.setVisible(event.target.checked)
    }
    function _onCurrentPositionPointVisible(event) {
        currentPositionPointVectorLayer.setVisible(event.target.checked)
    }
    return control; // Return the control instance
};
