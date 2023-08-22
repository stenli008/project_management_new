let baseUrlTask = 'http://127.0.0.1:8000/apis/task/'
$(document).ready(function (){
    $('.remove-worker-btn').click(function (){
        let $removeBtn = $(this);
        let worker = $removeBtn.data('worker');
        let task = $removeBtn.data('task');
        let apiEndpoint = `${baseUrlTask}${task}/worker/${worker}/`
        let workerLi = $removeBtn.parent();

        $.ajax({
            url: apiEndpoint,
            type: 'DELETE',
            headers: {
                'X-CSRFToken': getCookie('csrftoken')
            },
            success: function (data){
                console.log(data);
                console.log('success');
                workerLi.hide()
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