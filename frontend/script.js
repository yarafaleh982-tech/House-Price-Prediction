const API_URL = "http://127.0.0.1:8000";

// تحميل المدن عند فتح الصفحة
window.onload = async function () {
    const response = await fetch(`${API_URL}/locations`);
    const locations = await response.json();

    const locationSelect = document.getElementById("location");

    // حذف الخيار الافتراضي
    locationSelect.innerHTML = "";

    locations.forEach(location => {
        const option = document.createElement("option");
        option.value = location;
        option.textContent = location;
        locationSelect.appendChild(option);
    });
};

// إرسال البيانات إلى الـ API
async function predictPrice() {

    const data = {
        carpet_area_sqft: Number(document.getElementById("area").value),
        floor_num: Number(document.getElementById("floor").value),
        Bathroom: Number(document.getElementById("bathroom").value),
        Balcony: Number(document.getElementById("balcony").value),

        location_grouped: document.getElementById("location").value,
        Furnishing: document.getElementById("furnishing").value,
        Transaction: document.getElementById("transaction").value,
        Ownership: document.getElementById("ownership").value,
        facing: document.getElementById("facing").value
    };

    const response = await fetch(`${API_URL}/predict`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById("result").innerHTML =
        `Predicted Price: ₹ ${Number(result["Predicted Price"]).toLocaleString()}`;
}