document.getElementById("search-form").addEventListener("submit", function (e) {
    e.preventDefault();
    const city = document.getElementById("city").value;
    fetch(`/weather?city=${city}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("weather-result").innerText = data.error;
            } else {
                document.getElementById("weather-result").innerHTML = `
                    <h2>${data.city}</h2>
                    <p>${data.description}</p>
                    <p>Temperature: ${data.temperature}°C</p>
                    <p>Humidity: ${data.humidity}%</p>
                    <p>Wind Speed: ${data.wind_speed} m/s</p>
                `;
            }
        })
        .catch(error => {
            console.error(error);
            document.getElementById("weather-result").innerText = "An error occurred";
        });
});
