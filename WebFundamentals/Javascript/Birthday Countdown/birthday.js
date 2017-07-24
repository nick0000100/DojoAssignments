var daysUntilMyBirthday = 0;

countDown(daysUntilMyBirthday);

function countDown(daysUntilMyBirthday) {
    if(daysUntilMyBirthday > 30) {
        console.log(daysUntilMyBirthday + " days until my birthday. Such a long time ... :(");
    }else if(daysUntilMyBirthday > 5) {
        console.log(daysUntilMyBirthday + " days until my birthday. It is coming soon!");
    }else if(daysUntilMyBirthday == 0) {
        console.log("HAAPY BIRTHDAY!");
    }else if (daysUntilMyBirthday == 1) {
        console.log(daysUntilMyBirthday + " DAY UNTIL MY BIRTHDAY!!!!!")
    }
    else {
        console.log(daysUntilMyBirthday + " DAYS UNTIL MY BIRTHDAY!!");
    }
}