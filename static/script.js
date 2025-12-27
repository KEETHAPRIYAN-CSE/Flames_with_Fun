async function calculateFlames() {
  const name1 = document.getElementById("name1").value.trim();
  const name2 = document.getElementById("name2").value.trim();
  const resultDiv = document.getElementById("result");

  if (!name1 || !name2) {
    resultDiv.innerText = "✨ Please enter both names";
    return;
  }

  try {
    const response = await fetch("/flames", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ name1, name2 })
    });

    const data = await response.json();
    resultDiv.innerHTML = `💫 Relationship: <strong>${data.relationship}</strong>`;

  } catch (error) {
    resultDiv.innerText = "⚠️ Something went wrong";
  }
}
    