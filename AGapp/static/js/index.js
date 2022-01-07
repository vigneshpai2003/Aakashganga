window.addEventListener('scroll', function () {
    document.querySelector('.background').style.backgroundPosition = "center " + document.scrollingElement.scrollTop * 0.5 + "px"
})

$(window).scroll(function () {
    const scrollTop = $(this).scrollTop()

    $('.fade').each(function () {
        $(this).css({
            opacity: function () {
                return (scrollTop / $(this).height()) ** 3
            }
        })
    })
});
