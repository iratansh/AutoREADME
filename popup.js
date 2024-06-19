document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("generateButton").addEventListener("click", () => {
      const code = document.getElementById("inputBox").value;
      fetch("http://localhost:5002/generate_readme", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code })
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById("output").innerText = data.readme;
        document.getElementById("output").style.display = "block";  
        document.getElementById("InputBox").innerText = "";
      })
      .catch(error => {
        console.error("Error:", error);
      });
    });
  });
  