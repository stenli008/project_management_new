const baseUrl = 'http://127.0.0.1:8000';
$(document).ready(function () {
    $('.toggle-worker-btn').click(function () {
        const workerPk = $(this).data('pk');
        const apiEndpoint = `${baseUrl}/apis/workers/${workerPk}/toggle-activation/`;


        $.ajax({
                url: apiEndpoint,
                type: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': getCookie('csrftoken')
                },
                success: function (data) {
                    console.log(data);
                    updateStatusUI(workerPk, data.is_active);
                },
                error: function (xhr, status, error) {
                    console.error('Error:', error);
                    updateStatusUI();
                }

            }
        );
    });

    function updateStatusUI(workerPk, isActive) {
        const statusElement = $(`#status-${workerPk}`);
        const buttonElement = $(`.toggle-worker-btn[data-pk="${workerPk}"]`);

        if (isActive) {
            statusElement.text('Active');
            buttonElement.text('Deactivate');
        } else {
            statusElement.text('Inactive');
            buttonElement.text('Activate');
        }

    }

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
});