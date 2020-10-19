var output = document.getElementById('output');
var socket = new WebSocket("wss://06dbwvi4b0.execute-api.ap-northeast-1.amazonaws.com/smmi_stage");

socket.onopen = function() {
    output.innerHTML += "お題は...\n";
};

socket.onmessage = function(e) {
    output.innerHTML += "お題：" + e.data + "\n";
};

function send() {
    socket.send(JSON.stringify(
    {
        "action":"get_petricipant",
    }
    ));
};