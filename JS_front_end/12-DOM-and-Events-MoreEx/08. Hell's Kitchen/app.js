// "PizzaHut - Peter 500, George 300, Mark 800




function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);
   function onClick() {
      let textAreaJSON = JSON.parse(document.querySelector("#inputs textarea").value)
      let bestRestaurantP = document.querySelector('#bestRestaurant p');
      let bestRestaurantWorkersP = document.querySelector('#workers p');
      let restaurants = {};

      for (let line of textAreaJSON) {
         let [restaurantName, workers] = line.split(' - ');
         workers = workers.split(', ')

         if (!(restaurantName in restaurants)) {
            restaurants[restaurantName] = [];
         }
         workers.forEach(w => {
            let [workerName, workerSalary] = w.split(' ')
            restaurants[restaurantName].push({ workerName, workerSalary: Number(workerSalary) })
         });
      }

      let restaurantsSalaries = {}

      for (const rName of Object.keys(restaurants)) {
         let avgSalary = (restaurants[rName].map(i => i.workerSalary).reduce((prev, next) => prev + next)) / restaurants[rName].length;
         restaurantsSalaries[rName] = avgSalary
      }

      let bestRestaurant = Object.keys(restaurantsSalaries).reduce((a, b) => restaurantsSalaries[a] > restaurantsSalaries[b] ? a : b);
      let bestSalary = Math.max(...restaurants[bestRestaurant].map(obj => obj.workerSalary))

      bestRestaurantP.textContent = `Name: ${bestRestaurant} Average Salary: ${Number(restaurantsSalaries[bestRestaurant]).toFixed(2)} Best Salary: ${bestSalary.toFixed(2)}`;

      let workersOutput = [];

      restaurants[bestRestaurant]
         .sort((a, b) => b.workerSalary - a.workerSalary)
         .forEach(w => {
            workersOutput.push(`Name: ${w.workerName} With Salary: ${w.workerSalary}`)
         });

      bestRestaurantWorkersP.textContent = workersOutput.join(' ')
   }
}