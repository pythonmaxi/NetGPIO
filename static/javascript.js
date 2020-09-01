function updateGPIO(gpio) {
    var state = gpio.checked;
    var name = gpio.name;
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
    server.send(JSON.stringify({'pin': name, 'state': state}));
}

if (window.Worker) {
    var waiter = new Worker('/static/worker.js');
} else {
    alert('Your browser does not support workers. multi client mode will not work');
}
