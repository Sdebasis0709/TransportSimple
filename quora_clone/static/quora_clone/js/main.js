document.addEventListener("DOMContentLoaded", function () {
    const likes = document.querySelectorAll(".like-btn");

    likes.forEach(btn => {
        btn.addEventListener("click", () => {
            btn.disabled = true;
            btn.textContent = "Liked!";
        });
    });
});
