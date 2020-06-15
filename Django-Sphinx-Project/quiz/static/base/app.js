let mouseCursor = document.querySelector(".cursor");
let navLinks = document.querySelectorAll(".nav_head li");

window.addEventListener("mousemove", cursor);

function cursor(e) {
  mouseCursor.style.top = e.pageY + "px";
  mouseCursor.style.left = e.pageX + "px";
}

navLinks.forEach((link) => {
  link.addEventListener("mouseover", () => {
    mouseCursor.classList.add("link-grow");
  });
  link.addEventListener("mouseleave", () => {
    mouseCursor.classList.remove("link-grow");
  });
});

let tl2 = gsap.timeline({ default: { duration: 1.22 } });

tl2
  .fromTo(".veil", { height: "100%" }, { height: "0" })
  .fromTo(".container", { x: "-500", opacity: 0 }, { x: "0", opacity: 1 })
  .fromTo("header", { x: "500", opacity: 0 }, { x: "0", opacity: 1 });
