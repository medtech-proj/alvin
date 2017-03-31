function IIFE(){

	var mapdiv= document.getElementById('map');
	console.log(mapdiv);

	function initMap() {

		var map = new google.maps.Map(mapdiv, {
			zoom: 10,
			center: {lat: 40.78, lng: -74}
			// center: {lat: -10, lng: -10}
		});


		// NOTE: This uses cross-domain XHR, and may not work on older browsers.
		// map.data.loadGeoJson('../static/map.geojson');

		//getting user geolocation- requires consent
		// var infoWindow = new google.maps.InfoWindow({map: map});

		// Try HTML5 geolocation.
		if (navigator.geolocation) {
			navigator.geolocation.getCurrentPosition(function(position) {
				var pos = {
					lat: position.coords.latitude,
					lng: position.coords.longitude
				};

			// infoWindow.setPosition(pos);
			// infoWindow.setContent('Location found.');
				map.setCenter(pos);
		  	}, function() {
				handleLocationError(true, infoWindow, map.getCenter());
		  	});
		} else {
		  // Browser doesn't support Geolocation
		  	handleLocationError(false, infoWindow, map.getCenter());
		}
	};

	function handleLocationError(browserHasGeolocation, infoWindow, pos) {
		// infoWindow.setPosition(pos);
		infoWindow.setContent(browserHasGeolocation ?
	  	'Error: The Geolocation service failed.' :
	  	'Error: Your browser doesn\'t support geolocation.');
	}

}
// {
//   "featureType": "road"
// }
//poi.medical 
//transit