const booksTabBtn = document.getElementById("books-tab")
const OffersTabBtn = document.getElementById("offers-tab")
const TradesTabBtn = document.getElementById("trades-tab")

const btns = [booksTabBtn, OffersTabBtn, TradesTabBtn]

btns.forEach(btn => {
    btn.addEventListener("click", e => {
        const target = e.target
        const visible = target.getAttribute("data-visible")
        const inVisible = target.getAttribute("data-invisible").split(",")

        document.getElementById(visible).style.display = "flex"
        inVisible.forEach(item => {
            document.getElementById(item).style.display = "none"
        })
    })
})