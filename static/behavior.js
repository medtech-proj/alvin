var mapdiv= document.getElementById('map');
function initMap(data) {
	var map = new google.maps.Map(mapdiv, {
		zoom: 12,
		// center: {lat: 40.78, lng: -74}
		center: new google.maps.LatLng(40.78,-74)
	});
	getGeoLoc(map)
	if (data){
		newMarker(data, map);
	}

};

/*for as many data points returned from query:
	 make an instance of InfoWindow
	 make an instance of LatLng
	 make an instance of Marker, with given position, map, and details
*/
function newMarker(data, map){
	var infoWindow = new google.maps.InfoWindow();

	for (var i = 0; i<data.length; i++) {
		var facility= data[i];
		
		var latLng = new google.maps.LatLng(facility['latitude'], facility['longitude']);

		var marker = new google.maps.Marker(
			{
				position: latLng,
				map: map
			}
		);
		eventListener(infoWindow, marker, facility, map);
	}
};

// Attaching a click event listener to the current marker
function eventListener(infoWindow, marker, facility, map){
	google.maps.event.addListener(marker, "click", function(e) {
		console.log(facility.name)
		// var content=
		infoWindow.setContent(facility.address);
		infoWindow.open(map, marker);
	});

}




// gets geo-location
function getGeoLoc(map){
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

	function handleLocationError(browserHasGeolocation, infoWindow, pos) {
		infoWindow.setPosition(pos);
		infoWindow.setContent(browserHasGeolocation ?
	  	'Error: The Geolocation service failed.' :
	  	'Error: Your browser doesn\'t support geolocation.');
	}

};



document.getElementById('searchSub').addEventListener('click', function(event){
	//prevent page refresh
		event.preventDefault();
		console.log('click')
		//form value stored as var name and passed to searchBar()
		var name = document.querySelector('#searchInput').value

		console.log(name);
		searchBar(name);
	});


const searchBar = function(name){
	//goes to route ('/procedure/<name>') in controller.py and runs get_data(name)
	var url = '/procedure/'+name;	
	var xhttp= new XMLHttpRequest();
	xhttp.onreadystatechange=function(){
		if(this.readyState==4 && this.status==200){
			//this.responseText = get_data(name) response = json.dumps(data) from db query. turns .dumps string into an obj.
			var array_obj = JSON.parse(this.responseText);
			console.log("in searchBar", array_obj)
			//passes array_obj into initMap() as data
			initMap(array_obj);
		}
		// var newData= data.split(',');
		// console.log(newData);
	};
	xhttp.open("GET", url, true);
	xhttp.send()
}











