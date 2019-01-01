document.addEventListener("DOMContentLoaded", ready);

function ready() {

// Define a number to find out wiche player is playing
    player = 0;
    maindiv = document.getElementById("mainDiv")


    dot1 = document.getElementById("dot11")
    dot2 = document.getElementById("dot22")
    dot1.style.visibility = "visible"
    dot2.style.visibility = "hidden"

    var holdButton = document.getElementById("holdButton")

// This part for handle part 1 of extra
    score = document.getElementById("threshold")

    // threshold = 100
    //
    // score.onchange = function() {
    //     threshold = parseInt(score.value)
    //     console.log(threshold)
    // }
// Event on hold button
    holdButton.onclick = function() {


        var zeroTotalScore = document.getElementById("player0total").innerHTML
        var oneTotalScore = document.getElementById("player1total").innerHTML


        if (player == 0) {
            document.getElementById("player0total").innerHTML = parseInt(zeroTotalScore) + parseInt(document.getElementById("Cur1").innerHTML)
            document.getElementById("Cur1").innerHTML = 0
        }else {
            document.getElementById("player1total").innerHTML = parseInt(oneTotalScore) + parseInt(document.getElementById("Cur2").innerHTML)
            document.getElementById("Cur2").innerHTML = 0
        }

// Check for win
        if (parseInt(document.getElementById("player0total").innerHTML) >= threshold) {
            alert("PLAYER 0 WINS")
            alert("PLEASE PRESS <NEW GAME> BUTTON")
            document.getElementById("player0total").innerHTML = 0
            document.getElementById("player1total").innerHTML = 0
            document.getElementById("Cur1").innerHTML = 0
            document.getElementById("Cur2").innerHTML = 0
        }
        if (parseInt(document.getElementById("player1total").innerHTML) >= threshold) {
            alert("PLAYER 1 WINS")
            alert("PLEASE PRESS <NEW GAME> BUTTON")
            document.getElementById("player0total").innerHTML = 0
            document.getElementById("player1total").innerHTML = 0
            document.getElementById("Cur1").innerHTML = 0
            document.getElementById("Cur2").innerHTML = 0
        }
        

        if (maindiv.className == "mainDiv") {
            dot1.style.visibility = "hidden"
            dot2.style.visibility = "visible"
            player = 1;
            maindiv.className = "mainDiv2"
        }else {
            dot1.style.visibility = "visible"
            dot2.style.visibility = "hidden"
            player = 0;
            maindiv.className = "mainDiv"
        }
    }

    var rollButton = document.getElementById("rollButton")

// Event on rollDice button
    rollButton.onclick = function() {

// Generate random number to choose a dice
        var rand = Math.floor(Math.random() * 6) + 1
        var rand2 = Math.floor(Math.random() * 6) + 1
        // console.log(rand)
        // console.log(rand2)
        var diceImage = document.getElementById("dice")
        var diceImage2 = document.getElementById("dice2")

// Start 
        diceImage.style.visibility = "visible"
        diceImage2.style.visibility = "visible"

        if (player == 0) {
            var cur1 = document.getElementById("Cur1").innerHTML

// This part for handle part 3 of extra 
            if (rand == 1 || rand2 == 1) {
                if (rand == 1 && rand2 == 1) {
                    diceImage.setAttribute("src","/static/pic/dice-1.png")
                    diceImage2.setAttribute("src","/static/pic/dice-1.png")
                }else if (rand == 1) {
                    diceImage.setAttribute("src","/static/pic/dice-1.png")
                    for (let index = 1; index < 7; index++) {
                        if (rand2 == index) {
                            var pic = "/static/pic/dice-"+index+".png"
                            diceImage2.setAttribute("src",pic)
                        }
                    }
                }else {
                    diceImage2.setAttribute("src","/static/pic/dice-1.png")
                    for (let index = 1; index < 7; index++) {
                        if (rand == index) {
                            var picc = "/static/pic/dice-"+index+".png"
                            diceImage.setAttribute("src",picc)
                        }
                    }
                }
                dot1.style.visibility = "hidden"
                dot2.style.visibility = "visible"
                player = 1
                document.getElementById("Cur1").innerHTML = 0
                maindiv.className = "mainDiv2"
            } 
            else {

                if (rand == 2) {
                    diceImage.setAttribute("src","/static/pic/dice-2.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 2

                }else if (rand == 3) {
                    diceImage.setAttribute("src","/static/pic/dice-3.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 3

                }else if (rand == 4) {
                    diceImage.setAttribute("src","/static/pic/dice-4.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 4

                }else if (rand == 5) {
                    diceImage.setAttribute("src","/static/pic/dice-5.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 5

                }else if (rand == 6) {
                    diceImage.setAttribute("src","/static/pic/dice-6.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 6

                }
    // dice 2
                if (rand2 == 2) {
                    diceImage2.setAttribute("src","/static/pic/dice-2.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 2

                }else if (rand2 == 3) {
                    diceImage2.setAttribute("src","/static/pic/dice-3.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 3

                }else if (rand2 == 4) {
                    diceImage2.setAttribute("src","/static/pic/dice-4.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 4

                }else if (rand2 == 5) {
                    diceImage2.setAttribute("src","/static/pic/dice-5.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 5

                }else if (rand2 == 6) {
                    diceImage2.setAttribute("src","/static/pic/dice-6.png")
                    document.getElementById("Cur1").innerHTML = parseInt(document.getElementById("Cur1").innerHTML) + 6

                }
           }   

        } else {
            var cur2 = document.getElementById("Cur2").innerHTML

            if (rand == 1 || rand2 == 1) {
                if (rand == 1 && rand2 == 1) {
                    diceImage.setAttribute("src","/static/pic/dice-1.png")
                    diceImage2.setAttribute("src","/static/pic/dice-1.png")
                }else if (rand == 1) {
                    diceImage.setAttribute("src","/static/pic/dice-1.png")
                    for (let index = 1; index < 7; index++) {
                        if (rand2 == index) {
                            var pic = "/static/pic/dice-"+index+".png"
                            diceImage2.setAttribute("src",pic)
                        }
                    }
                }else {
                    diceImage2.setAttribute("src","/static/pic/dice-1.png")
                    for (let index = 1; index < 7; index++) {
                        if (rand == index) {
                            var picc = "/static/pic/dice-"+index+".png"
                            diceImage.setAttribute("src",picc)
                        }
                    }
                }
                dot1.style.visibility = "visible"
                dot2.style.visibility = "hidden"
                player = 0
                document.getElementById("Cur2").innerHTML = 0
                maindiv.className = "mainDiv"
            }
            else {

                if (rand == 2) {
                    diceImage.setAttribute("src","/static/pic/dice-2.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 2

                }else if (rand == 3) {
                    diceImage.setAttribute("src","/static/pic/dice-3.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 3

                }else if (rand == 4) {
                    diceImage.setAttribute("src","/static/pic/dice-4.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 4

                }else if (rand == 5) {
                    diceImage.setAttribute("src","/static/pic/dice-5.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 5

                }else if (rand == 6) {
                    diceImage.setAttribute("src","/static/pic/dice-6.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 6

                }
                // dice 2
                if (rand2 == 2) {
                    diceImage2.setAttribute("src","/static/pic/dice-2.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 2

                }else if (rand2 == 3) {
                    diceImage2.setAttribute("src","/static/pic/dice-3.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 3

                }else if (rand2 == 4) {
                    diceImage2.setAttribute("src","/static/pic/dice-4.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 4

                }else if (rand2 == 5) {
                    diceImage2.setAttribute("src","/static/pic/dice-5.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 5

                }else if (rand2 == 6) {
                    diceImage2.setAttribute("src","/static/pic/dice-6.png")
                    document.getElementById("Cur2").innerHTML = parseInt(document.getElementById("Cur2").innerHTML) + 6

                }
            }
        }
    }


    var newGame = document.getElementById("newGame")

// Event on newGame button
    newGame.onclick = function() {
// Reset all of variables
        alert("NEW GAME !")
        player = 0
        maindiv.className = "mainDiv"
        dot1.style.visibility = "visible"
        dot2.style.visibility = "hidden"
        document.getElementById("player0total").innerHTML = 0
        document.getElementById("player1total").innerHTML = 0
        document.getElementById("Cur1").innerHTML = 0
        document.getElementById("Cur2").innerHTML = 0
        document.getElementById("dice").style.visibility = "hidden"
        document.getElementById("dice2").style.visibility = "hidden"
        threshold = 100
        score.value = "Score"
    }
}