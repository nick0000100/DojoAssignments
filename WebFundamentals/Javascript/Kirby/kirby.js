$(document).ready(function() {
    displayWorld();
    displaykirby();
    addEnemy();
    // displayScore();
});


var world = [
    [1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,2,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,0,0,1],
    [1,0,0,2,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1]
];

var score = 0;

function displayScore() {
    $("#score").html(score);
}

// var world = makeWorld(20, 25);

// function makeWorld(height,width) {
//     var border = []
//     var coins = [];
//     for(var i = 0; i <= width + 4; i++) {
//         border.push(2);
//         coins.push(1);
//     }
//     var world = [];
//     world.push(border);
//     world.push(coins);
//     var long = [2,1];
//     for(var i = 0; i <= height; i++) {
//         for(var j = 0; j <= width; j++) {
//             var rand = (Math.random() * 2) + 1;
//             var blockType = Math.floor(rand);
//             console.log(blockType);
//             long.push(blockType);
//         }
//         long.push(1);
//         long.push(2);
//         world.push(long);
//         long = [2,1];
//     }
//     coins[0] = 2;
//     coins[coins.length -1] = 2;    
//     world.push(coins);
//     world.push(border);
//     return world;
// }

function displayWorld() {
    var output = "";
    for(var i = 0; i <= world.length - 1; i++) {
        output += "\n<div class='row'>\n"
        for(var j = 0; j <= world[i].length - 1; j++) {
            if(world[i][j] == 1) {
                output += "<div class='wall'></div>";
            }else if(world[i][j] == 0) {
                output += "<div class='empty'></div>";
            }else if(world[i][j] == 2) {
                output += "<div class='enemy'></div>";
            }
        }
        output += "\n</div>";
    }
    $("#world").html(output);
};

var kirby = {
    x: 1,
    y: 1
};

function displaykirby() {
    $("#kirby").css("top", kirby.y*20 + "px");
    $("#kirby").css("left", kirby.x*20 + "px");
}


document.onkeydown = function(e) {
    if(e.keyCode == 37 && world[kirby.y][kirby.x-1] != 1) {
        kirby.x--;
        $("#kirby").attr('class', 'left');
    }else if(e.keyCode == 39 && world[kirby.y][kirby.x+1] != 1) {
        kirby.x++;
        $("#kirby").attr('class', 'right');
    }else if(e.keyCode == 38 && world[kirby.y-1][kirby.x] != 1) {
        kirby.y--;
        $("#kirby").attr('class', 'up');
    }else if(e.keyCode == 40 && world[kirby.y+1][kirby.x] != 1) {
        kirby.y++;
        $("#kirby").attr('class', 'down');
    }
    if(e.keyCode == 32) {
        // $("#kirby").attr('class', 'suck');
        $("#kirby").addClass("suck");
    }

    // if(world[kirby.y][kirby.x] == 1) {
    //     world[kirby.y][kirby.x] = 0;
    //     score += 10;
    // displayScore();
    // displayWorld();
    // }
    //  console.log(e.keyCode);
    displaykirby();
}

function addEnemy() {
    for(var i = 0; i < world.length; i++) {
        for(var j =0; j < world.length; j++) {
            if($(world[i][j]).hasClass("enemy")) {
                //create enemy in space top = i*20 && j*20
                console.log("hi");
                $("#world").append("<div class='snowman' style='position:absolute; top:"+(i*20)+"px;left:"+(j*20)+"px;></div>");
            }
        }
    }

}

/*
check if there is an enemy to the against the direction class
check position of enemy


*/