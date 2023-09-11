document.addEventListener("DOMContentLoaded", function () {
    
    getLocation()
});
var map;
var service;
var a
var b
var distancia = [0]
var tempomedio = [0]

    function getLocation() {

  navigator.geolocation.getCurrentPosition(
    function(position) {
    var places = google.maps.places;
      var location = position;
        
    var latitude = position.coords.latitude;
     var longitude = position.coords.longitude;
     a = latitude
     b = longitude
    

    initMap(latitude,longitude)
    
    },
    function(error) {
    
      console.log(error);
    }
  );
}





function initMap(latitude,longitude) {
            const lugar = new google.maps.LatLng(latitude,longitude);
            infowindow = new google.maps.InfoWindow();
            map = new google.maps.Map(document.getElementById("map"), {
                center: lugar,
                zoom: 15,
            });
          
            var request = {
            location: lugar,
            radius: '5000',
            type: ['bar']
            };
          
            service = new google.maps.places.PlacesService(map);
            service.nearbySearch(request, callbacki);
          }
          function callbacki(results, status) {
          if (status == google.maps.places.PlacesServiceStatus.OK) {
          for (var i = 0; i < results.length; i++) {
          createMarker(results[i]);
          }
        }
}
          
          function createMarker(place) {
            if (!place.geometry || !place.geometry.location) return;
          
            const marker = new google.maps.Marker({
              map,
              position: place.geometry.location,
              title: place.name
            });
          var s = place.name
            /*marker.setTitle(place.name)
            marker.setLabelTextStyle({
             color: "red",
             fontSize: "16px",
              });
              */
            var lat = marker.getPosition().lat()
            var long = marker.getPosition().lng()
           
            calcularDistancia(lat,long)
            console.log(lat, long)
              
            const infowindow = new google.maps.InfoWindow({
               content: s,
              ariaLabel: "",
                   });
            marker.addListener("click", () => {
              infowindow.open({
              anchor: marker,
              map,
              });
            });

          }
          function calcularDistancia(latitude,longitude)
          {
            var origin1 = new google.maps.LatLng(a,b);
            
           
            var destinationB = new google.maps.LatLng(latitude, longitude);

            var service = new google.maps.DistanceMatrixService();
            service.getDistanceMatrix(
              {
                origins: [origin1,],
                destinations: [destinationB],
                travelMode: 'WALKING',
              }, callback);
          }
         
          function callback(response, status) {
            if (status == 'OK') {
              var origins = response.originAddresses;
              var destinations = response.destinationAddresses;

              for (var i = 0; i < origins.length; i++) {
                var results = response.rows[i].elements;
                for (var j = 0; j < results.length; j++) {
                  var element = results[j];
                  var distance = element.distance.text;
                  console.log(distance)
                  distancia.push(distance)
                  var duration = element.duration.text;
                  console.log(duration)
                  tempomedio.push(duration)
                  var from = origins[i];
                  var to = destinations[j];
                }
              }
            }
          }
        
          
         /* function getDistance(marker) {
          var myLatLng = new google.maps.LatLng(a, b);
          var distance = google.maps.geometry.distanceBetween(
          myLatLng,
          marker.getPosition()
            );
          return distance;
          }*/
          //window.initMap = initMap()




 