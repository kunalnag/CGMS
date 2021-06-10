const cases = document.querySelector('.ticket-input');
const deaths = document.querySelector('.answered-input');
const recovered = document.querySelector('.resolved-input');

const ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
	type: 'pie',
	data: {
		labels: ['Opened', 'Answered', 'Resolved'],
		datasets: [
			{
				label: '# of Votes',
				data: [0, 0, 0],
				backgroundColor: ['#2adece', '#FF7550', '#F4A460'],
				borderWidth: 1
				
			}
		]
	}
});

const updateChartValue = (input, dataOrder) => {
	input.addEventListener('change', e => {
		myChart.data.datasets[0].data[dataOrder] = e.target.value;
		myChart.update();
	});
};

updateChartValue(ticket, 0);
updateChartValue(answered, 1);
updateChartValue(resolved, 2);