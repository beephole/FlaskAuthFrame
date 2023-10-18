document.querySelector("#dark-mode-toggle").onclick = () => {
  const icon = document.querySelector("#dark-mode-icon");
  document.body.classList.toggle("dark-mode");

  if (document.body.classList.contains("dark-mode")) {
    icon.classList.replace("fas", "far");
    icon.classList.replace("fa-sun", "fa-moon");
  } else {
    icon.classList.replace("far", "fas");
    icon.classList.replace("fa-moon", "fa-sun");
  }
};
const specialButton = document.querySelector(".special-btn");
const imageFrame = document.querySelector("#image-frame");

// Image sources
const imageSources = [
  "static/assets/vendor/images/a_0.png",
  "static/assets/vendor/images/a_1.png",
  "static/assets/vendor/images/a_2 (2).png",
  "static/assets/vendor/images/a_2 (3).png",
  "static/assets/vendor/images/a_2.png",
  "static/assets/vendor/images/a_3 (2).png",
  "static/assets/vendor/images/a_3.png",
  "static/assets/vendor/images/b_1.png",
  "static/assets/vendor/images/c_0.png",
  "static/assets/vendor/images/c_2.png",
  "static/assets/vendor/images/d_2.png",
  "static/assets/vendor/images/d_3.png",
  "static/assets/vendor/images/e_0 (2).png",
  "static/assets/vendor/images/e_0 (3).png",
  "static/assets/vendor/images/e_0.png",
  "static/assets/vendor/images/e_1 (2).png",
  "static/assets/vendor/images/e_1 (3).png",
  "static/assets/vendor/images/e_1 (4).png",
  "static/assets/vendor/images/e_1.png",
  "static/assets/vendor/images/e_2 (2).png",
  "static/assets/vendor/images/e_2.png",
  "static/assets/vendor/images/e_3 (2).png",
  "static/assets/vendor/images/e_3.png",
  "static/assets/vendor/images/g_0.png",
  "static/assets/vendor/images/g_1 (2).png",
  "static/assets/vendor/images/g_1.png",
  "static/assets/vendor/images/g_2.png",
  "static/assets/vendor/images/g_3.png",
  "static/assets/vendor/images/i_0 (2).png",
  "static/assets/vendor/images/i_0 (3).png",
  "static/assets/vendor/images/i_0.png",
  "static/assets/vendor/images/i_1 (2).png",
  "static/assets/vendor/images/i_1 (4).png",
  "static/assets/vendor/images/i_1.png",
  "static/assets/vendor/images/i_2 (2).png",
  "static/assets/vendor/images/i_2.png",
  "static/assets/vendor/images/l_0.png",
  "static/assets/vendor/images/l_1.png",
  "static/assets/vendor/images/l_2.png",
  "static/assets/vendor/images/l_3.png",
  "static/assets/vendor/images/m_1.png",
  "static/assets/vendor/images/n_0 (2).png",
  "static/assets/vendor/images/n_0.png",
  "static/assets/vendor/images/n_1 (2).png",
  "static/assets/vendor/images/n_1 (3).png",
  "static/assets/vendor/images/n_1 (4).png",
  "static/assets/vendor/images/n_1.png",
  "static/assets/vendor/images/n_2 (2).png",
  "static/assets/vendor/images/n_2.png",
  "static/assets/vendor/images/n_3 (2).png",
  "static/assets/vendor/images/n_3.png",
  "static/assets/vendor/images/o_0 (2).png",
  "static/assets/vendor/images/o_0.png",
  "static/assets/vendor/images/o_1.png",
  "static/assets/vendor/images/o_2 (2).png",
  "static/assets/vendor/images/o_2.png",
  "static/assets/vendor/images/p_0.png",
  "static/assets/vendor/images/p_1.png",
  "static/assets/vendor/images/p_2.png",
  "static/assets/vendor/images/r_1.png",
  "static/assets/vendor/images/r_2.png",
  "static/assets/vendor/images/s_0 (2).png",
  "static/assets/vendor/images/s_0 (3).png",
  "static/assets/vendor/images/s_0 (4).png",
  "static/assets/vendor/images/s_0 (5).png",
  "static/assets/vendor/images/s_0.png",
  "static/assets/vendor/images/s_1 (2).png",
  "static/assets/vendor/images/s_1 (3).png",
  "static/assets/vendor/images/s_1 (4).png",
  "static/assets/vendor/images/s_1.png",
  "static/assets/vendor/images/s_2 (2).png",
  "static/assets/vendor/images/s_2 (3).png",
  "static/assets/vendor/images/s_2.png",
  "static/assets/vendor/images/s_3 (2).png",
  "static/assets/vendor/images/s_3.png",
  "static/assets/vendor/images/t_0 (2).png",
  "static/assets/vendor/images/t_0.png",
  "static/assets/vendor/images/t_1.png",
  "static/assets/vendor/images/t_2.png",
  "static/assets/vendor/images/u_0.png",
  "static/assets/vendor/images/v_1.png",
  "static/assets/vendor/images/v_3.png",
  "static/assets/vendor/images/w.png",
  "static/assets/vendor/images/y.png",
];

specialButton.addEventListener("click", function () {
  let imageElement = document.createElement("img");
  imageElement.src =
    imageSources[Math.floor(Math.random() * imageSources.length)]; // Random image source
  imageElement.classList.add("floating-image");
  imageFrame.appendChild(imageElement);
  // Start the floating animation
  const keyframes = `
        @keyframes float {
            0% { transform: translate3d(0, 100%, 0); opacity: 0; }
            ${Math.random() * 100}% { transform: translate3d(${
    Math.random() * 100 - 50
  }vw, ${Math.random() * 100 - 50}vh, 0); opacity: 1; }
            100% { transform: translate3d(${
              Math.random() * 100 - 50
            }vw, -5vh, 0); opacity: 0; }
        }
    `;

  // Create the style element
  const styleElement = document.createElement("style");
  styleElement.textContent = keyframes;
  imageElement.appendChild(styleElement);

  // Start the floating animation
  imageElement.style.animationName = "float"; // Use the random keyframes
  imageElement.style.display = "block";
  imageElement.style.left = Math.random() * window.innerWidth + "px";

  // Clean up the image after it finishes the floating animation
  setTimeout(() => {
    imageFrame.removeChild(imageElement);
  }, 10000); // 10s is the duration of the animation
});
