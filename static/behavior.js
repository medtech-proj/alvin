console.log("js connected");
var mapdiv= document.getElementById('map');

	function initMap(data) {
		console.log("data in init", data)
		var map = new google.maps.Map(mapdiv, {
			zoom: 12,
			// center: {lat: 40.78, lng: -74}
			center: new google.maps.LatLng(40.78,-74)
		});

		for (var i = 0; i<data.length; i++) {
			var infoWindow = new google.maps.InfoWindow();
			var details= data[i],
				latLng = new google.maps.LatLng(details['latitude'], details['longitude']);
			console.log(details, "in for loop")
			console.log(latLng)
		

			var marker = new google.maps.Marker({
				position: latLng,
				map: map,
				name: details.name

			});
			// Attaching a click event to the current marker
			google.maps.event.addListener(marker, "click", function(e) {
 	 			infoWindow.setContent(details);
  				infoWindow.open(map, marker);
			});

			// Creating a closure to retain the correct data 
			//Note how I pass the current data in the loop into the closure (marker, data)
			(function(marker, data) {

			// Attaching a click event to the current marker
				google.maps.event.addListener(marker, "click", function(e) {
					infoWindow.setContent(data.description);
					infoWindow.open(map, marker);
				});

			})(marker, data);
		}

		// map.data.addGeoJson(data);
		// console.log("in initmap", map)
		// console.log("we are in initmap",data)

		// var infoWindow = new google.maps.infoWindow();

// gets geo-location///////////////////////////////// 

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



const searchBar = function(name){
	var url = '/procedure/'+name;	
	var xhttp= new XMLHttpRequest();
		xhttp.onreadystatechange=function(){
			if(this.readyState==4 && this.status==200){
				console.log("we made it!")
				var array_obj = JSON.parse(this.responseText);
				console.log("in searchBar", array_obj)
				initMap(array_obj);
			
			}

			// var newData= data.split(',');

			// console.log(newData);
		};
		xhttp.open("GET", url, true);
		xhttp.send()
}


document.getElementById('searchSub').addEventListener('click', function(event){
		event.preventDefault();
		console.log('click')
		var name = document.querySelector('#searchInput').value

		console.log(name);
		searchBar(name);
		// console.log(data);
	});



// var getMap = function(dataObj){
// 	let map = IIFE();
	
// }












