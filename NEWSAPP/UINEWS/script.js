const API_KEY = ''; // Replace with your NewsAPI key
const newsContainer = document.getElementById('newsContainer');
const historyContainer = document.getElementById('historyContainer');
const searchInput = document.getElementById('searchInput');

// Load search history from localStorage
let searchHistory = JSON.parse(localStorage.getItem('newsSearchHistory')) || [];

// Display search history on load
displayHistory();

function displayHistory() {
    if (searchHistory.length === 0) {
        historyContainer.innerHTML = '<p class="no-history">No searches yet. Start exploring!</p>';
        return;
    }

    historyContainer.innerHTML = searchHistory
        .slice()
        .reverse()
        .map(term => `<div class="history-item" onclick="searchNewsByTerm('${term}')">${term}</div>`)
        .join('');
}

function handleKeyPress(event) {
    if (event.key === 'Enter') {
        searchNews();
    }
}

function searchNews() {
    const query = searchInput.value.trim();
    if (!query) {
        alert('Please enter a search term');
        return;
    }
    searchNewsByTerm(query);
}

function searchNewsByTerm(term) {
    // Add to history
    if (!searchHistory.includes(term)) {
        searchHistory.push(term);
        localStorage.setItem('newsSearchHistory', JSON.stringify(searchHistory));
        displayHistory();
    }

    searchInput.value = term;
    newsContainer.innerHTML = '<div class="spinner"></div><p class="loading-message">Searching for news...</p>';

    // Using NewsAPI.org - Replace with your API key
    const url = `https://newsapi.org/v2/everything?q=${encodeURIComponent(term)}&sortBy=publishedAt&language=en&pageSize=10`;

    // For demo purposes, showing mock data
    setTimeout(() => {
        displayMockNews(term);
    }, 1000);
}

function displayMockNews(query) {
    const mockArticles = [
        {
            title: `Latest developments in ${query}`,
            description: `Stay updated with the most recent news and updates about ${query}. Our comprehensive coverage ensures you don't miss important stories.`,
            urlToImage: null,
            source: { name: 'News Daily' },
            publishedAt: new Date().toISOString(),
            url: '#'
        },
        {
            title: `${query}: What you need to know today`,
            description: `Breaking news and analysis on ${query}. Get insights from leading experts and comprehensive reporting on this developing story.`,
            urlToImage: null,
            source: { name: 'Global News' },
            publishedAt: new Date(Date.now() - 3600000).toISOString(),
            url: '#'
        },
        {
            title: `Understanding the impact of ${query}`,
            description: `In-depth analysis of how ${query} affects industries and communities worldwide. Expert opinions and data-driven insights.`,
            urlToImage: null,
            source: { name: 'News Weekly' },
            publishedAt: new Date(Date.now() - 7200000).toISOString(),
            url: '#'
        },
        {
            title: `${query}: Market analysis and trends`,
            description: `Market experts discuss trends and predictions related to ${query}. Investment insights and economic impact analysis.`,
            urlToImage: null,
            source: { name: 'Business Times' },
            publishedAt: new Date(Date.now() - 10800000).toISOString(),
            url: '#'
        },
        {
            title: `Regional impact of ${query}`,
            description: `How ${query} is affecting different regions globally. Regional analysis and local perspectives on this important issue.`,
            urlToImage: null,
            source: { name: 'World News' },
            publishedAt: new Date(Date.now() - 14400000).toISOString(),
            url: '#'
        },
        {
            title: `Technology and ${query}`,
            description: `The intersection of technology and ${query}. Innovation updates and tech industry responses to recent developments.`,
            urlToImage: null,
            source: { name: 'Tech News' },
            publishedAt: new Date(Date.now() - 18000000).toISOString(),
            url: '#'
        },
        {
            title: `${query}: Social media buzz`,
            description: `How people are reacting to ${query} on social platforms. Trending discussions and public sentiment analysis.`,
            urlToImage: null,
            source: { name: 'Social Pulse' },
            publishedAt: new Date(Date.now() - 21600000).toISOString(),
            url: '#'
        },
        {
            title: `Future outlook on ${query}`,
            description: `What experts predict about the future of ${query}. Long-term implications and upcoming developments to watch.`,
            urlToImage: null,
            source: { name: 'Future Today' },
            publishedAt: new Date(Date.now() - 25200000).toISOString(),
            url: '#'
        },
        {
            title: `${query}: International perspective`,
            description: `How the international community views ${query}. Cross-border implications and global diplomatic responses.`,
            urlToImage: null,
            source: { name: 'International News' },
            publishedAt: new Date(Date.now() - 28800000).toISOString(),
            url: '#'
        },
        {
            title: `Success stories related to ${query}`,
            description: `Inspirational stories and positive outcomes connected to ${query}. Real-world examples and success metrics.`,
            urlToImage: null,
            source: { name: 'Positive News' },
            publishedAt: new Date(Date.now() - 32400000).toISOString(),
            url: '#'
        }
    ];

    displayNews(mockArticles);
}

function displayNews(articles) {
    if (!articles || articles.length === 0) {
        newsContainer.innerHTML = '<p class="loading-message">No news found. Try a different search term.</p>';
        return;
    }

    const newsHTML = articles.map((article, index) => {
        const date = new Date(article.publishedAt).toLocaleDateString('en-US', {
            year: 'numeric',
            month: 'short',
            day: 'numeric'
        });

        return `
            <div class="news-card" style="animation-delay: ${index * 0.1}s;">
                <div class="news-image placeholder">📰</div>
                <div class="news-content">
                    <div class="news-source">${article.source.name}</div>
                    <h3 class="news-title">${article.title}</h3>
                    <p class="news-description">${article.description}</p>
                    <div class="news-footer">
                        <span class="news-date">${date}</span>
                        <a href="${article.url}" target="_blank" class="news-link">Read More</a>
                    </div>
                </div>
            </div>
        `;
    }).join('');

    newsContainer.innerHTML = newsHTML;
}

function scrollToFooter() {
    const footer = document.getElementById('footer');
    footer.scrollIntoView({ behavior: 'smooth' });
}

// Optional: Add real API integration
async function fetchRealNews(query) {
    try {
        const response = await fetch(
            `https://newsapi.org/v2/everything?q=${encodeURIComponent(query)}&sortBy=publishedAt&language=en&pageSize=10&apiKey=${API_KEY}`
        );
        const data = await response.json();
        displayNews(data.articles);
    } catch (error) {
        console.error('Error fetching news:', error);
        displayMockNews(query);
    }
}