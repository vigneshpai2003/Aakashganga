window.addEventListener('scroll', function () {
    document.querySelector('.background').style.backgroundPosition = "center " + document.scrollingElement.scrollTop * 0.5 + "px"
})
