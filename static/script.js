document.addEventListener("DOMContentLoaded", function () {
    
    getLocation()
    
});

var baralat = ""
var baralongi = ""
var count = 0
var map;
var service;
var a
var b
var latlong = []
var distanciainicial = []
var distanciasi = []
var tempomedio = []
var nomes =[]

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
          count++
          localStorage.setItem('count',count)
          console.log(count)
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
            latlong.push([lat,long])
       
            nomes.push(s)
            calcularDistancia(lat,long)

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
                origins: [origin1],
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
                  
                  distanciainicial.push(distance)
                
                  var duration = element.duration.text;
                  var from = origins[i];
                  var to = destinations[j];
                }
              }
            }
          }

          function calcularDistanciaentrebares(latitude,longitude,lat,long,resultados,nomes)
          {
            var origin1 = new google.maps.LatLng(latitude,longitude);
            
           
            var destinationB = new google.maps.LatLng(lat, long);

            var service = new google.maps.DistanceMatrixService();
            service.getDistanceMatrix(
              {
                origins: [origin1,],
                destinations: [destinationB],
                travelMode: 'WALKING',
              }, function(response,status){
                if (status === 'OK') {
                  var results = response.rows[0].elements[0];
                  var distance = results.distance.text;
            
                  // Adicione o resultado ao array resultados
                  resultados.push([nomes,distance]);

                  if (resultados.length === latlong.length * latlong.length) {
                    passar(resultados)
                  }
                }
              });
          }

      
         function passar(mec)
         {
          
         
         
         
          for(var i = 0; i<distanciaa.length;i++)
          {
            var dist = distanciaa[i].replace(" km","")
            var b = dist.replace(",",".")
            document.getElementById("distanciaa").value+= "/"+ dist
           
          }
          console.log(document.getElementById("distanciaa").value)
         var qualquercoisa =""
          for(var i = 0 ; i < mec.length;i++)
          {
            var ai = mec[i]
            var dist = ai[1].replace(" km","")
            var b = dist.replace(",",".")
            var c = b.replace(" m","")
            if(c=="1")
            {
              
              continue
            }
            else{
              if(i==0)
              {
                document.getElementById("distanciasi").value += c
                document.getElementById("nomesbar").value += ai[0]
              }
              else{
                document.getElementById("distanciasi").value += "/"+c
                document.getElementById("nomesbar").value += "/"+ai[0]
              }
            }
            
          
            
          }
          
          console.log(document.getElementById("distanciasi").value)
          console.log(mec.length)
          for(var i = 0 ; i <nomes.length;i++)
          {
            document.getElementById("nomes").value+= ","+nomes[i]
            
          }
          console.log(document.getElementById("nomes").value)
          document.forms["form1"].submit()
         }
         function pegar5distancias()
         {
          var resultados = []
             for(var i = 0;i<latlong.length;i++)
             {
              
              for(var j = 0;j<latlong.length;j++)
              {
               
                
               
                
                var l = latlong[i]
                var l1 = latlong[j]
                var lat1 = l[0]
                var long1 = l[1]
                var lat2 = l1[0]
                var long2 = l1[1]
                var nome = nomes[j]
                calcularDistanciaentrebares(lat1,long1,lat2,long2,resultados,nome)
                
                

          
             }
            }
             
         }
        var but = document.getElementById("but")
         var mec = []
        but.addEventListener("click",function(){
          
          pegar5distancias()
          
         
        })
         /* function getDistance(marker) {
          var myLatLng = new google.maps.LatLng(a, b);
          var distance = google.maps.geometry.distanceBetween(
          myLatLng,
          marker.getPosition()
            );
          return distance;
          }*/
          //window.initMap = initMap()




 
