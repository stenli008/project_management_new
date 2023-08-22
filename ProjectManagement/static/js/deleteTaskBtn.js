const baseUrl = 'http://127.0.0.1:8000';
$(document).ready(function () {
    $('.delete-task-btn').click(function () {
        let taskPk = $(this).data('pk')
        let apiEndPoint = `${baseUrl}/apis/tasks/delete/${taskPk}`
        let taskSlug = $(this).data('slug')
        let taskTr = $(this).data('pk')
        console.log(taskTr)

        let confirmation = confirm(`Are you sure you want to delete task: ${taskSlug}`)
        if (confirmation){
            $.ajax({
                url: apiEndPoint,
                type: 'DELETE',
                headers: {

                },
                success: function (data) {
                    console.log(data);
                    $(`.task-tr[data-pk=${taskTr}]`).remove()

                },
                error: function (xhr, status, error) {
                    console.error('Error:', error);
                }
            })
        }

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