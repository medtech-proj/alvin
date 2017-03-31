

// $(document).ready(function(){
// 	console.log("Document ready");
// 	$("#searchbar").keypress(function (enter) {
// 		if enter.which == 13{
// 			$('#searchbar').submit();
//     		alert('you pressed enter')
//     		return false;
// 		};
// 		// data = $("#searchbar");
// 		// $.ajax({
// 		// 	method:"POST",
// 		// 	// url: "/tweet",
// 		// 	data: data,
// 		// 	success: function(response) {
// 		// 		console.log(response);
// 		// 	}
// 		// });
// 	});
// });



//input submitted on 'enter'
// $('.input').keypress(function (e) {
//   if (e.which == 13) {
//     $('search').submit();
//     alert('search')
//     return false;
//   }
// });
import {IFFE} from './gmaps.js'


document.getElementById('searchSub').addEventListener('click', function(event){
		event.preventDefault();
		console.log('click')
		var name = document.querySelector('#searchInput').value

		console.log(name);
		var data =searchBar(name);
		console.log(data)

})

const searchBar = function(name){
	var data;
	var url = '/procedure/'+name;	
	var xhttp= new XMLHttpRequest();
		xhttp.onreadystatechange=function(){
			if(this.readyState==4 && this.status==200){
				data = JSON.parse(this.responseText);
				
			}

			// var newData= data.split(',');

			// console.log(newData);
		};
		xhttp.open("GET", url, true);
		xhttp.send()
}


var getMap = function(dataObj){
	

}












