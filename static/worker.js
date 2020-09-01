function updateStates(state) {
    for (var gpio in state) {
        document.getElementById(gpio).checked = state[gpio];
    }
}

while (true) {
    var server = new XMLHttpRequest();
    server.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            updateStates(JSON.parse(server.responseText));
        } else if (this.readyState == 4) {
            alert('Some error on the server, Try to reload');
        }
    }
    server.open('POST', '/waitevent', true);
    server.send();
}
