class MobileMenu {
    constructor() {
        this.menu = document.querySelector("#mobile-menu")
        this.MenuButton = document.querySelector("#open-menu-btn")
        this.openIcon = document.querySelector("#icon-open")
        this.closeIcon = document.querySelector("#icon-close")
        this.events()
      }

      events() {
        this.MenuButton.addEventListener("click", () => this.toggleMenu())
      }

      toggleMenu() {
        const isExpanded = this.MenuButton.getAttribute('aria-expanded') === 'true';
        console.log(isExpanded ? 'Close the menu' : 'Open the menu');
        this.openIcon.classList.toggle('block', isExpanded);
        this.openIcon.classList.toggle('hidden', !isExpanded);
        this.closeIcon.classList.toggle('block', !isExpanded);
        this.closeIcon.classList.toggle('hidden', isExpanded);
        this.MenuButton.setAttribute('aria-expanded', !isExpanded);
        this.menu.classList.toggle('hidden', isExpanded);
      }
}

document.addEventListener('DOMContentLoaded', () => {
   const mobileMenu = new MobileMenu();

});