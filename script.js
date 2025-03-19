// Tovarlar ro'yxati
const products = [
    { id: 1, name: "Cyber Oyinchoq", price: 100 },
    { id: 2, name: "Oyumena", price: 50 }
];

// URL orqali tovarni aniqlash
const urlParams = new URLSearchParams(window.location.search);
const productId = parseInt(urlParams.get("productId"));
const selectedProduct = products.find(product => product.id === productId);



function showToyInfo(name, price) {
    document.getElementById("toy-name").innerText = name;
    document.getElementById("toy-price").innerText = "Цена: €" + price.toFixed(2);
    document.getElementById("modal").style.display = "flex";
}

function closeModal() {
    document.getElementById("modal").style.display = "none";
}