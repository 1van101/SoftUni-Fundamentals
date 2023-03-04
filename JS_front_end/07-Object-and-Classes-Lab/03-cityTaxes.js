function cityTaxes(cityName, population, treasury) {
    let thisCity = {
        name: cityName,
        population: population,
        treasury: treasury,
        taxRate: 10,
        collectTaxes() {
            this.treasury += this.population * this.taxRate;
        },
        applyGrowth(percentage) {
            this.population *= (percentage / 100 + 1);
        },
        applyRecession(percentage) {
            this.treasury *= (1 - percentage / 100);
        }
    }

    return thisCity
}


