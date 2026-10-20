async function sendCommand(command) {
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log("Reply text: " + replyText);
    document.querySelector("#replyText").innerHTML = replyText;
    return response;
}

function main() {
    console.log("Hello JavaScript!");

    document.querySelector("#on").onclick = () => {
        console.log("LED On button clicked");
        sendCommand("led/on");
    };
    document.querySelector("#off").onclick = () => {
        console.log("LED Off button clicked");
        sendCommand("led/off");
    };
    document.querySelector("#flash").onclick = () => {
        console.log("Flash button clicked");
        let numflash = document.querySelector("#numflash").value;
        let period = document.querySelector("#period").value;
        sendCommand(`flash/${numflash}/${period}`);
    };
}

main();