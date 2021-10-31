const api = {

  async get(url) {
    const response = await fetch(url);
    return await response.json();
  },

  async post(url, data) {
    const response = await fetch(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    });
    return await response.json();
  },

  async put(url, data) {
    const response = await fetch(url, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(data),
    });
    return await response.json();
  },

  async delete(url) {
    const response = await fetch(url, {
      method: 'DELETE',
    });
    return await response.json();
  },

  async getStock(stockId) {
    return await this.get(`/api/stocks/${stockId}/`);
  },

  async getStocks() {
    const { results } = await this.get('/api/stocks/');
    return results;
  },

  async createStock(stock) {
    return await this.post('/api/stocks/', stock);
  },

  async getPortfolios() {
    const { results } = await this.get('/api/portfolios/');
    return results;
  },

  async createPortfolio(portfolio) {
    return await this.post('/api/portfolios/', portfolio);
  },

};

export default api;
