const parentDiv = document.querySelector(".genre-parent");
const addButton = parentDiv.querySelector(".add-genre");

addButton.addEventListener("click", () => {
    const clone = parentDiv.cloneNode(true);
    const buttonsDiv = clone.querySelector(".buttons");
    buttonsDiv.innerHTML = `
        <button type="button" class="btn btn-secondary mt-2 add-genre">+</button>
        <button type="button" class="btn btn-secondary mt-2 remove-genre">-</button>
    `;
    const genresInputs = clone.querySelectorAll('input[name="genres_name"]');
    genresInputs.forEach((input) => {
        input.value = '';
    });
    const addButtons = clone.querySelectorAll(".add-genre");
    const removeButton = clone.querySelector(".remove-genre");

    addButtons.forEach((button) => {
        button.addEventListener("click", () => {
            addButtonClicked(button);
        });
    });

    removeButton.addEventListener("click", () => {
        removeButtonClicked(removeButton);
    });

    parentDiv.after(clone);
});

function addButtonClicked(button) {
    const parentDiv = button.closest(".genre-parent");
    const clone = parentDiv.cloneNode(true);


    const buttonsDiv = clone.querySelector(".buttons");
    buttonsDiv.innerHTML = `
        <button type="button" class="btn btn-secondary mt-2 add-genre">+</button>
        <button type="button" class="btn btn-secondary mt-2 remove-genre">-</button>
    `;
    const genresInputs = clone.querySelectorAll('input[name="genres_name"]');
    genresInputs.forEach((input) => {
        input.value = '';
    });
    const addButtons = clone.querySelectorAll(".add-genre");
    const removeButton = clone.querySelector(".remove-genre");

    addButtons.forEach((button) => {
        button.addEventListener("click", () => {
            addButtonClicked(button);
        });
    });

    removeButton.addEventListener("click", () => {
        removeButtonClicked(removeButton);
    });

    parentDiv.after(clone);
}

function removeButtonClicked(button) {
    const parentDiv = button.closest(".genre-parent");
    parentDiv.remove();
}

// Select the parent div element that will be cloned
const parentalDiv = document.querySelector('.coauthor-parent');

// Select the "Add Coauthor" button that will trigger the cloning functionality
const addsButtons = document.querySelector('.add-coauthor');

// Add a click event listener to the "Add Coauthor" button
addsButtons.addEventListener('click', () => {
    // Clear all input fields within the cloned div

    // Clone the parent div element and all its child elements
    const cloneddDiv = parentalDiv.cloneNode(true);
    const buttonsDivs = cloneddDiv.querySelector(".buttons");
    buttonsDivs.innerHTML = `
      <button type="button" class="btn btn-secondary mt-2 add-coauthor">+</button>
      <button type="button" class="btn btn-secondary mt-2 remove-coauthor">-</button>
  `;
    const coauthorInputs = cloneddDiv.querySelectorAll('input[name="coauthors_name"]');
    coauthorInputs.forEach((input) => {
        input.value = '';
    });
    const adddButtons = cloneddDiv.querySelectorAll(".add-coauthor");
    const removeddButton = cloneddDiv.querySelector(".remove-coauthor");
    adddButtons.forEach((button) => {
        button.addEventListener("click", () => {
            adddButtonsClicked(button);
        });
    });

    removeddButton.addEventListener("click", () => {
        removedButtonsClicked(removeddButton);
    });

    parentalDiv.after(cloneddDiv);
});
function adddButtonsClicked(button) {
    const parentDiv = button.closest(".coauthor-parent");
    const cloneddDiv = parentDiv.cloneNode(true);
    const coauthorInputs = cloneddDiv.querySelectorAll('input[name="coauthors_name"]');
    coauthorInputs.forEach((input) => {
        input.value = '';
    });
    const buttonsDivs = cloneddDiv.querySelector(".buttons");
    buttonsDivs.innerHTML = `
      <button type="button" class="btn btn-secondary mt-2 add-coauthor">+</button>
      <button type="button" class="btn btn-secondary mt-2 remove-coauthor">-</button>
  `;
    const adddButtons = cloneddDiv.querySelectorAll(".add-coauthor");
    const removeddButton = cloneddDiv.querySelector(".remove-coauthor");
    adddButtons.forEach((button) => {
        button.addEventListener("click", () => {
            adddButtonsClicked(button);
        });
    });
    removeddButton.addEventListener("click", () => {
        removedButtonsClicked(removeddButton);
    });
    parentalDiv.after(cloneddDiv);
}

function removedButtonsClicked(button) {
    const parentalDiv = button.closest(".coauthor-parent");
    parentalDiv.remove();
}
function formatISBN() {
    var isbnInput = document.getElementById("isbn-input");
    var isbnValue = isbnInput.value.replace(/\D/g, "");

    if (isbnValue.length == 10) {
        isbnValue = isbnValue.substring(0, 1) + "-" + isbnValue.substring(1, 4) + "-" + isbnValue.substring(4, 9) + "-" + isbnValue.substring(9, 10);
    } else if (isbnValue.length == 13) {
        isbnValue = isbnValue.substring(0, 3) + "-" + isbnValue.substring(3, 4) + "-" + isbnValue.substring(4, 6) + "-" + isbnValue.substring(6, 12) + "-" + isbnValue.substring(12, 13);
    }

    isbnInput.value = isbnValue;
}
function removeISBNMask() {
    var isbnInput = document.getElementById("isbn-input");
    var isbnValue = isbnInput.value.replace(/-/g, "");
    isbnInput.value = isbnValue;
}
// Get the form field and the error element
const title = document.getElementById("id_title");
const author = document.querySelector('#id_author_name');
const coauthor = document.querySelector('#co_authors');
const publisher = document.querySelector('#id_publisher_name');
const genres = document.querySelector('#id_genres_name');
const edition = document.querySelector('#id_edition');
const error = document.querySelector('.invalid-feedback');

// Define a regular expression that matches special characters
const regex = /[!@#$%^&*()_+\=\[\]{};':"\\|,<>\/?]/;

// Listen for the form input event
title.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(title.value)) {
        // Show the error message
        document.getElementById("title-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("title-error").style.display = "none";
    }
});
author.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(author.value)) {
        // Show the error message
        document.getElementById("author-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("author-error").style.display = "none";
    }
});
coauthor.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(coauthor.value)) {
        // Show the error message
        document.getElementById("coauthor-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("coauthor-error").style.display = "none";
    }
});
publisher.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(publisher.value)) {
        // Show the error message
        document.getElementById("publisher-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("publisher-error").style.display = "none";
    }
});
genres.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(genres.value)) {
        // Show the error message
        document.getElementById("genre-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("genre-error").style.display = "none";
    }
});
edition.addEventListener('input', () => {
    // Check if the field value contains a special character
    if (regex.test(edition.value)) {
        // Show the error message
        document.getElementById("edition-error").style.display = "block";
    } else {
        // Hide the error message
        document.getElementById("edition-error").style.display = "none";
    }
});