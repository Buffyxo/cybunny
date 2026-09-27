const patterns = {

    C: [
        "11111",
        "10000",
        "10000",
        "10000",
        "10000",
        "10000",
        "11111"
    ],

    Y: [
        "10001",
        "10001",
        "01010",
        "00100",
        "00100",
        "00100",
        "00100"
    ],

    B: [
        "11110",
        "10001",
        "10001",
        "11110",
        "10001",
        "10001",
        "11110"
    ],

    U: [
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "10001",
        "11111"
    ],

    N: [
        "10001",
        "11001",
        "11001",
        "10101",
        "10011",
        "10011",
        "10001"
    ]
};


const word = "CYBUNNY";

const container = document.getElementById("pixel-word");

let pixelNumber = 0;


for (const character of word) {

    const letter = document.createElement("div");

    letter.className = "letter";


    for (const row of patterns[character]) {

        for (const cell of row) {

            const square = document.createElement("span");

            if (cell === "1") {

                square.className = "pixel";

                square.style.animationDelay =
                    `${-(pixelNumber % 15) * 0.1}s`;

                square.style.animationDuration =
                    `${1.2 + (pixelNumber % 8) * 0.1}s`;

                pixelNumber++;

            } else {

                square.className = "empty";

            }

            letter.appendChild(square);
        }
    }

    container.appendChild(letter);
}