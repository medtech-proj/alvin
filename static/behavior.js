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
			//this.responseText = get_data(name) response = json.dumps(data) from db query
			var array_obj = JSON.parse(this.responseText);
			// console.log("in searchBar", array_obj)
			//passes array_obj into initMap() as data
			initMap(array_obj);
			// initMap([1,2,3,4,5]);
		}
		// var newData= data.split(',');
		// console.log(newData);
	};
	xhttp.open("GET", url, true);
	xhttp.send()
}



var mapdiv= document.getElementById('map');

// function initMap() {
function initMap(data) {
// console.log("data in init")
	var facility, data, address, infoWindow, latLng, marker;

	console.log("data in init", typeof(data))
	console.log(data)
	var map = new google.maps.Map(mapdiv, {
		// zoom: 12,
		zoom: 8,

		// radius: 146093,
		// center: {lat: 40.78, lng: -74}
		center: new google.maps.LatLng(40.78,-74)
	});


	// for as many data points returned from query:
	// 	make an instance of InfoWindow
	// 	make an instance of LatLng
	// 	make an instance of Marker, with given position, map, and details

	for (var i = 0; i<data.length; i++) {
		
		facility= data[i];
		address = facility['address']
		infoWindow = new google.maps.InfoWindow(facility);
		latLng = new google.maps.LatLng(facility.latitude, facility.longitude);
		// latLng = new google.maps.LatLng(facility['latitude'], facility['longitude']);


		// console.log(infoWindow, "in for loop");
		// console.log(latLng);
	

		marker = new google.maps.Marker({
			position: latLng,
			map: map
			// title: facility.name
		});
		// console.log(marker);

		// Attaching a click event + listener to the current marker
		// google.maps.event.addListener(marker, "click", function(e) {
	 // 			console.log('infowin',infoWindow)
	 // 			infoWindow.setContent(facility.tot_price);
	 // 			// console.log()
	 // 			// console.log(infoWindow.setContent('string'));
		// 		infoWindow.open(map, marker);
		// });

		// Creating a closure to retain the correct data 
		//Note how I pass the current data in the loop into the closure (marker, data)
		
		// this will show all the markers and not close
		// (function(marker, facility, infoWindow) {

		(function(marker, facility) {

		// Attaching a click event to the current marker
			google.maps.event.addListener(marker, "click", function(e) {
				// infoWindow.setContent(data[i]);
				console.log("in that listener",facility.address)
				var content = '<div><strong>' + facility.name + '</strong><br>'
                + facility.address + '<br>' + 'Cpt code: ' + facility.cpt_code + '</br>' + 'Price: $' +
                facility.tot_price + '<br>' + 'Description: ' + facility.description + '</div>';

				infoWindow.setContent(content);
				// infoWindow.setContent(facility.name);
				infoWindow.open(map, marker);
			});
		// })(marker, facility, infoWindow);

		})(marker, facility);
	}



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













