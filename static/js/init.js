let NavbarBtn;
let btnIcon;
let navLinks;

function init(){
    openTap('mining');
    NavbarBtn = document.getElementById('navbar-btn');
    btnIcon = document.getElementById('btn-icon');
    navLinks = document.getElementById('nav');

    if (submitted()){
        document.getElementById('contact').scrollIntoView();
    }
}

function submitted (){
    submitted = false
    try {
        const product = urlParms.get('submitted')
        submitted = true;
    }
    catch{

    }

    return submitted
}






function openPopup(popup){
    id = 'popup-'+ popup;
    document.getElementById(id).classList.remove('hidden');
    document.getElementById('body').classList.add('no-scroll');
}

function closePopup(){
    document.getElementById('popup-dataprotection').classList.add('hidden');
    document.getElementById('popup-impressum').classList.add('hidden');
    document.getElementById('body').classList.remove('no-scroll');
}

function prefillForm(){
    document.getElementById('id_prename').value = 'test';
    document.getElementById('id_name').value = 'test';
    document.getElementById('id_email').value = 'test@gmail.com';
    document.getElementById('id_message').value = 'test';
}