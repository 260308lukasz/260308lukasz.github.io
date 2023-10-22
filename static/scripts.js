function toggleTheme() {
    const container = document.querySelector('.container');
    container.classList.toggle("dark");

    if (document.getElementById('motyw').textContent === "Motyw: jasny") {
        document.getElementById('motyw').textContent = "Motyw: ciemny";
    } else {
        document.getElementById('motyw').textContent = "Motyw: jasny";
    }
}

function toggleDetail() {
    let detailValue = localStorage.getItem('detail') || 'basic';
    const newDetailValue = detailValue === 'basic' ? 'advanced' : 'basic';
    
    localStorage.setItem('detail', newDetailValue);
    
    const rowsToToggle = document.querySelectorAll('.weather-table .advanced');
    rowsToToggle.forEach(row => {
        row.classList.toggle('hidden');
    });

    if (document.getElementById('informacje').textContent === "Informacje: podstawowe") {
        document.getElementById('informacje').textContent = "Informacje: złożone";
    } else {
        document.getElementById('informacje').textContent = "Informacje: podstawowe";
    }
}

function toggleFormat() {
    if (document.querySelector('#display_format_option_value').value === "main") {
        document.querySelector('#display_format_option_value').value = "description";
        const rowsToToggle = document.querySelectorAll('.weather-table .description-cell-main, .weather-table .description-cell-description');
        rowsToToggle.forEach(row => {
            row.classList.toggle('hidden');
        });
    } else if (document.querySelector('#display_format_option_value').value === "description") {
        document.querySelector('#display_format_option_value').value = "icons";
        const rowsToToggle = document.querySelectorAll('.weather-table .description-cell-description, .weather-table .description-cell-icons');
        rowsToToggle.forEach(row => {
            row.classList.toggle('hidden');
        });
    } else {
        document.querySelector('#display_format_option_value').value = "main";
        const rowsToToggle = document.querySelectorAll('.weather-table .description-cell-icons, .weather-table .description-cell-main');
        rowsToToggle.forEach(row => {
            row.classList.toggle('hidden');
        });
    }

    if (document.getElementById('format').textContent === "Format opisu: Krótki") {
        document.getElementById('format').textContent = "Format opisu: Długi";
    } else if (document.getElementById('format').textContent === "Format opisu: Długi") {
        document.getElementById('format').textContent = "Format opisu: Z ikonami";
    } else {
        document.getElementById('format').textContent = "Format opisu: Krótki";
    }
}
