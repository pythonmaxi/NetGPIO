var useSocket
var socket
if (window.WebSocket) {
    useSocket = true;
    var location = window.location;
    socket = new WebSocket('ws://' + location.host + ':5000/socket');
    socket.onmessage = function (event) {
        if (event.data == 'changed') {
            updateStates();
        }
    }
} else {
    useSocket = false;
    alert('Your browser does not support WebSockets, multiple clients wont be supported');
}

var gpios = document.getElementsByClassName('gpios')
for (var i = 0; i < gpios.length; i++) {
    gpios[i].addEventListener('click', function (e) {
        if (useSocket == true) {
            socket.send('changed')
        }
        var gpio = e.target || e.srcElement;
        var state = gpio.checked;
        var name = gpio.id;
        var pin = gpio.name;
        var server = new XMLHttpRequest();
        server.onreadystatechange = function () {
            if (this.readyState == 4 && this.status == 200) {
                return;
            } else if (this.readyState == 4) {
                alert('Something failed!!');
            }
        }
        server.open('POST', '/');
        server.setRequestHeader('Content-Type', 'application/json');
        server.send(JSON.stringify({'pin': pin, 'state': state, 'name':name}));
    });
}

function updateStates() {
    var server = new XMLHttpRequest();
    server.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            state = JSON.parse(server.responseText);
            for (var gpio in state) {
                document.getElementById(gpio).checked = state[gpio]['state'];
                console.log(state, gpio);
            }
        } else if (this.readyState == 4) {
            alert('Some error on the server, Try to reload');
        }
    }
    server.open('POST', '/state', true);
    server.send();
}
