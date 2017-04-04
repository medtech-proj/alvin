console.log("js connected");
var mapdiv= document.getElementById('map');
	console.log(mapdiv);

	function initMap(data) {

		var map = new google.maps.Map(mapdiv, {
			zoom: 12,
			center: {lat: 40.78, lng: -74}
			// center: {lat: -10, lng: -10}
		});

		map.data.addGeoJson(data);


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
				var data = JSON.parse(this.responseText);
				// console.log(data)
				initMap(data);
			
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
		var data =searchBar(name);
		console.log(data);
	});



// var getMap = function(dataObj){
// 	let map = IIFE();
	
// }












