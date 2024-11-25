async function fetchProducts() {
    const response = await fetch("/products");
    const products = await response.json();
    const list = document.getElementById("product-list");
    list.innerHTML = products.map(product => 
        <div>
            <h2>${product.name}</h2>
            <p>${product.description}</p>
            <p><strong>$${product.price}</strong></p>
        </div>
    ).join("");
}
fetchProducts();