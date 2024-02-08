function setOverlayPhotoSrc(id) {
    let existingPhoto = document.getElementById('enlargedPhoto');
    let photoParent = document.querySelector('div.photoContainer');

    fetch(`/photo/full/${id}`, {
        headers: {
            "Accept": "text/html"
        }
    })
    .then((response) => response.text())
    .then((text) => {
        if (existingPhoto) {
            existingPhoto.remove();
        }
        
        photoParent.insertAdjacentHTML('beforeend', text);

        let image = document.getElementById('enlargedPhoto');
        image.style.visibility = 'hidden';

        let overlay = document.querySelector('#overlay-photo');

        if (!overlay.classList.contains('visible')) {
            overlay.classList.add('visible');
        }

        let callback = () => { image.style.visibility = 'visible' };

        image.addEventListener('load', callback);
    });
}

function minimizePhoto() {
    document.querySelector('#overlay-photo').classList.remove('visible');
}

function navigateLeft(evt) {
    // if user clicks left arrow from first item in list, navigate to last photo
    var index = state.selectedPhotoIndex - 1 === -1 ? state.photoIds.length - 1 : state.selectedPhotoIndex - 1;
    state.selectedPhotoIndex = index;
    setOverlayPhotoSrc(state.photoIds[index]);

    evt.stopPropagation();
}

function navigateRight(evt) {
    // if user clicks left arrow from first item in list, navigate to last photo
    var index = state.selectedPhotoIndex + 1 === state.photoIds.length ? 0 : state.selectedPhotoIndex + 1;
    state.selectedPhotoIndex = index;
    setOverlayPhotoSrc(state.photoIds[index]);

    evt.stopPropagation();
}

function enlargePhoto(event) {
    // only enlarge photo if the screen is wider than 800 px. otherwise the images fill width anyway
    if (window.innerWidth >= 800) {
        var id;
        var target = event.target;

        id = target.id;

        state.selectedPhotoIndex = state.photoIds.findIndex(elem => elem === Number(id));

        setOverlayPhotoSrc(id);
        //setOverlayPhotoSrc('./styles/pics/kyle3.jpg');
    }
}

// handle keypress events if enlarged photo is showing
document.addEventListener('keyup', (e) => {
    if (document.getElementById('overlay-photo').style.visibility === 'visible') {
        switch (e.code) {
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
