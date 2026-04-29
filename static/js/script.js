// Mobile nav
const menuBtn = document.querySelector('#menu-btn');
const navbar  = document.querySelector('.navbar');

menuBtn.onclick = () => {
    menuBtn.classList.toggle('fa-times');
    navbar.classList.toggle('active');
};
window.addEventListener('scroll', () => {
    menuBtn.classList.remove('fa-times');
    navbar.classList.remove('active');
}, { passive: true });

// Scrolled header
const header = document.getElementById('header');
window.addEventListener('scroll', () => {
    header.classList.toggle('scrolled', window.scrollY > 60);
}, { passive: true });

// Hero slider
new Swiper('.home-slider', {
    grabCursor: true, loop: true, centeredSlides: true,
    effect: 'fade', fadeEffect: { crossFade: true },
    autoplay: { delay: 6000, disableOnInteraction: false },
    navigation: { nextEl: '.swiper-button-next', prevEl: '.swiper-button-prev' },
    speed: 900,
});

// Gallery slider
new Swiper('.gallery-slider', {
    spaceBetween: 10, grabCursor: true, loop: true,
    autoplay: { delay: 2000, disableOnInteraction: false },
    speed: 600,
    breakpoints: {
        0:    { slidesPerView: 1 },
        600:  { slidesPerView: 2 },
        900:  { slidesPerView: 3 },
        1200: { slidesPerView: 4 },
    },
});

// Scroll to result after form submit
const result = document.querySelector('.result');
if (result) {
    result.scrollIntoView({ behavior: 'smooth', block: 'center' });
}
