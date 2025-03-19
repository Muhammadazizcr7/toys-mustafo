// Savat ma'lumotlari
let cart = [];

// Mahsulotni savatga qo'shish funksiyasi
function addToCart(productName, price) {
    cart.push({ name: productName, price: price });
    updateCart();
}

// Savatni yangilash
function updateCart() {
    const cartItems = document.getElementById("cart-items");
    const cartCount = document.getElementById("cart-count");
    const cartTotal = document.getElementById("cart-total");
    
    cartItems.innerHTML = "";
    let total = 0;

    cart.forEach(item => {
        const li = document.createElement("li");
        li.textContent = ${item.name} - $${item.price};
        cartItems.appendChild(li);
        total += item.price;
    });

    cartCount.textContent = cart.length;
    cartTotal.textContent = Total: $${total};
}

// Savatni ko'rsatish/tayinish
document.getElementById("cart-btn").addEventListener("click", () => {
    document.getElementById("cart-modal").classList.toggle("cart-hidden");
});

// Mahsulotni qo'shish misoli
document.querySelectorAll(".buy-now").forEach(button => {
    button.addEventListener("click", () => {
        const productName = button.getAttribute("data-name");
        const price = parseFloat(button.getAttribute("data-price"));
        addToCart(productName, price);
    });
});