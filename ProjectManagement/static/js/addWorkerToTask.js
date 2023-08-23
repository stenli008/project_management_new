$(document).ready(function (){
    $('.add-worker-btn').click(function (){
        let $addWorkerBtn = $(this);
        let $liElement = $addWorkerBtn.closest('.list-group-item');
        let $selectElement = $liElement.find('.form-select');
        let selectedWorkerPk = $selectElement.find(':selected').data('unusedworker'); // Get the data-worker attribute of the selected option
        let taskPk = $addWorkerBtn.data('task');
        let $workerOption = $selectElement.find(':selected')


        let apiEndpoint = `${baseUrlTask}${taskPk}/worker/${selectedWorkerPk}/`

        $.ajax({
            url: apiEndpoint,
            type: 'PATCH',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function (data){
                console.log(data);
                location.reload()


            },
            error: function (xhr, status, error) {
                console.error('Error:', error);
            },
        });

    })
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
})