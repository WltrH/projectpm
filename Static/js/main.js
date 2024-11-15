function sendMessage() {
    const userInput = document.getElementById('userInput');
    const message = userInput.value.trim();
    
    if (message) {
        // Afficher le message de l'utilisateur
        addMessageToChat('user', message);
        
        // Envoyer la requête au serveur
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: message })
        })
        .then(response => response.json())
        .then(data => {
            // Afficher la réponse de l'IA
            addMessageToChat('ai', data.response);
        })
        .catch(error => {
            console.error('Erreur:', error);
            addMessageToChat('ai', 'Désolé, une erreur est survenue.');
        });
        
        userInput.value = '';
    }
}

function addMessageToChat(sender, message) {
    const chatBox = document.getElementById('chatBox');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}-message`;
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Permettre l'envoi avec la touche Entrée
document.getElementById('userInput').addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
});