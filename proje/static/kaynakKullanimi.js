$(document).ready(function() {
    const config = {
        type: 'doughnut',
        data: {
            labels: ['Kullanılan', 'Boşta'],
            datasets: [{
                label: '# Ram Kullanımı',
                data: [],
                backgroundColor: [
                    '#e74a3b',
                    '#1cc88a',
                ],
                borderColor: [
                    '#ffffff',
                    '#ffffff',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'RAM'
            },
            legend: {
                display: false
            },
        }
    };

    const context = document.getElementById('ramKullanim').getContext("2d");
    const pastaGrafik = new Chart(context, config);
    const kaynak = new EventSource("/anlik-veri");
    kaynak.onmessage = function(event) {
        const veri = JSON.parse(event.data);
        config.data.datasets[0].data[0] = veri['ram_Boşta'];
        config.data.datasets[0].data[1] = veri['ram_Kullanılan'];
        pastaGrafik.update();
    }
});

// https://www.chartjs.org/docs/latest/developers/api.html

$(document).ready(function() {
    const config = {
        type: 'doughnut',
        data: {
            labels: ['Geçerli', 'Maks.'],
            datasets: [{
                label: '# CPU Kullanımı',
                data: [],
                backgroundColor: [
                    '#e74a3b',
                    '#1cc88a',
                ],
                borderColor: [
                    '#ffffff',
                    '#ffffff',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'CPU'
            },
            legend: {
                display: false
            },
        }
    };

    const context = document.getElementById('cpuKullanimi').getContext("2d");
    const pastaGrafik = new Chart(context, config);
    const kaynak = new EventSource("/anlik-veri");
    kaynak.onmessage = function(event) {
        const veri = JSON.parse(event.data);
        config.data.datasets[0].data[0] = veri['CPU_Kullanılan'];
        config.data.datasets[0].data[1] = veri['CPU_Maks'];
        pastaGrafik.update();
    }
});


$(document).ready(function() {
    const config = {
        type: 'doughnut',
        data: {
            labels: ['Kullanılan', 'Kalan'],
            datasets: [{
                label: '# Şarj Seviyesi',
                data: [],
                backgroundColor: [
                    '#e74a3b',
                    '#1cc88a',
                ],
                borderColor: [
                    '#ffffff',
                    '#ffffff',
                ]
            }]
        },
        options: {
            maintainAspectRatio: false,
            title: {
                display: true,
                text: 'Şarj'
            },
            legend: {
                display: false
            },
        }
    };

    const context = document.getElementById('sarjSeviyesi').getContext("2d");
    const pastaGrafik = new Chart(context, config);
    const kaynak = new EventSource("/anlik-veri");
    kaynak.onmessage = function(event) {
        const veri = JSON.parse(event.data);
        config.data.datasets[0].data[0] = 100-veri['Şarj_Seviye'];
        config.data.datasets[0].data[1] = veri['Şarj_Seviye'];
        pastaGrafik.update();
    }
});