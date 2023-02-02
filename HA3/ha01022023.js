// Aufgabe 1

function dreieckF (a, b, c) {
    let s = (a + b + c) / 2;
    console.log(s);
    let z = s * (s - a) * (s - b) * (s - c);
    console.log(z);
    let A = Math.sqrt(z);
    console.log(A);
    if (isNaN(A)) {
        return ("Die Eingabe ergibt kein Dreieck!!");
    }
    else {
        return A;
    }
}
console.log(dreieckF(17, 16, 15));

// Aufgabe 2

function techstarter () {
    console.log("Techstarter");
}
setInterval(techstarter, 2000)

// Aufgabe 3

function diff (x) {
    let y = x - 13;
    console.log(y);
    if (y  >= 0) {
        let z = 2 * y;
        // console.log(z);
        return z;
    }
    else {
        // console.log(y);
        return y;
    }
}
console.log(diff(13));

// Aufgabe 4

function bereich (a, b) {
    if ((a >= 50 && a <= 90) || (b >= 50 && b <= 90)) {
        // console.log("True");
        return true;
    }
    else {
        // console.log("False");
        return false;
    }
}
console.log(bereich(107, 107));

// Aufgabe 5

function ausgabe (n) {
    myArray = [27, "Schnitzel", 109, "Steak", 333];
    let item = myArray[n - 1];
    return item;
}
console.log(ausgabe(5))

// Aufgabe 6

function palindrom (name) {
    name = name.toLowerCase();
    console.log(name);
    let myArray = name.split("");
    console.log(myArray);
    let myReverseArray = myArray.slice().reverse();
    console.log(myReverseArray);
    console.log(myArray);
    if (JSON.stringify(myArray) === JSON.stringify(myReverseArray)) {
        return ("Das ist ein Palindrom!");
    }
    else {
        return ("Das ist kein Palindrom!");
    }
}
console.log(palindrom("Lagerregal"));

// Aufgabe 7

function combi(str) {
    let result = [];
    let counter = 0;
    let strLength = str.length;
    while (counter < strLength) {
        let char = str.charAt(counter);
        let x;
        let arrayTemp =[char];
        for (x in result) {
            arrayTemp.push("" + result[x] + char);
        }
        result = result.concat(arrayTemp);
        counter += 1;
    }
    return result;
}
console.log(combi("dieter"));

// Aufgabe 8

let myArray = [1, 2, 2, 3, 4, 4, 5];

function remDup(myArray) {
    return myArray.filter((item, index) => myArray.indexOf(item) === index);
}
console.log(remDup(myArray));

// Aufgabe 9

function first(a, b = 1) {
    let myArray = a.splice(0, b);
    return myArray;
}
console.log(first([7, 9, 0, -2]));
console.log(first([], 3));
console.log(first([7, 9, 0, -2], 3));
console.log(first([7, 9, 0, -2], 6));
console.log(first([7, 9, 0, -2], -3));

// Aufgabe 10

let myArray = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];
function shuffle() {
    newArray = myArray.sort(() => Math.random() - 0.5);
    return newArray;
}
console.log(shuffle());
