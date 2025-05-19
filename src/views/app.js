let currentExcuseText = null;
const API_URL = 'http://localhost:8080';

async function loadExcuses() {
    try {
        const response = await fetch(
            `${API_URL}/get-excuses?` + new URLSearchParams({
                numberOfExcuses: 0,
                needAll: true
            })
        );
        
        const excusesData = await response.json();
        const excuses = excusesData.map(([id, text, rank]) => ({ id, text, rank }));
        renderExcuses(excuses);
    } catch (error) {
        console.error('Error:', error);
    }
}

async function getNewExcuse() {
    try {
        const response = await fetch(`${API_URL}/generate-joke`);
        const data = await response.json();
        
        if (!data.joke || typeof data.id !== 'number') {
            throw new Error('Invalid response format');
        }
        
        const cleanJoke = data.joke.replace(/^["']+|["']+$/g, '');
        
        currentExcuseText = cleanJoke;
        sessionStorage.setItem('currentExcuseId', data.id);
        
        document.getElementById('currentExcuse').textContent = cleanJoke;
    } catch (error) {
        console.error('Error getting excuse:', error);
        alert('Error getting excuse!');
    }
}

async function rateExcuse(deltaRank) {
    if (!currentExcuseText) return;

    try {
        const params = new URLSearchParams({
            id: sessionStorage.getItem('currentExcuseId'),
            deltaRank: deltaRank
        });

        const response = await fetch(`${API_URL}/change-excuse-rank?${params}`, {
            method: 'POST'
        });

        if (response.ok) {
            await loadExcuses();
            await getNewExcuse();
        }
    } catch (error) {
        alert('Error: ' + error.message);
    }
}
function renderExcuses(excuses) {
    const tbody = document.getElementById('excusesList');
    tbody.innerHTML = excuses
        .sort((a, b) => b.rank - a.rank)
        .map(excuse => `
            <tr>
                <td>${excuse.text}</td>
                <td>${excuse.rank}</td>
            </tr>
        `).join('');

    document.querySelectorAll('#excusesList tr').forEach(row => {
        if (row.children[0].textContent === currentExcuseText) {
            row.style.background = '#fff3b0';
        }
    });
}

document.addEventListener('DOMContentLoaded', () => {
    loadExcuses();
    getNewExcuse();
});