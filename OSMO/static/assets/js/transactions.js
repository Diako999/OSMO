
    if ($('#lineChart').length) {
      var lineChartCanvas = $("#lineChart").get(0).getContext("2d");
      var data = {
        labels: {{ labels|safe }},
        datasets: [
          {
            label: 'Apple',
            data: [120, 180, 140, 210, 160, 240, 180, 210],
            borderColor: [
              '#2e7ce4'
            ],
            borderWidth: 3,
            fill: false,
            pointBackgroundColor: "#ffffff",
            pointBorderColor: "#2e7ce4"
          },
          {
            label: 'Samsung',
            data: [80, 140, 100, 170, 120, 200, 140, 170],
            borderColor: [
              '#00c2b2'
            ],
            borderWidth: 3,
            fill: false,
            pointBackgroundColor: "#ffffff",
            pointBorderColor: "#00c2b2"
          }
        ]
      };
      var options = {
        scales: {
          yAxes: [{
            gridLines: {
              drawBorder: false,
              borderDash: [3, 3]
            },
            ticks: {
              min: 0
            },
          }],
          xAxes: [{
            gridLines: {
              display: false,
              drawBorder: false,
              color: "#ffffff"
            }
          }]
        },
        elements: {
          line: {
            tension: 0.2
          },
          point: {
            radius: 4
          }
        },
        stepsize: 1
      };
      var lineChart = new Chart(lineChartCanvas, {
        type: 'bar',
        data: data,
        options: options
      });
}
if ($('#lineChart').length) {
      var lineChartCanvas = $("#lineChart").get(0).getContext("2d");
      var data = {
        labels: ["2013", "2014", "2014", "2015", "2016", "2017", "2018", "2019"],
        datasets: [
          {
            label: 'Apple',
            data: [120, 180, 140, 210, 160, 240, 180, 210],
            borderColor: [
              '#2e7ce4'
            ],
            borderWidth: 3,
            fill: false,
            pointBackgroundColor: "#ffffff",
            pointBorderColor: "#2e7ce4"
          },
          {
            label: 'Samsung',
            data: [80, 140, 100, 170, 120, 200, 140, 170],
            borderColor: [
              '#00c2b2'
            ],
            borderWidth: 3,
            fill: false,
            pointBackgroundColor: "#ffffff",
            pointBorderColor: "#00c2b2"
          }
        ]
      };
      var options = {
        scales: {
          yAxes: [{
            gridLines: {
              drawBorder: false,
              borderDash: [3, 3]
            },
            ticks: {
              min: 0
            },
          }],
          xAxes: [{
            gridLines: {
              display: false,
              drawBorder: false,
              color: "#ffffff"
            }
          }]
        },
        elements: {
          line: {
            tension: 0.2
          },
          point: {
            radius: 4
          }
        },
        stepsize: 1
      };
      var lineChart = new Chart(lineChartCanvas, {
        type: 'line',
        data: data,
        options: options
      });
    }