// Ask the user for input
let season = prompt("Enter the season (summer or winter)").toLowerCase();
let plantType = prompt("Enter the plant type (flower or vegetable)").toLowerCase();

let advice = "";

if (season === "summer") {
    advice += "Water your plants regularly and provide some shade.\n";
} else if (season === "winter") {
    advice += "Protect your plants from frost with covers.\n";
} else {
    advice += "No advice for this season.\n";
}

if (plantType === "flower") {
    advice += "Use fertiliser to encourage blooms.";
} else if (plantType === "vegetable") {
    advice += "Keep an eye out for pests!";
} else {
    advice += "No advice for this type of plant.";
}

alert("Your gardening advice:\n" + advice);
