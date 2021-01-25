function checkTemp () {
    //from nestIf.html
    var temp = prompt ("What temperature is it outside?")
    temp = parseInt (temp)

    if (temp < 60) {
        //less than 60
        if (temp < 32) {
            //less than 32
            alert ("It's Freezing!")
        } else {
            //between 32 and 60
            alert ("It's Cold!")
        } //end 'freezing if'
    } else {
        //We're over 60
        if (temp < 75) {
            //between 60 and 75
            alert ("It's cool.")
        } else {
            //Temp is higher than 75
            if (temp < 90) {
                //over 90
                alert ("It's hot!")
            } else {
                //between 75 and 90
                alert ("It's warm.")
            } // end over 90
        } // end over 75
    } // end over 60
} // end function