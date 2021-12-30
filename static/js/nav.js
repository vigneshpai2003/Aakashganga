function main() {
    const menu_toggle = document.querySelector('.menu-toggle')
    const nav = document.querySelector('.nav-link')
    const nav_links = document.querySelectorAll('.nav-link li')

    menu_toggle.addEventListener('click', function () {
        nav.classList.toggle('menu-active')

        nav_links.forEach(function (link, index) {
            if (link.style.animation)
                link.style.animation = ''
            else
                link.style.animation = 'menuFade 0.5s ease forwards ' +  (index / 10 + .3) + 's'
        })
        menu_toggle.classList.toggle('toggle')
    })
}

main()
