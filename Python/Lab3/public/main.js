async function sendCommand(command) {
    var response = await fetch(`/api/${command}`);
    var replyText = await response.text();
    console.log("Reply text: " + replyText);
    document.querySelector("#replyText").innerHTML = replyText;
    return response;
}

function main() {
    console.log("Hello JavaScript!");

    document.querySelector("#reset").onclick = () => {
        console.log("Reset button clicked");
        sendCommand("RESET");
    };
    document.querySelector("#x1").onclick = () => {
        console.log("X-AXIS 1 button clicked");
        sendCommand("X-AXIS 1");
    };
    document.querySelector("#x2").onclick = () => {
        console.log("X-AXIS 2 button clicked");
        sendCommand("X-AXIS 2");
    };
    document.querySelector("#x3").onclick = () => {
        console.log("X-AXIS 3 button clicked");
        sendCommand("X-AXIS 3");
    };
    document.querySelector("#x4").onclick = () => {
        console.log("X-AXIS 4 button clicked");
        sendCommand("X-AXIS 4");
    };
    document.querySelector("#x5").onclick = () => {
        console.log("X-AXIS 5 button clicked");
        sendCommand("X-AXIS 5");
    };
    document.querySelector("#z1").onclick = () => {
        console.log("Z-AXIS EXTEND button clicked");
        sendCommand("Z-AXIS EXTEND");
    };
    document.querySelector("#z2").onclick = () => {
        console.log("Z-AXIS RETRACT button clicked");
        sendCommand("Z-AXIS RETRACT");
    };
    document.querySelector("#g1").onclick = () => {
        console.log("Gripper OPEN button clicked");
        sendCommand("Gripper OPEN");
    };
    document.querySelector("#g2").onclick = () => {
        console.log("Gripper CLOSE button clicked");
        sendCommand("Gripper CLOSE");
    };
    document.querySelector("#move").onclick = () => {
        console.log("Plate button clicked");
        let startpos = document.querySelector("#p1").value;
        let endpos = document.querySelector("#p2").value;
        sendCommand(`MOVE ${startpos} ${endpos}`);
    }
}

main();
