require([
    "esri/Map",
    "esri/layers/FeatureLayer",
    "esri/views/MapView",
    "esri/widgets/Home"
  ],
  function (
    Map,
    FeatureLayer,
    MapView,
    Home
  ) {
    var map = new Map({
      basemap: "streets"
    });

    var view = new MapView({
      container: "viewDiv",
      map: map,
      zoom: 12,
      center: [-74.051239, 4.673729]
    });

    var homeWidget = new Home({
      view: view
    });
    view.ui.add(homeWidget, "top-left");


    var featureLayer = new FeatureLayer({
      url: "https://services7.arcgis.com/rxsqAG0ztOQO48WN/arcgis/rest/services/Colegios_Bogota_2017/FeatureServer/0"
    });
    map.add(featureLayer);
  });
