// CONTACT FORM
document.addEventListener('DOMContentLoaded', function() {
  const contactForm = document.querySelector('.first-contact-container form');
  if (contactForm) {
    contactForm.addEventListener('submit', function(e) {
      const name = contactForm.querySelector('#name').value.trim();
      const email = contactForm.querySelector('#email').value.trim();
      const message = contactForm.querySelector('#message').value.trim();

      if (!name || !email || !message) {
        e.preventDefault();
        alert('Please fill in all the fields before submitting.');
        return;
      }

      alert('Thank you for contacting us! Your message has been received.');
    });
  }
});


// APPOINTMENT FORM
document.addEventListener('DOMContentLoaded', function() {
  const appointmentForm = document.querySelector('.appointment-form');
  if (appointmentForm) {
    appointmentForm.addEventListener('submit', function(e) {
      const name = appointmentForm.querySelector('input[name="name"]').value.trim();
      const email = appointmentForm.querySelector('input[name="email"]').value.trim();
      const phone = appointmentForm.querySelector('input[name="phone"]').value.trim();
      const professional = appointmentForm.querySelector('select[name="professional"]').value;
      const date = appointmentForm.querySelector('input[name="date"]').value;

      if (!name || !email || !phone || !professional || !date) {
        e.preventDefault();
        alert("Please fill in all required fields.");
        return;
      }

      alert("Your appointment request has been submitted successfully!");
   });
 }
});

// About section numbers increased =====================================================================================================

document.addEventListener("DOMContentLoaded", function() {
    // Find all .calender h1 elements
    const counters = document.querySelectorAll('.calender h1');
    const targets = [300, 10000];
    const duration = 2000; // animation duration

    counters.forEach((counter, idx) => {
        let start = 0;
        let end = parseInt(targets[idx]);
        let increment = end > 100 ? Math.ceil(end / (duration / 25)) : 1;
        let current = start;

        function updateCounter() {
            current += increment;
            if(current > end) current = end;
            counter.textContent = current + "+";
            if(current < end) {
                setTimeout(updateCounter, 25);
            }
        }
        updateCounter();
    });
});

// smooth scrolling==========================================
document.addEventListener("DOMContentLoaded", () => {
  const elements = document.querySelectorAll(
    "body *:not(nav):not(nav *):not(.navbar):not(.navbar *):not(.navbar-collapse):not(.navbar-collapse *):not(.navbar-toggler):not(.navbar-toggler *):not(.services *):not(footer):not(.copyright):not(.copyright *)"
  );

  elements.forEach(el => el.classList.add("reveal"));

  function revealOnScroll() {
    const triggerBottom = window.innerHeight * 0.85;

    elements.forEach(el => {
      const elementTop = el.getBoundingClientRect().top;

      if (elementTop < triggerBottom) {
        el.classList.add("show");
      }
    });
  }

  window.addEventListener("scroll", revealOnScroll);
  revealOnScroll();
});
