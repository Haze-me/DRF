document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("login-form");
    const registerForm = document.getElementById("register-form");
    const messageContainer = document.getElementById("auth-message");

    function getCSRFToken() {
        let csrfToken = null;
        const cookies = document.cookie.split("; ");
        for (const cookie of cookies) {
            if (cookie.startsWith("csrftoken=")) {
                csrfToken = cookie.split("=")[1];
                break;
            }
        }
        return csrfToken;
    }

    function showMessage(type, message) {
        messageContainer.innerHTML = `
            <div class="alert alert-${type} alert-dismissible fade show" role="alert">
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert" aria-label="Close"></button>
            </div>
        `;
    }

    async function handleAuth(url, data, form, button) {
        try {
            button.disabled = true;
            button.innerText = "Processing...";

            const response = await fetch(url, {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                    "X-CSRFToken": getCSRFToken(),
                },
                body: JSON.stringify(data),
            });

            const responseData = await response.json();

            if (!response.ok) {
                throw responseData;
            }

            return responseData;
        } catch (error) {
            throw error;
        } finally {
            button.disabled = false;
            button.innerText = form === loginForm ? "Login" : "Register";
        }
    }

    if (loginForm) {
        loginForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const username = document.getElementById("username").value.trim();
            const password = document.getElementById("password").value.trim();
            const submitButton = loginForm.querySelector("button[type='submit']");

            try {
                const data = await handleAuth("/api/login/", { username, password }, loginForm, submitButton);
                localStorage.setItem("access_token", data.access);

                showMessage("success", "Login successful! Redirecting...");
                setTimeout(() => window.location.href = "/home/", 2000);
            } catch (error) {
                showMessage("danger", error.detail || "Invalid credentials. Please try again.");
            }
        });
    }

    if (registerForm) {
        registerForm.addEventListener("submit", async function (event) {
            event.preventDefault();

            const username = document.getElementById("username").value.trim();
            const email = document.getElementById("email").value.trim();
            const password = document.getElementById("password").value.trim();
            const submitButton = registerForm.querySelector("button[type='submit']");

            try {
                await handleAuth("/api/register/", { username, email, password }, registerForm, submitButton);

                showMessage("success", "Registration successful! Redirecting to login...");
                setTimeout(() => window.location.href = "/login/", 2000);
            } catch (error) {
                showMessage("danger", error.detail || "Registration failed. Please check your inputs.");
            }
        });
    }
});
