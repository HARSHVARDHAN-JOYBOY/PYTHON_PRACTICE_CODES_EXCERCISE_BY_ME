const searchBtn = document.getElementById("searchBtn");
const topicInput = document.getElementById("topic");
const sortSelect = document.getElementById("sort");
const newsContainer = document.getElementById("newsContainer");
const loader = document.getElementById("loader");
const themeToggle = document.getElementById("themeToggle");

// THEME MODE
themeToggle.onclick = () => {
  document.body.classList.toggle("light");
  themeToggle.textContent =
    document.body.classList.contains("light")
      ? "🌙 Dark Mode"
      : "☀️ Light Mode";
};

// FETCH NEWS
async function getNews() {
  const topic = topicInput.value.trim();
  const sort = sortSelect.value;

  if (!topic) {
    alert("Please enter a topic.");
    return;
  }

  loader.style.display = "block";
  newsContainer.innerHTML = "";

  try {
    const res = await fetch(`/news?topic=${encodeURIComponent(topic)}&sort=${sort}`);
    const data = await res.json();

    loader.style.display = "none";

    if (!res.ok) {
      newsContainer.innerHTML = `<p>Error: ${data.error}</p>`;
      return;
    }

    data.forEach((a, i) => {
      const item = document.createElement("div");
      item.className = "news-item";

      item.innerHTML = `
        <div>
          <h3>${i + 1}. ${a.title}</h3>
          <p>Source: ${a.source}</p>
        </div>
        <div>
          <a href="${a.url}" target="_blank">Read More →</a>
        </div>
      `;

      newsContainer.appendChild(item);
    });

  } catch (err) {
    loader.style.display = "none";
    newsContainer.innerHTML = `<p>Error: ${err.message}</p>`;
  }
}

searchBtn.onclick = getNews;
topicInput.addEventListener("keyup", (e) => {
  if (e.key === "Enter") getNews();
});
