const burger = document.getElementById('burger');
const sideMenu = document.getElementById('side-menu');

// Generate excuse when button is clicked
document.getElementById("generate").addEventListener("click", () => {
  fetchExcuse(); // Call API to get a new excuse
});

// Fetch a new excuse from the API
async function fetchExcuse() {
  try {
    const response = await fetch('http://localhost:8080/generate-joke');
    if (!response.ok) throw new Error('Failed to fetch joke');
    const data = await response.json();
    document.getElementById("excuse-box").textContent = data[0]?.excuse; // Display the excuse
  } catch (err) {
    console.error("Failed to fetch excuse:", err);
  }
}

// Fetch and display the rankings of excuses
async function fetchRankings() {
  try {
    const response = await fetch('http://localhost:8080/get-excuses');
    const data = await response.json();
    const tbody = document.querySelector('#ranking-table tbody');
    tbody.innerHTML = '';

    data.forEach(item => {
      const tr = document.createElement('tr');

      const excuseTd = document.createElement('td');
      excuseTd.textContent = item.excuse;
      tr.appendChild(excuseTd);

      const votesTd = document.createElement('td');
      votesTd.textContent = item.votes;
      tr.appendChild(votesTd);

      const actionTd = document.createElement('td');
      const upBtn = document.createElement('button');
      upBtn.textContent = '+1';
      upBtn.className = 'vote-btn';
      upBtn.onclick = () => vote(item.id, 1);

      const downBtn = document.createElement('button');
      downBtn.textContent = '-1';
      downBtn.className = 'vote-btn';
      downBtn.onclick = () => vote(item.id, -1);

      actionTd.appendChild(upBtn);
      actionTd.appendChild(downBtn);
      tr.appendChild(actionTd);

      tbody.appendChild(tr);
    });
  } catch (err) {
    console.error("Failed to load rankings:", err);
  }
}

// Vote up or down for an excuse
async function vote(id, value) {
  try {
    await fetch(`http://localhost:8080/change-excuse-rank`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ id, vote: value })
    });
    fetchRankings();
  } catch (err) {
    console.error("Voting failed:", err);
  }
}

// Toggle between light and dark themes
document.getElementById("toggle-theme").addEventListener("click", () => {
  document.body.classList.toggle("dark");
});

// Toggle the burger menu
document.querySelector(".burger").addEventListener("click", () => {
  const menu = document.getElementById("burger-menu");
  menu.classList.toggle("active");
});

// Close menu on link click
document.querySelectorAll(".sidebar-menu a").forEach(link => {
  link.addEventListener("click", () => {
    document.getElementById("burger-menu").classList.remove("active");
  });
});

// Toggle burger menu open/close
burger.addEventListener('click', () => {
  burger.classList.toggle('open');
  sideMenu.classList.toggle('active');
});

// Initialize rankings on page load
window.onload = fetchRankings;
