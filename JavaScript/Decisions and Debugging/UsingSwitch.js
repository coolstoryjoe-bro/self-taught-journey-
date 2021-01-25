function checkName() {
    //from switch.html
    var name = prompt ("What is your name?")

    switch(name) {
        case "Bill Gates":
            alert("Thanks for MS Bill!")
            break
        case "Steve Jobs":
            alert("Thanks for OSX Steve!")
            break
        default:
            alert("Do I know you?")
    } // end
} // end checkName