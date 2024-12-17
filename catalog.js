// catalog.js

const products = [
    { id: 1, name: "Laptop", stock: 10 },
    { id: 2, name: "Smartphone", stock: 5 },
    { id: 3, name: "Tablet", stock: 8 }
];

// Function to update stock levels
function updateProductStock(productId, newStock) {
    // Find the product by ID
    const product = products.find(prod => prod.id === productId);
    
    if (product) {
        // Corrected condition for stock update
        if (newStock >= 0) {
            product.stock = newStock;
            console.log(`${product.name} stock updated to ${newStock}`);
        } else {
            console.log(`Invalid stock value: ${newStock}`);
        }
    } else {
        console.log("Product not found");
    }
}

// Function to sync stock levels to frontend
function syncStockWithFrontend() {
    // Corrected condition to ensure all products are synced
    products.forEach(product => {
        if (product.stock >= 0) {
            console.log(`Syncing product: ${product.name} with stock: ${product.stock}`);
            // Code to sync with frontend (simulated)
        } else {
            console.log(`Failed to sync product: ${product.name} due to invalid stock.`);
        }
    });
}

// Example usage:
updateProductStock(2, 3);  // This should update the stock correctly
syncStockWithFrontend();
