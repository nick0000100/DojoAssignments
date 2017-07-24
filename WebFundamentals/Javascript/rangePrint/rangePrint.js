printRange(2, 10, 2);

function printRange(start, end, skip) {
    for(var i = start; i < end; i += skip) {
        console.log(i);
    }
}