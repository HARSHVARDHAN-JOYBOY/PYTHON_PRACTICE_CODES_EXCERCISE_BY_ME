const searchBtn = document.getElementById('searchBtn');
const topicInput = document.getElementById('topic');
const newsContainer = document.getElementById('newsContainer');
const status = document.getElementById('status');

async function getNews() {
  const topic = topicInput.value.trim();
  if (!topic) {
    alert('Please enter a topic.');
    return;
  }
  status.classList.remove('hidden');
  status.textContent = 'Loading news...';
  newsContainer.innerHTML = '';

  try {
    const res = await fetch(`/news?topic=${encodeURIComponent(topic)}`);
    if (!res.ok) {
      const err = await res.json();
      status.textContent = 'Error: ' + (err.error || 'Failed');
      return;
    }
    const data = await res.json();
    status.classList.add('hidden');

    if (!Array.isArray(data) || data.length === 0) {
      newsContainer.innerHTML = '<p>No news found.</p>';
      return;
    }

    data.forEach((a, i) => {
      const item = document.createElement('div');
      item.className = 'news-item';

      const left = document.createElement('div');
      left.className = 'news-left';
      const title = document.createElement('h3');
      title.textContent = `${i+1}. ${a.title || 'No title'}`;
      left.appendChild(title);
      if (a.source) {
        const src = document.createElement('p');
        src.textContent = `Source: ${a.source}`;
        left.appendChild(src);
      }

      const right = document.createElement('div');
      right.className = 'news-right';
      const link = document.createElement('a');
      link.href = a.url || '#';
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = 'Open Article';
      right.appendChild(link);

      item.appendChild(left);
      item.appendChild(right);
      newsContainer.appendChild(item);
    });

  } catch (err) {
    status.textContent = 'Error: ' + err.message;
  }
}

searchBtn.addEventListener('click', getNews);
topicInput.addEventListener('keyup', e => { if (e.key === 'Enter') getNews(); });
