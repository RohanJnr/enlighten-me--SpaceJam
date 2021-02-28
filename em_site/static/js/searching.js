const singleBooksSearch = document.querySelector(".single-search-div")
const bundlesSearch = document.querySelector(".bundle-search-div")

const bookBtnSearch = document.getElementById("book-btn-search")
const bundleBtnSearch = document.getElementById("bundle-btn-search")

bookBtnSearch.addEventListener("click", e => {
    singleBooksSearch.style.display = "flex"
    bundlesSearch.style.display = "none"
})

bundleBtnSearch.addEventListener("click", e => {
    singleBooksSearch.style.display = "none"
    bundlesSearch.style.display = "flex"
})



