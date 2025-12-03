// Inicializar gráficos para reportes personalizados
function initReportCharts(config) {
    if (!config.mostrarGraficos) return;

    // Gráfico de producción mensual
    if (config.produccionMensual && config.produccionMensual.length > 0) {
        const ctxMensual = document.getElementById('chartProduccionMensual');
        if (ctxMensual) {
            new Chart(ctxMensual, {
                type: 'line',
                data: {
                    labels: config.produccionMensual.map(item => item.mes),
                    datasets: [{
                        label: `Producción (${config.unidadMedida})`,
                        data: config.produccionMensual.map(item => item.total),
                        borderColor: 'rgb(75, 192, 192)',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        tension: 0.1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: true,
                            position: 'top'
                        },
                        title: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    }

    // Gráfico de distribución por tipo de alga
    if (config.distribucion && config.distribucion.length > 0) {
        const ctxDistribucion = document.getElementById('chartDistribucion');
        if (ctxDistribucion) {
            new Chart(ctxDistribucion, {
                type: 'bar',
                data: {
                    labels: config.distribucion.map(item => item.nombre),
                    datasets: [{
                        label: `Total Cosechado (${config.unidadMedida})`,
                        data: config.distribucion.map(item => item.total),
                        backgroundColor: [
                            'rgba(255, 99, 132, 0.7)',
                            'rgba(54, 162, 235, 0.7)',
                            'rgba(255, 206, 86, 0.7)',
                            'rgba(75, 192, 192, 0.7)',
                            'rgba(153, 102, 255, 0.7)',
                            'rgba(255, 159, 64, 0.7)'
                        ],
                        borderWidth: 1
                    }]
                },
                options: {
                    responsive: true,
                    plugins: {
                        legend: {
                            display: false
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true
                        }
                    }
                }
            });
        }
    }
}
