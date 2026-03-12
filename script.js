// script.js

// Load the local pokemon-data.json file
fetch('pokemon-data.json')
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }
        return response.json();
    })
    .then(data => {
        // Initialize game variables and logic
        const pokemons = data.pokemons; // Assuming JSON structure has a `pokemons` key.
        let score = 0;
        let gameActive = true;

        // Set up the game loop
        function gameLoop() {
            if (!gameActive) return;

            // Update game state here

            // Request the next frame
            requestAnimationFrame(gameLoop);
        }

        // Handle user interactions
        document.addEventListener('click', event => {
            if (gameActive) {
                // Logic for user interactions (e.g., selecting a pokemon)
            }
        });

        // Start the game loop
        gameLoop();

    })
    .catch(error => {
        console.error('There was a problem with the fetch operation:', error);
    });
