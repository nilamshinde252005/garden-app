
const SEASON_TIPS = {
  summer: "Water your plants regularly and provide some shade.",
  winter: "Protect your plants from frost with covers.",
};

const PLANT_TIPS = {
  flower: "Use fertiliser to encourage blooms.",
  vegetable: "Keep an eye out for pests!",
};

function normalise(text) {
  return (text || "").trim().toLowerCase();
}

function adviceFor(season, plantType) {
  const s = normalise(season);
  const p = normalise(plantType);

  const seasonLine = SEASON_TIPS[s] || "No advice for this season.";
  const plantLine  = PLANT_TIPS[p] || "No advice for this type of plant.";

  return `${seasonLine}\n${plantLine}`;
}


function main() {
  const season = prompt("Enter the season (e.g., summer / winter)");
  const plant  = prompt("Enter the plant type (e.g., flower / vegetable)");
  alert("Your gardening advice:\n" + adviceFor(season, plant));
}
