/**
 * Retrieves all products from the database.
 * 
 * @param {Object} req - The request object.
 * @param {Object} res - The response object.
 * 
 * @returns {void} - Sends a JSON response with the list of products or an error message.
 * 
 * @throws {Error} - If there is an issue fetching products, a 500 status code is returned with an error message.
 */
const getProducts = async (req, res) => {
    try {
        const products = await Product.find(); 
        res.status(200).json(products);
    } catch (error) {
        res.status(500).json({ message: 'Error fetching products', error });
    }
};

/**
 * Retrieves a product by its ID from the database.
 * 
 * @param {Object} req - The request object, containing the product ID in req.params.id.
 * @param {Object} res - The response object.
 * 
 * @returns {void} - Sends a JSON response with the product details or an error message.
 * 
 * @throws {Error} - If the product ID is not provided, a 400 status code is returned.
 *                   If the product is not found, a 404 status code is returned.
 *                   If there is a server error, a 500 status code is returned with an error message.
 */
const getProductById = async (req, res) => {
    try {
        const productId = req.params.id;

        if (!productId) {
            return res.status(400).json({ message: 'Product ID is required' });
        }

        const product = await Product.findById(productId);

        if (product) {
            res.json(product);
        } else {
            res.status(404).json({ message: 'Product not found' });
        }
    } catch (error) {
        res.status(500).json({ message: 'Server Error', error: error.message });
    }
};

module.exports = {
    getProducts,
    getProductById
};
