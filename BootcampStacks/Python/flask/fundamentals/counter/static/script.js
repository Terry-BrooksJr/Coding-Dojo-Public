function add() {
    accumulator = document.getElementByName('accumulator').innerHTML;
    accumulator = Number(accumulator);
    accumulator =+ accumulator+1;
    return accumulator;
}

function reset() {
    document.getElementByName('accumulator').innerText = "0";
}