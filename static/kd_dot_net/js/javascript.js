function setOverlayPhotoSrc(id) {
    let existingPhoto = document.getElementById('enlargedPhoto');
    let photoParent = document.querySelector('div.photoContainer');

    if (existingPhoto) {
        existingPhoto.remove();
    }

    $.ajax({
        url: '/photo/full/' + id,
        dataType: 'html',
        success: (data, status, xhr) => {
            photoParent.insertAdjacentHTML('beforeend', data);
            $('body').find($('#overlay-photo')).fadeIn(400);
        }
    })
}

// function to reset the selected overlay photo and its info to empty.
// Without this, we would get a flash of an empty img tag on fadeOut of the selectedPhoto.
function clearVals() {
    state.selectedPhotoIndex = null;
    setOverlayPhotoSrc('');
}

function minimizePhoto() {
    $('body').find($('#overlay-photo')).fadeOut(200, clearVals)
}

function navigateLeft() {
    // if user clicks left arrow from first item in list, navigate to last photo
    var index = state.selectedPhotoIndex - 1 === -1 ? state.photoIds.length - 1 : state.selectedPhotoIndex - 1;
    state.selectedPhotoIndex = index;
    setOverlayPhotoSrc(state.photoIds[index]);
}

function navigateRight() {
    // if user clicks left arrow from first item in list, navigate to last photo
    var index = state.selectedPhotoIndex + 1 === state.photoIds.length ? 0 : state.selectedPhotoIndex + 1;
    state.selectedPhotoIndex = index;
    setOverlayPhotoSrc(state.photoIds[index]);
}

function enlargePhoto(event) {
    // only enlarge photo if the screen is wider than 800 px. otherwise the images fill width anyway
    if (window.innerWidth >= 800) {
        var id;
        var target = $(event.target);

        if (target.is('img')) {
            id = target.attr('id');
        }

        state.selectedPhotoIndex = state.photoIds.findIndex(elem => elem === Number(id));

        setOverlayPhotoSrc(id);
        //setOverlayPhotoSrc('./styles/pics/kyle3.jpg');
    }
}

// handle keypress events if enlarged photo is showing
$(document).keyup(function(e) {
    if (document.getElementById('overlay-photo').style.display === 'block') {
        switch(e.keyCode) {
            // ESC
            case 27:
                minimizePhoto();
                break;
            // Left arrow
            case 37:
                navigateLeft();
                break;
            // Right arrow
            case 39:
                navigateRight();
                break;
        }
    }
});
