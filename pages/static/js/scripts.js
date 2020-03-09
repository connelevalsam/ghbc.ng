//javascript file


document.querySelector('.hamburger').addEventListener('click', event => {

    let navbar = document.querySelector('.navbar')
    let hamburger = document.querySelector('.hamburger')
    let navbarWidth = navbar.getBoundingClientRect().width

    event.preventDefault()
    navbar.classList.toggle('transform-off')

    hamburger.style.transform = hamburger.style.transform ? '' : 'translate3d(-' + navbarWidth + 'px, 0, 0)'
})

document.querySelector('.contents').addEventListener('click', event => {
    document.querySelector('.hamburger').style.transform = ''
    document.querySelector('.navbar').classList.add('transform-off')
})