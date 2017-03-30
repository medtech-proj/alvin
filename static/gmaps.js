//map.data.loadGeoJson('map.geojson')

console.log("connected");

var mapdiv= document.getElementById('map');
console.log(mapdiv);

function initMap() {

var map = new google.maps.Map(mapdiv, {
    zoom: 10,
    center: {lat: 40.78, lng: -74}
  });


  console.log('inside initMap');

// NOTE: This uses cross-domain XHR, and may not work on older browsers.
  map.data.loadGeoJson(
      '../static/map.geojson');
  // console.log('after loadGeoJson');
};