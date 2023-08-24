const baseUrl = 'http://127.0.0.1:8000';
$(document).ready(function () {
    $('.track-progress-btn').click(function () {
        let $trackBtn = $(this)
        let $input = $trackBtn.next('.input-label');
        let $checkBtn = $input.next('.check-btn')

        $checkBtn.show()
        $input.show()
        $trackBtn.hide();

        $('.check-btn').click(function () {

            let $checkBtn = $(this);
            let $inputLabel = $checkBtn.prev('.input-label');
            let $workInput = $inputLabel.children('.work-input');
            let inputValue = $workInput.val();
            let workDone = $checkBtn.data('done');
            let taskPk = $checkBtn.data('pk');

            let apiEndpoint = `${baseUrl}/apis/tasks/update_work_done/${taskPk}/`;


            let newWork = parseInt(workDone) + parseInt(inputValue);


            let patch_data = {
                work_done: newWork
            };
            if (inputValue > 0) {
                $.ajax({
                    url: apiEndpoint,
                    type: 'PATCH',
                    data: JSON.stringify(patch_data),
                    headers: {
                        'Content-Type': 'application/json',
                        'X-CSRFToken': getCookie('csrftoken')
                    },
                    success: function () {
                        location.reload();

                    },
                    error: function (xhr, status, error) {
                        console.error('Error', error);
                        console.log(xhr)
                        location.reload();
                    }

                })
            } else {
                console.log('Input must be positive')
            }
        })


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