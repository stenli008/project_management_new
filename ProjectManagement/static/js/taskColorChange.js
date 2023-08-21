let now = new Date();

function checkDeadlines() {
    let taskRow = document.querySelectorAll('.task-tr')

    taskRow.forEach(function (row){
        let deadline = new Date(row.getAttribute('data-deadline'));

        if (deadline < now){
            let tds = row.querySelectorAll('td')
            tds.forEach( function (td) {
                td.classList.add('bg-danger')
            })
        }
    })
}



window.addEventListener('load', checkDeadlines)