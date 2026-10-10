
const API_URL = "https://mlops-house-price-cloud-deployment.onrender.com";

const form = document.getElementById("prediction-form");
const button = document.getElementById("predict-button");
const statusMessage = document.getElementById("status");
const result = document.getElementById("result");
const price = document.getElementById("price");

form.addEventListener("submit", async (event) => {
    event.preventDefault();

    result.hidden = true;
    statusMessage.textContent = "Getting prediction...";
    button.disabled = true;

    const payload = {
        area: Number(document.getElementById("area").value),
        bedrooms: Number(document.getElementById("bedrooms").value),
        age: Number(document.getElementById("age").value)
    };

    try {
        const response = await fetch(`${API_URL}/predict`, {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail
                ? JSON.stringify(data.detail)
                : "Prediction request failed.");
        }

        price.textContent =
            `₹${data.predicted_price_lakhs} lakh`;

        result.hidden = false;
        statusMessage.textContent = "";
    } catch (error) {
        statusMessage.textContent =
            `Unable to get prediction: ${error.message}`;
    } finally {
        button.disabled = false;
    }
});
