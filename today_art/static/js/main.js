console.log("main.js loaded");

document.getElementById("fetchData").addEventListener("click", function () {
  // Fetch data from the server
  fetch("/api/data")
    .then((response) => response.json())
    .then((data) => {
      // Update the content of div with id "A"
      document.getElementById("A").innerText = data;
    })
    .catch((error) => {
      console.error("Error fetching data:", error);
    });
});
