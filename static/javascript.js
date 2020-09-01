function updateGPIO(gpio) {
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
}

function updateStates() {
    var server = new XMLHttpRequest();
    server.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            state = JSON.parse(server.responseText);
            for (var gpio in state) {
                document.getElementById(gpio).checked = state[gpio];
                console.log(state, gpio);
            }
        } else if (this.readyState == 4) {
            alert('Some error on the server, Try to reload');
        }
    }
    server.open('POST', '/state', true);
    server.send();
}

var updateState = setInterval(updateStates(), 1000);
