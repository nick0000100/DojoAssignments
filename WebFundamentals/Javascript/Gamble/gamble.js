function gamble(quarters) {
    var win = Math.trunc(Math.random() * 100);
    while(quarters != 0) {    
        if(win < 1) {
            quarters += (Math.floor(Math.random * 50) + 50);
        }else {
            quarters--;
        }
    }
    if(quarters === 0) {
        console.log("end");
        return 0;
    }
}