window.onload = function() {
    let isSubmitting = false;

    document.getElementsByTagName('form')[0].addEventListener('submit', function(event) {
        if (isSubmitting) {
            event.preventDefault();
            return false;
        }
        isSubmitting = true;
        document.getElementsByTagName('button')[0].disabled = true;
        return true;
    });
}
