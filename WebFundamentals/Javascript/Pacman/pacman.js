$(document).ready(function() {
    displayWorld();
    displayPacman();
    displayScore();
});


// var world = [
//     [2,2,2,2,2,2,2,2,2,2,2,2],
//     [2,1,1,1,1,2,1,1,1,1,1,2],
//     [2,1,1,1,1,2,1,1,1,1,1,2],
//     [2,1,1,1,1,1,2,1,1,1,1,2],
//     [2,1,1,1,1,1,2,1,1,1,1,2],
//     [2,1,1,1,1,1,2,1,1,1,1,2],
//     [2,1,1,1,1,1,1,2,1,1,1,2],
//     [2,1,1,1,1,1,1,2,1,1,1,2],
//     [2,1,1,1,1,1,1,1,2,1,1,2],
//     [2,2,2,2,2,2,2,2,2,2,2,2]
// ];

var world = makeWorld(20, 25);

function makeWorld(height,width) {
    var border = []
    var coins = [];
    for(var i = 0; i <= width + 4; i++) {
        border.push(2);
        coins.push(1);
    }
    var world = [];
    world.push(border);
    world.push(coins);
    var long = [2,1];
    for(var i = 0; i <= height; i++) {
        for(var j = 0; j <= width; j++) {
            var rand = (Math.random() * 2) + 1;
            var blockType = Math.floor(rand);
            console.log(blockType);
            long.push(blockType);
        }
        long.push(1);
        long.push(2);
        world.push(long);
        long = [2,1];
    }
    coins[0] = 2;
    coins[coins.length -1] = 2;    
    world.push(coins);
    world.push(border);
    return world;
}

function displayWorld() {
    var output = "";
    for(var i = 0; i <= world.length - 1; i++) {
        output += "\n<div class='row'>"
        for(var j = 0; j <= world[i].length - 1; j++) {
            if(world[i][j] == 2) {
                output += "\n\t<div class='brick'></div>";
            }else if(world[i][j] == 1) {
                output += "\n\t<div class='coin'></div>";
            }else if(world[i][j] == 0) {
                output += "\n\t<div class='empty'></div>";
            }
        }
        output += "\n</div>";
    }
    // console.log(output);
    document.getElementById("world").innerHTML = output;
};

var pacman = {
    x: 1,
    y: 1
};

function displayPacman() {
    document.getElementById("pacman").style.top = pacman.y*25+"px";
    document.getElementById("pacman").style.left = pacman.x*25+"px";
}

var score = 0;

function displayScore() {
    document.getElementById("score").innerHTML = score;
}

document.onkeydown = function(e) {
    if(e.keyCode == 37 && world[pacman.y][pacman.x-1] != 2) {
        pacman.x--;
        $("#pacman").attr('class', 'left');
    }else if(e.keyCode == 39 && world[pacman.y][pacman.x+1] != 2) {
        pacman.x++;
        $("#pacman").attr('class', 'right');
    }else if(e.keyCode == 38 && world[pacman.y-1][pacman.x] != 2) {
        pacman.y--;
        $("#pacman").attr('class', 'up');
    }else if(e.keyCode == 40 && world[pacman.y+1][pacman.x] != 2) {
        pacman.y++;
        $("#pacman").attr('class', 'down');
    }

    if(world[pacman.y][pacman.x] == 1) {
        world[pacman.y][pacman.x] = 0;
        score += 10;
        displayScore();
        displayWorld();
    }
    // console.log(e.keyCode);
    displayPacman();
}